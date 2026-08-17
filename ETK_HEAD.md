# ETK — HEAD (stare curentă)
**Proiecție a jurnalului · reconstruit 2026-08-17 · NU se editează de mână**

> **Vârf:** v3.101 · Partea CV (2026-08-16)  
> **Sursă:** `ETK_LEDGER.md`  
> **STARE:** Acoperire **0/I → Partea CV** (v3.101) · 12 părți-append indexate viu · ERA I (0–XLIV) pliată · regenerat 2026-08-17  
> **Regulă:** HEAD = artefact de build ȘI autoritatea de stare (LXXXIV). INDEX-ul de mai jos e REGENERAT din markerii `# APPEND` — nu-l citi din jurnal (acolo e înghețat). Orice schimbare aterizează întâi în jurnal (append + grep), apoi se re-rulează `etk_project_head.py`.
> **📤 PROCEDURĂ UPLOAD (regulă vie, imună la `-N`):** la finalul sesiunii operatorul urcă **DOAR 2 fișiere** — jurnalul nou `ETK_LEDGER_v3_XX_<stamp>.md` + `ETK_HEAD.md` — și **șterge jurnalul precedent** (ca să nu se adune). Tooling-ul (`etk_ledger_commit.py` + `etk_project_head*.py`) se urcă **o singură dată**. Append-urile **NU se urcă** (commit-ul le pliază). **Interfața poate adăuga sufixe `-N` la upload — E INOFENSIV:** pipeline-ul e imun (commit-ul alege automat jurnalul cel mai recent + proiectorul cel mai capabil, indiferent de `-N`). **Nu redenumi nimic** — singurul gest de igienă e ștergerea jurnalului vechi.

---

## 🗺 INDEX PĂRȚI — regenerat, viu (12 părți-append)
*Era append XLV→vârf, proiectată din jurnal la fiecare build (O1, fix M-2/M-3). ERA I (0–XLIV) = pliată/înghețată.*

- **v3.90 · Partea XCIV** (2026-08-13) — XCIV.1 Defectul — prins prin test funcțional, nu inspecție
- **v3.91 · Partea XCV** (2026-08-15) — XCV.1 Defectul — narat în XCIV, absent de pe disc (prins prin grep + rulare)
- **v3.92 · Partea XCVI** (2026-08-15) — XCVI.1 Cele patru inserții — ce s-a aterizat și unde
- **v3.93 · Partea XCVII** (2026-08-15) — XCVII.1 Ce s-a reconciliat și cum
- **v3.94 · Partea XCVIII** (2026-08-15) — XCVIII.1 Coeficienții calibrați (8) — valoare + țintă + status
- **v3.95 · Partea XCIX** (2026-08-15) — XCIX.1 Coada de priorități parcată (autoritate de stare)
- **v3.96 · Partea C** (2026-08-15) — C.1 Ancore primare VERIFICATE (disponibile pt P1/P2/P4)
- **v3.97 · Partea CI** (2026-08-15) — CI.1 Cele 3 secundare verificate (adăugate la pool)
- **v3.98 · Partea CII** (2026-08-16) — CII.1 Dispoziție (decizie Alexandru)
- **v3.99 · Partea CIII** (2026-08-16) — CIII.1 Ce s-a verificat (gate + disc + primar)
- **v3.100 · Partea CIV** (2026-08-16) — CIV.1 FSSP v2_6 — container reparat (A4 ÎNCHIS)
- **v3.101 · Partea CV** (2026-08-16) — CV.1 Reverificare — verdict pe starea reală (disc acum)

---

## ⚠ ERORI / FLAG-URI ACTIVE (6)
*Doar cele deschise. Cele închise trăiesc în jurnal.*

