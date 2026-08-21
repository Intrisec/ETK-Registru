# ETK — HEAD (stare curentă)
**Proiecție a jurnalului · reconstruit 2026-08-21 · NU se editează de mână**

> **Vârf:** v3.122 · Partea CXXVI (2026-08-21)  
> **Sursă:** `ETK_LEDGER.md`  
> **STARE:** Acoperire **0/I → Partea CXXVI** (v3.122) · 12 părți-append indexate viu · ERA I (0–XLIV) pliată · regenerat 2026-08-21  
> **Regulă:** HEAD = artefact de build ȘI autoritatea de stare (LXXXIV). INDEX-ul de mai jos e REGENERAT din markerii `# APPEND` — nu-l citi din jurnal (acolo e înghețat). Orice schimbare aterizează întâi în jurnal (append + grep), apoi se re-rulează `etk_project_head.py`.
> **📤 PROCEDURĂ UPLOAD (regulă vie, imună la `-N`):** la finalul sesiunii operatorul urcă **DOAR 2 fișiere** — jurnalul nou `ETK_LEDGER_v3_XX_<stamp>.md` + `ETK_HEAD.md` — și **șterge jurnalul precedent** (ca să nu se adune). Tooling-ul (`etk_ledger_commit.py` + `etk_project_head*.py`) se urcă **o singură dată**. Append-urile **NU se urcă** (commit-ul le pliază). **Interfața poate adăuga sufixe `-N` la upload — E INOFENSIV:** pipeline-ul e imun (commit-ul alege automat jurnalul cel mai recent + proiectorul cel mai capabil, indiferent de `-N`). **Nu redenumi nimic** — singurul gest de igienă e ștergerea jurnalului vechi.

---

## 🗺 INDEX PĂRȚI — regenerat, viu (12 părți-append)
*Era append XLV→vârf, proiectată din jurnal la fiecare build (O1, fix M-2/M-3). ERA I (0–XLIV) = pliată/înghețată.*

- **v3.110 · Partea CXIV** (2026-08-19) — CXIV.1 Reîncadrarea flag-ului Mesman
- **v3.111 · Partea CXV** (2026-08-19) — CXV.1 FAZA 0.4 — PF-04457845 aterizat (RAPORT_SUPERPOZITIE, axa eCB/Med)
- **v3.112 · Partea CXVI** (2026-08-19) — CXVI.1 Reîncadrarea țintei 0.5 (L-eCB-5)
- **v3.113 · Partea CXVII** (2026-08-19) — CXVII.1 FAZA 1 — aterizări corpus (`eCB_tonus_Modul_v1`)
- **v3.114 · Partea CXVIII** (2026-08-19) — CXVIII.1 Stare D1–D6 (verificat la sursă + disk)
- **v3.115 · Partea CXIX** (2026-08-20) — CXIX.1 Cele 4 direcții FAZA 3 — stare
- **v3.116 · Partea CXX** (2026-08-20) — CXX.1 GUARD Route B λ≡0 — verificat prezent+corect (neatins)
- **v3.117 · Partea CXXI** (2026-08-20) — CXXI.1 Amenințarea și neutralizarea
- **v3.118 · Partea CXXII** (2026-08-20) — CXXII.1 RASP — audit de independență (direcția dependenței)
- **v3.119 · Partea CXXIII** (2026-08-20) — CXXIII.1 Cochran — dispoziția canonică (dublă)
- **v3.120 · Partea CXXIV** (2026-08-20) — CXXIV.1 Aterizări (protocol + planificare)
- **v3.121 · Partea CXXV** (2026-08-21) — CXXV.1 Reverificare la primar — Runda Kimi R7 (ExtrapolareKimi + Raspuns_Nod_Kimi v2)

---

## ⚠ ERORI / FLAG-URI ACTIVE (21)
*Doar cele deschise. Cele închise trăiesc în jurnal.*

