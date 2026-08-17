#!/usr/bin/env python3
"""
etk_project_head.py — Proiectorul HEAD al Registrului ETK.

CE FACE (pe scurt):
  Citește Registrul-jurnal (append-only, imutabil) și emite o pagină de stare
  curentă, mică, structurată — ETK_HEAD.md. HEAD e un ARTEFACT DE BUILD:
  se regenerează din jurnal, NU se scrie de mână. Dacă HEAD diverge de jurnal,
  se re-rulează scriptul, nu se editează HEAD.

CUM (mecanic):
  - Vârful: ultima secțiune "# APPEND — vX.Y · Partea Z".
  - Erori active: ultima linie "ACTIVE:" din secțiunea ERORI (cea mai recentă câștigă).
  - Erori închise: se numără (trăiesc în jurnal, nu în HEAD).
  - Referințe R-xx: fiecare rând "| **R-xx** | referință | subiect | verdict | status |".
  - Muncă deschisă: linii cu markeri de deschidere (DESCHIS/PENDING/de șters/necitit...).

Utilizare:
  python etk_project_head.py <registru.md> [-o ETK_HEAD.md]
"""
import re, sys, argparse, datetime

VERDICT_SYMBOLS = ["⛔", "✔", "✅", "⚠", "(C)", "(D)", "(S)", "[C]", "[D]", "[S]"]

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def last_head(text):
    """Ultimul APPEND = vârful curent."""
    heads = re.findall(r"# APPEND — (v[\d.]+)\s*\(([^)]*)\)\s*·\s*(Partea [IVXLCDM]+)", text)
    if heads:
        v, date, part = heads[-1]
        return v, date, part
    # fallback: banner "vârf vX.Y · Partea Z"
    m = re.findall(r"vârf\s+\*\*(v[\d.]+)\s*·\s*(Partea [IVXLCDM]+)", text)
    if m:
        return m[-1][0], "?", m[-1][1]
    return "?", "?", "?"

def active_errors(text):
    """Ultima linie 'ACTIVE:' câștigă (cea mai recentă stare)."""
    blocks = re.findall(r"\*\*ACTIVE:\*\*(.+)", text)
    if not blocks:
        return []
    line = blocks[-1]
    # taie la sfârșit de paragraf
    line = line.split("\n")[0]
    items = [re.sub(r"\*\*|`", "", x).strip(" ·") for x in line.split("·")]
    return [i for i in items if i]

def count_closed(text):
    blocks = re.findall(r"\*\*ÎNCHISE:\*\*(.+)", text)
    if not blocks:
        return 0
    line = blocks[-1].split("\n")[0]
    ids = re.findall(r"E-\d+|C-\d+", line)
    return len(set(ids))

def references(text):
    """Rânduri de tabel R-xx. Extrage ID, referință scurtă, verdict, status scurt."""
    rows = re.findall(r"^\|\s*\*\*(R-\d+[a-z]?)\*\*\s*\|(.+)$", text, re.MULTILINE)
    seen = {}
    for rid, rest in rows:
        cells = [c.strip() for c in rest.split("|")]
        ref = re.sub(r"\*\*", "", cells[0])[:120] if cells else ""
        subject = re.sub(r"\*\*", "", cells[1])[:60] if len(cells) > 1 else ""
        verdict = ""
        for c in cells[2:]:
            for s in VERDICT_SYMBOLS:
                if s in c:
                    verdict = s; break
            if verdict: break
        # status = ultima celulă, scurtată la prima propoziție
        status = re.sub(r"\*\*|`", "", cells[-1]) if len(cells) > 3 else ""
        status = status.split(".")[0][:90]
        seen[rid] = (ref, subject, verdict, status)   # ultimul câștigă
    return seen

def open_work(text):
    """Linii care semnalează muncă deschisă. Deduplicate, scurtate."""
    markers = ["DESCHIS", "PENDING", "NEATINS", "NECITIT", "de șters", "TOT PENDING",
               "rămâne deschis", "de reparat", "în așteptarea deciziei"]
    out = []
    for line in text.split("\n"):
        if not any(m in line for m in markers):
            continue
        # scoate zgomotul: rânduri de tabel, linii de changelog, dumpuri ACTIVE/ÎNCHISE
        if line.lstrip().startswith("|"):        # rând de tabel
            continue
        if re.match(r"\s*\*?\(v[\d.]+:", line):   # linie de changelog
            continue
        if "ACTIVE:" in line or "ÎNCHISE:" in line:
            continue
        clean = re.sub(r"\*\*|`|>|#|^\s*-\s*", "", line).strip()
        if len(clean) > 25:
            out.append(clean[:150])
    # dedup păstrând ordinea
    seen, uniq = set(), []
    for x in out:
        k = x[:50]
        if k not in seen:
            seen.add(k); uniq.append(x)
    return uniq[:25]