- C-2 (marcaj specie — gata)
- FEP_integ_TVK (pending Ororbia&Friston 2023 + Kleiner 2024)
- eCB_tonus_Modul_v1 (R-41; „mergi")
- clase-capcană T11/T12/T13
- FLAG OR Cochran (R-43)
- FSSP ODE — a_NM/g_NM [S] + Q_opt.

_Erori închise (în jurnal, nu aici): ~0._

---

## 🔧 MUNCĂ DESCHISĂ / PENDING

- VI.1 FSSP — blocul matematic. Cel mai mare deficit unic. TOT PENDING
- Nuanță: în v3.2 σ e rezolvat prin derivare (P6) → pentru coloana de publicare, delta σ nu mai e necesar. Pentru ACPS_v13 și TDSAF rămâne deschis, iar 
- VI.10 Fișiere: livrate 23 iul / de șters
- ⚠ ÎNCĂ PREZENTE, de șters DUPĂ verificarea merge-ului: ETK_1.md · ETK_AVP_2.md · ETK_SCRISOARE_INSTANTA_v2/v3/v4 · ETK_INSERTII_PENDINTE_CONSOLIDAT_20
- 🔴 NECITIT ÎNCĂ: BioSkepsis_VAL3_Intrebari_2026-07-17.md — singurul fișier .md din proiect pe care nicio instanță nu l-a deschis. Conține întrebările V
- X.5 Ce rămâne deschis, onest
- 2. Veriga AVP→ATP rămâne slabă, single-lab (B-25). Ancora oferită (32406599) e review, re-descrie Haam/Tasker — nu replicare independentă. Route C răm
- 3. Q3-specific rămâne deschis (B-21). Disocierea generală 2-AG/AEA = (C), dar replicarea OXTR→AEA în SON de grup non-Tasker nu a fost livrată — „Cover
- XII.3 Corecții de corpus PENDING (nu executate — așteaptă „mergi" pe corpus)
- ⛔ PROBLEMĂ: Registrul_Master a fost SUPERSEDAT de Registrul General v1→v3.x (autoritatea unică). Munca din 04 iul a fost scrisă într-o bază stale → ex
- XXV.1 ⚠ FLAG DESCHIS — „Menuet 2025" (clasa Cochran)
- Capetele canonice satelit = versiunile „-1" — nu le confunda cu duplicate de șters.
- → NU se marchează pentru ștergere înainte de a conserva $I_i$. Parcat la XXXII.4. După parcare: update_Qualia = sigur de șters (conținut unic conserva
- Task 1 ✅ · Task 2 ✅ · Task 3 ✅ · Task 4 ✅ (diligență; alinierea de nume = decizie operator) · Task 5 ✅ (verdict + $I_i$ parcat; update_Qualia sigur de
- PARTEA XLI — TRIAJ ALERTE BIOSKEPSIS (inbound) vs. ÎNTREBĂRILE DESCHISE ETK (30 iul)
- FSSP v2: drafturi gata; bloc matematic per VI.1 PENDING (neverificat în această pasă).
- np5 (branch parcat): aceleași fantome (Moore L721/L2789, Dye L793, Alaerts Nat Commun L2677) — de reparat la merge, cu re-etichetarea D-EPI (XXXIV.6 /
- XLIX.5 Semnalat — rămâne deschis (real)
- 6. v4_2 cadru „moștenire transgenerațională, oferă cadru unificator": frază teoretică (nu citare) — NEATINSĂ. Opțiune: păstrează ca ipoteză modelată S
- LXIX.3 Abateri de reparat (înainte de absorbție)
- LXX.3 Abateri de reparat (înainte de absorbție)
- *Se stivuiește PESTE v3.68 (Partea LXXII). Titlu „v3.69 (2026-08-09)"; changelog sub v3.68; adaugă Partea LXXIII; adaugă v3.68 la „AUTORITATEA UNICĂ".
- FLAG OR Cochran rămâne DESCHIS — endpoint-ul PMC a dat doar abstract; verificarea la corpul full-text (singura cale de ridicare a interdicției, LXXVI.
- T14 / dispoziție operator: rezidualul structural al pliererii (3 coliziuni) = închis prin ratificare -a/-b zero-risc; atașamentul verificat cu 4 corec
- LXXX.3 MANIFEST DE ȘTERGERE — sigure de șters (subsumate 100%)

---

## 📚 REFERINȚE — verdict curent (59)
*Cea mai recentă mențiune per ID câștigă. ⛔=neverificat/blocat · ✔/✅=verificat · (C)/(D)/(S)=marcaj epistemic · ⚠=rezervă.*

| ID | Referință | Subiect | Verdict |
|----|-----------|---------|---------|
| R-07 | Hirasawa 2004, *J Physiol* 559:611, PMID 15254151 | DSI/DSE la neuroni OXT/AVP | ⛔ |
| R-10 | Oliet SHR, Baimoukhametova DV, Piet R, Bains JS (2007), *J Neurosci* 27(6):1325–1333, DOI 10.1523/JNEUROSCI.2676-06.2007 | OXTR→eCB retrograd = ancora ACK | ✔ |
| R-13 | Hashimotodani/Ohno-Shosaku/Kano 2010 | „orice Gq recrutează 2-AG" | ⛔ |
| R-17 | Di S, Popescu IR, Tasker JG (2013), *J Neurosci* 33:18331, PMID 24227742 | E-13 | ✔ |
| R-25 | Kagerbauer 2013 (23574490); 2019 (31538678); Barreca 1988 (3220462); Mindt 2019 (30194934) | copeptina = numărătorul `Pc_AVP_CLINICAL` | ⛔ |
| R-26 | „Tan et al. 2019" → Terrillon 2003 | heterodimer OXTR/V1aR → LS ca nod-PIVOT, `C(t)=max` | ⛔ |
| R-28 | Kelly AM, Ong JY, Witmer R, Ophir AG (2020), *Sci Adv* 6(36):eabb9116, PMID 32917597 | ε_AVP, Modulul #1 | ✔ |
| R-31 | Bardeleben/Holsboer 1985 (2997567, UMAN); Hohnloser 1989 (2557988, UMAN); Rabadán-Diehl 1998 (9645696); Ma & Aguilera 19 | ireversibilitatea Pc (D-1) | ✔ |
| R-34 | Song Z, Albers HE (2018), *Front Neuroendocrinol* 51:14–24, DOI 10.1016/j.yfrne.2017.10.004, PMID 29054552 | reactivitate încrucișată AVP↔OXTR | (C) |
| R-35 | Haam J, Halmos K, Di S, Tasker J (2014), *J Neurosci* 34:6201–6213, PMID 24790191 (+ review 28035187) | brațul AVP astrocitar | ⚠ |
| R-36 | Iremonger, Kuzmiski, Baimoukhametova, Bains (2011), *J Neurosci* 31:12011, PMID 21849561 | candidat detector de coincidență | ⚠ |
| R-37 | Tretiakov, Hevesi, Böröczky, Alpár, Harkany, Keimpema (2025), *Cells* 14, PMID 40497964 | gardianul glial | ✔ |
| R-38 | PMID 24227742, brațul glial | triada nașterii | ⚠ |
| R-39 | decalajul specie | — | ⛔ |
| R-40 | (rezervat) | — |  |
| R-41 | PMID 24227742, finding #13 (Results) | disocierea 2-AG / AEA | ⚠ |
| R-42 | secvența dezvoltării CB1/DAGLα | — | ⚠ |
| R-43 | Cochran JN et al. (2020), *Am J Hum Genet* 106(5):632–645, DOI 10.1016/j.ajhg.2020.03.010, PMID 32330418 + Holstege 2020 | TET2 → neurodegenerare | ⛔ |
| R-44 | George K, Hoang HTM, Tibbs T, …, Ahmad M (2024), *iScience* 27(6):110047, PMID 38883814, PMC11179071 | cinetică OXTR neuronală | ✔ |
| R-45 | Iremonger KJ, Bains JS (2009), *J Neurosci* 29(22):7349–7358, PMID 19494156, PMC6666467 | dinorfină ca mesager retrograd al neuronilor VP | ✔ |
| R-46 | Hatton GI et al. (1992), PMID 1393572 · Chen Y, Zhao Z, Hertz L (2000), *J Neurosci Res* 60(6):761–766, PMID 10861788 ·  | AVP → Ca²⁺ astrocitar | ✔ |
| R-47 | Moeller HB, Fenton RA, Zeuthen T, Macaulay N (2009). Vasopressin-dependent short-term regulation of aquaporin 4 expresse | AVP → V1aR → PKC → Ser180 → internalizare AQP4 | (D) |
| R-47b | Niermann H, Amiry-Moghaddam M, Holthoff K, Witte OW, Ottersen OP (2001). A Novel Role of Vasopressin in the Brain: Modul | AVP → V1a → flux de apă activitate-dependent + geometria spa | (D) |
| R-47c | ⚠ PMID 25231107 (2014) — *„AQP4 plasma membrane trafficking or channel gating is NOT significantly modulated by phosphor | contestarea Ser180 · dependența de scală temporală | ⛔ |
| R-48 | Du W, Stern JE, Filosa JA (2015), *J Neurosci* 35:5330–5341, PMID 25834057 | AVP dendritic → cuplare neurovasculară | (D) |
| R-49 | Crosby 2018 (30108130, DMH) · Xu 2016 (27559172, ARC/P2X4) · Bhattacharya 2013 (23637193, SCN/P2X2) | ATP astrocitar → P2X presinaptic → ↑GABA | ✔ |
| R-50 | Yokoyama 2009 (19732292) · Soldo 2003 (14645448) | ghrelină → eliberare somatodendritică de AVP | ✔ |
| R-51 | Shimizu T, Yokotani K (2008), *Eur J Pharmacol* 582(1-3):62–69, PMID 18234185 · Ruginsk SG et al. (2015), *Am J Physiol  | eCB pe axa AVP | (D) |
| R-52 | Kim 2020 (32066670) · Wingenfeld 2021 (33542190) · Wieder 2021 (34079501) · Unternaehrer 2015 (26061800) · Jack, Connell | metilarea OXTR la om | ✔ |
| R-53 | Ororbia A, Friston K (2023), arXiv:2311.09589 | Puntea mortalitate↔FEP e construită de Friston însuși. Axiom |  |
| R-54 | Kleiner J (2024), arXiv:2403.03925 | Funcționalismul computațional implică computația muritoare → |  |
| R-55 | Hinton G (2022), arXiv:2212.13345 | Verificat. Nota ACPS că nu e proceedings NeurIPS e corectă |  |
| R-56 | Grossman P et al. (2026), *Clin Neuropsychiatry* 23(1):100–112 | Invalidează localizarea vagală dorsală. PDF în proiect |  |
| R-57 | Smith R, Kuplicki R et al. (33315893), N=500 | Repaus: precizie egală; perturbare (apnee): martorii cresc,  |  |
| R-58 | 20692645 · 39187192 · 35479498 · 36543824 · 24587061 | Dihotomia clinică anxios/anhedonic există deja. ACPS derivă, |  |
| R-59 | Towers AJ, Tremblay M, Chung L, Li X, Bey AL, Zhang W, et al. (2018). Epigenetic dysregulation of Oxtr in Tet1-deficient | TET1 ↔ OXTR | ⛔ |
| R-60 | Harrison IF et al. (2020), *Brain* 143:2576–2593, PMID 32705145 · Yang J et al. (2011), PMID 21891870 · Aalling N et al. | polarizarea AQP4 ↔ clearance ↔ AD | (D) |
| R-61 | Bielsky IF, Hu SB, Ren X, Terwilliger EF, Young LJ (2005), *Neuron* 47:503–513, PMID 16102534 | ancoră LS candidată pentru recunoașterea socială | (D) |
| R-62 | Tanoue A, Ito S, Honda K, Oshikawa S, Kitagawa Y, Koshimizu T-A, Mori T, Tsujimoto G (2004), *J Clin Invest* 113(2):302– | identitatea de subtip V1bR pe corticotropi (ancora cauzală a | (C) |
| R-63 | Murat B, Devost D, Andrés M, Mion J, Boulay V, Corbani M, Zingg HH, Guillon G (2012), *Mol Endocrinol* 26(3):502–520, DO | heterodimer V1b–CRHR1 → sinergie AVP+CRH (mecanismul „claim  | (D) |
| R-64 | von Bardeleben U, Holsboer F, Stalla GK, Müller OA (1985), *Life Sci* 37(17):1613–1618, DOI 10.1016/0024-3205(85)90480-1 | ancora umană a escape-ului AVP+CRH din dexametazonă (fenomen | (D) |
| R-65 | Brezivaptan (DCI) = ANC-501 = THY-1773 = TS-121, CAS 1370444-22-6, C25H30ClN5O3; antagonist V1b/AVPR1B selectiv, Taisho→ | identitatea de asset V1b (corecție de consolidare D3) | (C) |
| R-66 | Maejima Y et al. (2025). Oxytocin Enhances Demethylation Through TET Enzyme Expression in Neurons of Aged Mice. *Aging C | OXTR→TET2 (veriga de intrare a lanțului AD/îmbătrânire) | (D) |
| R-67 | Huang SY, Zhang YR, Guo Y, et al. (2024). Glymphatic system dysfunction predicts amyloid deposition, neurodegeneration,  | inversiunea cauzală: ALPS precede Aβ (keystone-ul lanțului A | (D) |
| R-68 | Xie X, Li H, Chang Y, et al. (2026). Aquaporin-4 Dysfunction in Depression: From Pathogenic Mechanisms to Novel Therapeu | AQP4↔depresie (relevant NP_Depresia + teza AVP/clearance) | (S) |
| R-69 | He F, Wu H, Zhou L, Lin Q, Cheng Y, Sun YE (2020). Tet2-mediated epigenetic drive for astrocyte differentiation from emb | veriga TET2 → AQP4 (mijlocul lanțului AD) | (D) |
| R-71 | Wang M, Yan C, Li X, Yang T, Wu S, Liu Q, et al. (2024). Non-invasive modulation of meningeal lymphatics ameliorates age | glimfatic/mLV ↔ enrichment OXT | (D) |
| R-72 | Asaba T, Hamano S, Nanmo A, Seo J, Kageyama T, Fukuda J. (2025). Human iPSC-derived cerebral organoids reveal oxytocin-m | OXT→OTR-microglie→TREM2→clearance Aβ (UMAN) | (D) |
| R-73 | Amato S, Averna M, Farsetti E, Guidolin D, et al. (2024). Control of Dopamine Signal in High-Order Receptor Complex on S | OTR pe astrocit → Ca²⁺/glutamat (mozaic A2A-D2-OTR) | (D) |
| R-74 | Zhang Y, Tang C, He Y, et al. (2024). Semaglutide ameliorates Alzheimer's disease and restores oxytocin in APP/PS1 mice  | terapie AD ↔ ↑OXT | (D) |
| R-75 | Mesbah-Benmessaoud O, Benabdesselam R, Hardin-Pouzet H, Dorbani-Mamine L, Grange-Messent V. (2011). Cellular and subcell | AQP4 în granule neurosecretorii OXT/AVP; osmo-responsiv | (C) |
| R-76 | Ida KK, Otsuki DA, Sasaki ATC, …, Malbouisson LMS (2015). Effects of terlipressin as early treatment for protection of b | agonist V1 (terlipresină) ↔ AQP4 cortical (animal MARE) | (D) |
| R-77 | Fill Malfertheiner S, Bataiosu-Zimmer E, Michel H, Fouzas S, Bernasconi L, Bührer C, Wellmann S (2021). Vasopressin but  | KEYSTONE §VIII.4 — surge-ul AVP la naștere; C-section îl oco | (D) |
| R-78 | Kenkel W (2020). Birth signalling hormones and the developmental consequences of caesarean delivery. *J Neuroendocrinol* | TDSAF — hormonii de naștere ↓ după cezariană | (D) |
| R-79 | Altstein M, Gainer H (1988). Differential biosynthesis and posttranslational processing of vasopressin and oxytocin in r | AVP-first ontogenetic (susține asimetria §VIII.2 „mediu înai | (D) |
| R-80 | Grinevich V, Desarménien MG, Chini B, Tauber M, Muscatelli F (2015). Ontogenesis of oxytocin pathways in the mammalian b | OXT maturare târzie (majoritar postnatal) | (D) |
| R-81 | Theofanopoulou C, Gedman G, Cahill JA, Boeckx C, Jarvis ED (2021). Universal nomenclature for oxytocin-vasotocin ligand  | filogenie OT/VT — VT reține mai mult din secvența parentală | (D) |
| R-82 | Clarke L, Gesundheit N, Sherr EH, Hardan AY, Parker KJ (2024). Vasopressin deficiency: a hypothesized driver of both soc | CONVERGENȚĂ CLINICĂ cu §VIII: Parker leagă AVP-deficit de de | (D) |
| R-83 | Talbot CF, Oztan O, …, Capitanio JP, Parker KJ (2024). Nebulized vasopressin penetrates CSF and improves social cognitio | replicare NHP a ipotezei AVP-deficit (completează R-27/R-29) | (D) |

---
*Generat de etk_project_head.py din ETK_LEDGER.md. 59 referințe · 6 active · 25 deschise. Pentru istorie/provenență → jurnalul.*