- C-2 (T-C2-1 la nod)
- a_NM (coliziune rezolvată a_NM^att)
- FEP_integ_TVK [S] (temă Kimi 4)
- clase-capcană T11/T12/T13
- FSSP ODE a_NM^rate/g_NM/γ_NM [S] neancorate, NU gated pe RASP (temă Kimi 1)
- G-ETK-R2/R3 (9 predicții [S], temă Kimi 3)
- G-ETK-3 AQP4-delocalizare [predicție neverificată] (temă Kimi 2)
- L-eCB-PTSD [D] (temă Kimi 5, cu avertisment)
- calibrare T_2AG^ev/T_AEA^ton = pending (nod)
- L-eCB-5 NEADMIS [S]
- ε_total candidat +ε_CB1R [S] (temă Kimi 4)
- T-eCB-ABX (nod)
- adiacență OXTR-metilare Braun/Bock [D] (nod)
- R-13 ⛔ argument-de-clasă only (nod marcaj)
- etk_reference_corrector.py hard-guard = ZIP pending redeploy
- G-RASP-1 = doar în ghid Alzheimer, de redenumit/separat (nod)
- ACPS_v14_FINAL_08-08 + v13 obsolete (P18-RASP vechi), neatinse; canonic ACPS = 0-4_RASPsep
- TheUpstream -1 = quasi-dup al -2, de reconciliat
- protocol de lucru canonic = SCRISOARE_CATRE_INSTANTA_v2
- teme Kimi active = SCRISOARE_CATRE_KIMI_v1
- T1/T4/ancore-cronice = pending la nod.

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