def part_index(text, window=12):
    """O1 (fix M-2/M-3): INDEX de părți regenerat viu din markerii `# APPEND`.
    Titlul = primul heading `## ` de după marker care NU e 'LINIE DE CHANGELOG'.
    Determinist, din jurnal — nu se citește indexul înghețat din antet."""
    lines = text.split("\n")
    marks = []  # (linie_idx, v, date, part)
    hdr = re.compile(r"^# APPEND — (v[\d.]+)\s*\(([^)]*)\)\s*·\s*(Partea [IVXLCDM]+)")
    for i, ln in enumerate(lines):
        m = hdr.match(ln)
        if m:
            marks.append((i, m.group(1), m.group(2), m.group(3)))
    entries = []
    for k, (idx, v, date, part) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        title = ""
        for j in range(idx + 1, end):
            s = lines[j].strip()
            if s.startswith("## ") and "LINIE DE CHANGELOG" not in s.upper():
                title = s[3:].strip()
                break
        entries.append((v, date, part, title))
    return entries, len(marks)


def build_head(path):
    text = read(path)
    v, date, part = last_head(text)
    act = active_errors(text)
    closed_n = count_closed(text)
    refs = references(text)
    openw = open_work(text)
    today = datetime.date.today().isoformat()

    L = []
    L.append("# ETK — HEAD (stare curentă)")
    L.append(f"**Proiecție a jurnalului · reconstruit {today} · NU se editează de mână**")
    L.append("")
    L.append(f"> **Vârf:** {v} · {part} ({date})  ")
    L.append(f"> **Sursă:** `{path.split('/')[-1]}`  ")
    idx_entries, n_marks = part_index(text)
    win = idx_entries[-12:]
    L.append(f"> **STARE:** Acoperire **0/I → {part}** ({v}) · {len(win)} părți-append indexate viu · ERA I (0–XLIV) pliată · regenerat {today}  ")
    L.append(f"> **Regulă:** HEAD = artefact de build ȘI autoritatea de stare (LXXXIV). INDEX-ul de mai jos e REGENERAT din markerii `# APPEND` — nu-l citi din jurnal (acolo e înghețat). Orice schimbare aterizează întâi în jurnal (append + grep), apoi se re-rulează `etk_project_head.py`.")
    L.append(f"> **📤 PROCEDURĂ UPLOAD (regulă vie, imună la `-N`):** la finalul sesiunii operatorul urcă **DOAR 2 fișiere** — jurnalul nou `ETK_LEDGER_v3_XX_<stamp>.md` + `ETK_HEAD.md` — și **șterge jurnalul precedent** (ca să nu se adune). Tooling-ul (`etk_ledger_commit.py` + `etk_project_head*.py`) se urcă **o singură dată**. Append-urile **NU se urcă** (commit-ul le pliază). **Interfața poate adăuga sufixe `-N` la upload — E INOFENSIV:** pipeline-ul e imun (commit-ul alege automat jurnalul cel mai recent + proiectorul cel mai capabil, indiferent de `-N`). **Nu redenumi nimic** — singurul gest de igienă e ștergerea jurnalului vechi.")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## 🗺 INDEX PĂRȚI — regenerat, viu ({len(win)} părți-append)")
    L.append("*Era append XLV→vârf, proiectată din jurnal la fiecare build (O1, fix M-2/M-3). ERA I (0–XLIV) = pliată/înghețată.*")
    L.append("")
    for ev, edate, epart, etitle in win:
        tail = f" — {etitle}" if etitle else ""
        L.append(f"- **{ev} · {epart}** ({edate}){tail}")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## ⚠ ERORI / FLAG-URI ACTIVE ({len(act)})")
    L.append("*Doar cele deschise. Cele închise trăiesc în jurnal.*")
    L.append("")
    if act:
        for a in act:
            L.append(f"- {a}")
    else:
        L.append("- (niciuna extrasă — verifică secțiunea ERORI din jurnal)")
    L.append("")
    L.append(f"_Erori închise (în jurnal, nu aici): ~{closed_n}._")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 🔧 MUNCĂ DESCHISĂ / PENDING")
    L.append("")
    if openw:
        for w in openw:
            L.append(f"- {w}")
    else:
        L.append("- (niciuna extrasă)")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## 📚 REFERINȚE — verdict curent ({len(refs)})")
    L.append("*Cea mai recentă mențiune per ID câștigă. ⛔=neverificat/blocat · ✔/✅=verificat · (C)/(D)/(S)=marcaj epistemic · ⚠=rezervă.*")
    L.append("")
    L.append("| ID | Referință | Subiect | Verdict |")
    L.append("|----|-----------|---------|---------|")
    for rid in sorted(refs, key=lambda x: int(re.sub(r"\D", "", x))):
        ref, subj, verdict, status = refs[rid]
        cell = (verdict + " " + status).strip()
        L.append(f"| {rid} | {ref} | {subj} | {cell} |")
    L.append("")
    L.append("---")
    L.append(f"*Generat de etk_project_head.py din {path.split('/')[-1]}. "
             f"{len(refs)} referințe · {len(act)} active · {len(openw)} deschise. "
             f"Pentru istorie/provenență → jurnalul.*")
    return "\n".join(L)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("registru")
    ap.add_argument("-o", "--out", default="ETK_HEAD.md")
    a = ap.parse_args()
    head = build_head(a.registru)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(head)
    print(f"HEAD scris: {a.out}  ({len(head)} caractere)")