## 📚 REFERINȚE — verdict curent (83)
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
| R-41 | Di S, Popescu IR, Tasker JG (2013), *J Neurosci* 33(46):18331, PMC3828473, DOI 10.1523/JNEUROSCI.2971-12.2013 | 24227742 | (D) |
| R-42 | secvența dezvoltării CB1/DAGLα | — | ⚠ |
| R-43 | Cochran JN et al. (2020), *Am J Hum Genet* 106(5):632–645, DOI 10.1016/j.ajhg.2020.03.010, PMID 32330418, PMC7212268 | TET2→neurodegenerare: OR 2.3 (1.6–3.4) AD/FTD [Tab.2]; 3.1 ( | (C) |
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
| R-53 | Ororbia A, Friston K (2023), arXiv:2311.09589 | — | [S] |
| R-54 | Kleiner J (2024), arXiv:2403.03925 | — | [S] |
| R-55 | Hinton G (2022), arXiv:2212.13345 | — | [S] |
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
| R-66 | Maejima Y et al. (2025), *Aging Cell* 24(10):e70198, PMC12507420, DOI 10.1111/acel.70198 | 40788779 | (D) |
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
| R-93 | Inagaki TK, Muscatell KA, Irwin MR, Cole SW, Eisenberger NI (2012), *NeuroImage* 59(4):3222–3226, DOI 10.1016/j.neuroima | I(t)→amigdală→amenințare socială (reasignat din R-84/coliziu | (D) |
| R-94 | Bilbo SD et al. (2005), *J Neurosci* 25(35):8000–8009, DOI 10.1523/JNEUROSCI.1748-05.2005, PMID 16135757 | microglie primed (reasignat din R-85/coliziune) | (D) |
| R-95 | McLaughlin KA, Sheridan MA, Tibu F, Fox NA, Zeanah CH, Nelson CA (2015), *PNAS* 112(18):5637–5642, DOI 10.1073/pnas.1423 | BEIP: perioadă sensibilă umană <24/18 luni (ancoră A1/A6) | (C) |
| R-96 | Kang J et al. (2005), *Cell* 123(5):833–847, DOI 10.1016/j.cell.2005.09.011, PMID 16325578 | β-arrestin1 nuclear→p300→acetilare H4 (δ-opioid) — BARR-0 | (D) |
| R-97 | Gimpl G, Fahrenholz F (2001), *Physiol Rev* 81(2):629–683, DOI 10.1152/physrev.2001.81.2.629, PMID 11274341 | OXTR→Gq/11→PLCβ canonic (GATE3-1) | (C) |
| R-98 | Tronick E, Als H, Adamson L, Wise S, Brazelton TB (1978), *J Am Acad Child Psychiatry* 17(1):1–13, DOI 10.1016/s0002-713 | still-face original (perturbator g_NM) | (C) |
| R-99 | Feldman R, Gordon I, Zagoory-Sharon O (2010), *Dev Sci* 14(4):752–761, DOI 10.1111/j.1467-7687.2010.01021.x, PMID 216760 | pOT/sOT ↔ sincronie afectivă diadică (r=.34) — ancoră a_NM | (D) |
| R-100 | Cecil CAM et al. (2014), *Mol Psychiatry* 19(10):1071–1077, DOI 10.1038/mp.2014.95, PMID 25199917 | OXTR DNAm serial (ALSPAC, naștere/7/9) → CU 13 ani — traseu  | (D) |
| R-101 | Ziegler C et al. (2015), *Neuropsychopharmacology* 40(6):1528–1538, DOI 10.1038/npp.2015.2, PMID 25563749 | metilare OXTR ↔ anxietate socială/cortizol; „peripheral surr | (D) |
| R-102 | Thaler L et al. (2019), *Eur Eat Disord Rev* 28(1):79–86, DOI 10.1002/erv.2703, PMID 31823473 | metilare OXTR ↔ atașament nesecurizant (n=21 — slab) | (D) |
| R-103 | Scheffer M et al. (2009), *Nature* 461(7260):53–59, DOI 10.1038/nature08227, PMID 19727193 | early-warning / critical slowing down (ancoră metodă Th_ACK) | (C) |
| R-104 | Peters A, McEwen BS, Friston K (2017), *Prog Neurobiol* 156:164–188, DOI 10.1016/j.pneurobio.2017.05.004, PMID 28576664 | incertitudine/stres = entropie → sarcină alostatică; cea mai | (D) |
| R-105 | Adams RA et al. (2018), *J Neurosci* 38(44):9471–9485, DOI 10.1523/JNEUROSCI.3163-17.2018, PMID 30185463 | dinamică de atractor în credințe (Scz); INSTABILITATE (semn  | (C) |
| R-106 | Powers AR, Mathys C, Corlett PR (2017), *Science* 357(6351):596–600, DOI 10.1126/science.aan3458, PMID 28798131 | priori supra-ponderați (precizie RIDICATĂ) — opusul DU | (C) |
| R-107 | Durstewitz D, Huys QJM, Koppe G (2021), *Biol Psychiatry CNNI* 6(9):865–876, DOI 10.1016/j.bpsc.2020.01.001, PMID 322492 | aparatul formal al atractorilor patologici (oferă limbajul,  | (D) |
| R-108 | Braun PR et al. (2019), *Transl Psychiatry* 9(1):47, DOI 10.1038/s41398-019-0376-y, PMID 30705257 | concordanță sânge–creier per-CpG (IMAGE-CpG): mediu r≈0.86,  | (C) |
| R-109 | Edgar RD, Jones MJ, Meaney MJ, Turecki G, Kobor MS (2017), *Transl Psychiatry* 7(8):e1187, DOI 10.1038/tp.2017.171, PMID | BECon: concordanță blood–brain „tenuous", media | (C) |
| R-110 | Nishitani S et al. (2023), *Transl Psychiatry* 13(1):72, DOI 10.1038/s41398-023-02370-0, PMID 36843037 | AMAZE-CpG: replicare independentă (japoneză) a IMAGE-CpG (19 | (C) |
| R-111 | deRoon-Cassini TA et al. (2022), *Transl Psychiatry* 12(1):48 (Hillard coautor) | 35105857 | (D) |
| R-112 | Rajasekera TA, Spagnolo PA et al. (2025), *Prog Neuropsychopharmacol Biol Psychiatry* 142:111501 | 40967565 | (D) |
| R-113 | Demaili A, …, Braun K, Bock J (2023), *Front Cell Neurosci* 17:1129946, PMC9992175, DOI 10.3389/fncel.2023.1129946 | 36909279 | (D) |
| R-114 | Inada K, Hagihara M, …, Miyamichi K (2025), *Nat Commun* 16(1):10844 | 41372215 | (D) |
| R-115 | Couttas TA, Hoffmann AE, …, Rohleder C (2026), *Transl Psychiatry* 16(1), PMC13219800, DOI 10.1038/s41398-026-04120-4 (r | 42209468 | (C) |
| R-116 | Nave G, Camerer C, McCullough M (2015), *Perspect Psychol Sci* 10(6):772–789, DOI 10.1177/1745691615600138 | 26581735 | (C) |

---
*Generat de etk_project_head.py din ETK_LEDGER.md. 83 referințe · 21 active · 25 deschise. Pentru istorie/provenență → jurnalul.*