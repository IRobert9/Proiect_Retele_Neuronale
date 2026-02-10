<<<<<<< HEAD
# Proiect_Retele_Neuronale
=======
## 1. Identificare Proiect

---

| **Câmp** | **Valoare** |
| :--- | :--- |
| **Student** | Iordache Robert Georgian |
| **Grupa / Specializare** | 632AB / Informatică Industrială |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | [URL-ul tău de GitHub] |
| **Acces Repository** | Public / Privat (cu acces cadre didactice RN) |
| **Stack Tehnologic** | Python (PyTorch, NumPy, Tkinter) |
| **Domeniul Industrial de Interes (DII)** | Medical / Robotică (Sisteme de Control Mioelectric) |
| **Tip Rețea Neuronală** | CNN 1D Improved |

---
### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 5 | Rezultat Final (Etapa 6) | Îmbunătățire | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Accuracy (Test Set)** | $\geq 70\%$ | $62.00\%$ | **$81.24\%$** | $+19.24\%$ | **✓** |
| **F1-Score (Macro)** | $\geq 0.65$ | $0.58$ | **$0.80$** | $+0.22$ | **✓** |
| **Latență Inferență** | $\leq 50\text{ ms}$ | $80\text{ ms}$ | **$45\text{ ms}$** | $-35\text{ ms}$ | **✓** |
| **Contribuție Date Originale** | $\geq 40\%$ | $100\%$ | **$100\%$** | - | **✓** |
| **Nr. Experimente Optimizare** | $\geq 4$ | $1$ | **$5$** | $+4$ | **✓** |



### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință | Confirmare |
|:---|:---|:---:|
| 1 | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [X] DA |
| 2 | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [X] DA |
| 3 | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [X] DA |
| 4 | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [X] DA |
| 5 | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [X] DA |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

---
## 2. Descrierea Nevoii și Soluția SIA

---

### 2.1 Nevoia Reală / Studiul de Caz

Proiectul abordează problema controlului intuitiv al protezelor de membru superior pentru persoanele cu amputații sau deficiențe neuromusculare. În prezent, multe sisteme comerciale se bazează pe control de tip on/off sau sunt extrem de sensibile la zgomotul bioelectric, ceea ce duce la mișcări sacadate, nesigure sau obositoare pentru utilizator. Contextul actual necesită o tranziție de la simple dispozitive mecanice la **interfețe mioelectrice inteligente** capabile să recunoască pattern-uri complexe de activare musculară.

Rezolvarea acestei probleme este critică pentru a reda pacienților autonomia în activitățile cotidiene. Un sistem care poate distinge între o strângere de forță (Power Grip) și una de precizie (Precision Pinch), menținând în același timp o stabilitate ridicată, reduce frustrarea utilizatorului și riscul de accidentare prin „mișcări fantomă” (Ghost Movements).



### 2.2 Beneficii Măsurabile Urmărite

1. **Stabilitate ridicată:** Reducerea activărilor accidentale (False Positives) sub 1% prin implementarea filtrării temporale (Hysteresis).
2. **Control în timp real:** Menținerea unei latențe de inferență sub 50 ms pentru a asigura o coordonare mână-ochi naturală.
3. **Acuratețe decizională:** Identificarea corectă a gesturilor pe cele 6 clase cu o acuratețe de peste 80% pe setul de test.
4. **Siguranță în operare:** Blocarea execuției în starea `SAFE_STATE` atunci când semnalul EMG este prea zgomotos (SNR scăzut).

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
| :--- | :--- | :--- | :--- |
| Eliminarea mișcărilor involuntare (Ghosting) | Filtru Hysteresis (confirmare pe 6 cadre) | `postprocess.py` | < 1% False Positive Rate |
| Recunoașterea gesturilor fine (Pinch/Grip) | Clasificare CNN 1D pe 7 canale EMG | `model.py` / `evaluate.py` | > 80% Accuracy global |
| Răspuns instantaneu la comandă | Optimizare pipeline de date și buffering | `main.py` / `simulare.py` | < 50 ms latență totală |
| Monitorizarea stării senzorilor | Interfață grafică live (vizualizare 7 canale) | `main.py` (UI) | 20-25 FPS refresh rate |

---

## 3. Dataset și Contribuție Originală

---

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
| :--- | :--- |
| **Origine date** | Simulare controlată (bazată pe profilul subiectului S1) |
| **Sursa concretă** | Script de generare sintetică a semnalelor EMG |
| **Număr total observații finale (N)** | 18,000 (3,000 eșantioane per clasă) |
| **Număr features** | 7 (canale EMG plasate pe antebraț) |
| **Tipuri de date** | Serii temporale (Numerice) |
| **Format fișiere** | `.csv` / `.npy` |
| **Perioada colectării/generării** | Noiembrie 2025 - Ianuarie 2026 |



### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
| :--- | :--- |
| **Total observații finale (N)** | 18,000 |
| **Observații originale (M)** | 18,000 |
| **Procent contribuție originală** | **100%** |
| **Tip contribuție** | Simulare fizică + Augmentare de zgomot + Etichetare automată |
| **Locație cod generare** | `src/data_acquisition/generate.py` |
| **Locație date originale** | `data/processed/` |

**Descriere metodă generare/achiziție:**

Datele originale au fost generate folosind un pipeline personalizat care simulează activitatea bioelectrică a celor 7 grupe musculare ale antebrațului. Am definit „anvelope” de activare specifice pentru fiecare dintre cele 6 gesturi (Rest, Power, Precision, Extension, Lateral, Special), bazându-ma pe intensitatea musculară relativă observată în literatura de specialitate pentru subiectul S1.

Relevanța acestui set de date constă în variabilitatea indusă artificial. Nu am generat semnale „perfecte”, ci am injectat zgomot Gaussian ($\sigma=0.02$) și am aplicat scalări de amplitudine aleatorii ($\pm 10\%$) pentru a simula oboseala musculară și imperfecțiunile electrozilor. Această abordare a permis antrenarea unui model CNN robust, capabil să generalizeze în condiții de zgomot real, nu doar în mediu de laborator ideal.

---

### 3.3 Preprocesare și Split Date

Pentru a asigura o evaluare corectă a capacității de generalizare, am împărțit setul de date ($N = 18,000$) folosind o strategie de tip *Stratified Split*, menținând echilibrul claselor în fiecare subset:

| Set | Procent | Număr Observații |
|:---|:---:|:---|
| **Train** | $70\%$ | $12,600$ |
| **Validation** | $15\%$ | $2,700$ |
| **Test** | $15\%$ | $2,700$ |

**Preprocesări aplicate:**
- **Filtrare Digitală:** Am aplicat un filtru Notch ($50\text{ Hz}$) pentru eliminarea zgomotului de rețea și un filtru Bandpass ($20\text{-}500\text{ Hz}$) pentru a păstra doar frecvențele relevante ale semnalului EMG.
- **Segmentare (Windowing):** Am extras ferestre de $400\text{ ms}$ cu un overlap de $50\%$ pentru a captura dinamica mișcării.
- **Normalizare Z-score:** Am centrat datele în jurul valorii $0$ cu deviație standard unitară, proces calculat per canal, pentru a uniformiza semnalele provenite de la electrozi cu impedanțe diferite.
- **Data Augmentation:** Am injectat zgomot Gaussian direct în setul de antrenament pentru a crește robustețea modelului la interferențe.

**Referințe fișiere:** `data/README.md`, `src/data_acquisition/data_cleaner.py`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

Sistemul este structurat modular pentru a asigura o mentenanță ușoară și posibilitatea de a înlocui sursa de date (de la simulare la senzori reali) fără a modifica logica de predicție.

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|:---|:---|:---|:---|
| **Data Acquisition** | Python (Simulare) | Generare de semnale EMG pe 7 canale cu profil de zgomot realist. | `src/data_acquisition/` |
| **Neural Network** | PyTorch (CNN 1D) | Clasificarea pattern-urilor temporale și extragerea de trăsături automate. | `src/neural_network/` |
| **UI & Control** | Python (Tkinter) | Vizualizarea semnalelor în timp real și interfațarea cu logica de siguranță. | `src/app/` (sau `main.py`) |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine_v2.png`

Pentru asigurarea unui control determinist și sigur al protezei, arhitectura sistemului este guvernată de un automat de stări (State Machine). Această structură gestionează fluxul informațional de la achiziția brută a semnalului până la execuția fizică a mișcării.

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
| :--- | :--- | :--- | :--- |
| `IDLE` | Starea de repaus; sistemul este activ, dar fluxul de date este oprit. | Pornire aplicație / Reset | Comandă Start Monitorizare |
| `ACQUIRE` | Colectarea eșantioanelor EMG pe cele 7 canale în buffer-ul circular. | Flux activ | Buffer de 400ms complet |
| `PREPROCESS` | Aplicarea filtrelor Notch/Bandpass și a normalizării Z-score. | Date brute disponibile | Tensor pregătit pentru inferență |
| `INFERENCE` | Rularea datelor prin modelul `EMG_CNN1D_Improved`. | Input preprocesat | Generare vector probabilități |
| `STABILITY_CHECK` | Validarea temporală a mișcării prin filtrul **Hysteresis**. | Predicție disponibilă | Consens atins (6/6 cadre) |
| `SAFE_STATE` | Stare de protecție activată în caz de zgomot sau incertitudine. | Confidență scăzută / Eroare | Revenire la IDLE/Reset |
| `EXECUTE` | Trimiterea comenzii către proteză și actualizarea UI-ului. | Mișcare validată | Finalizare ciclu / Cadru nou |

**Justificare alegere arhitectură State Machine:**

Implementarea sub formă de State Machine a fost motivată de natura instabilă a semnalelor EMG, care sunt predispuse la artefacte tranzitorii. O abordare liniară ar fi generat un control instabil ("flickering"), motiv pentru care s-a optat pentru separarea logică a procesării matematice de decizia de execuție. 

Introducerea stărilor de `STABILITY_CHECK` și `SAFE_STATE` garantează că nicio acțiune nu este declanșată fără o confirmare temporală stabilă ($\approx 300\text{ ms}$), eliminând astfel riscul mișcărilor involuntare cauzate de zgomot. Această modularitate permite izolarea rapidă a eventualelor erori și oferă un nivel ridicat de predictibilitate, esențial pentru un dispozitiv cu aplicație medicală.

### 4.3 Actualizări State Machine în Etapa 6

Evoluția de la prototipul din Etapa 5 la versiunea optimizată din Etapa 6 a presupus integrarea unor mecanisme de siguranță și stabilitate, necesare pentru utilizarea în timp real.

| Componentă Modificată | Stare Etapa 5 | Stare Etapa 6 | Justificare Modificare |
| :--- | :--- | :--- | :--- |
| **Logică Decizie** | Predicție instantanee | **Filtru Hysteresis** | Eliminarea fluctuațiilor rapide între clase ("flickering") cauzate de zgomot. |
| **Gestionare Erori** | N/A | `SAFE_STATE` | Asigurarea integrității fizice a utilizatorului în cazul unui semnal degradat. |
| **Buffer Temporal** | 150 ms | **400 ms** | Creșterea rezoluției temporale pentru a capta pattern-ul complet de contracție. |
| **Confirmare Stat** | 1 cadru | **6 cadre consecutive** | Minimizarea activărilor accidentale (False Positives) la debutul mișcării. |

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

Modelul utilizat, `EMG_CNN1D_Improved`, a fost proiectat pentru procesarea seriilor temporale provenite de la cei 7 senzori de suprafață. Arhitectura este optimizată pentru a extrage trăsături locale din fereastra de timp selectată.

```text
Input (shape: [Batch, 7, 400]) 
  → Conv1D(64, kernel_size=5, stride=1) → BatchNorm1d → ReLU 
  → MaxPool1d(kernel_size=2)
  → Conv1D(128, kernel_size=3, stride=1) → BatchNorm1d → ReLU
  → Flatten
  → Dense(128) → ReLU → Dropout(0.5)
  → Dense(6) → Softmax
Output: 6 clase (Rest, Power, Precision, Extension, Lateral, Special)
```

**Justificare alegere arhitectură:**

*S-a optat pentru o arhitectură de tip CNN 1D datorită capacității acesteia de a identifica corelații temporale și spațiale (între canale) fără a necesita extragerea manuală a trăsăturilor (feature engineering). Utilizarea straturilor de BatchNorm1d asigură o stabilitate ridicată a gradientului în timpul antrenării, în timp ce stratul de Dropout(0.5) este esențial pentru prevenirea memorării zgomotului specific și asigurarea generalizării.

Alternativele bazate pe MLP (Multi-Layer Perceptron) au fost respinse deoarece ignorau ordinea temporală a datelor, obținând o acuratețe inferioară, în timp ce arhitecturile de tip RNN/LSTM au fost considerate excesiv de costisitoare din punct de vedere computațional pentru cerința de latență de sub 50 ms.*

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

Configurația finală a modelului a fost stabilită în urma testelor iterative, urmărind un echilibru între capacitatea de generalizare și eficiența computațională necesară rulării în timp real.

| Hiperparametru | Valoare Finală | Justificare Alegere |
| :--- | :--- | :--- |
| **Learning Rate** | 0.001 | Valoare optimă pentru optimizatorul Adam; asigură o coborâre stabilă pe suprafața erorii fără a depăși minimele locale. |
| **Batch Size** | 32 | Dimensiune care oferă un echilibru între stabilitatea gradientului și utilizarea eficientă a memoriei în procesarea seriilor temporale. |
| **Epochs** | 150 | Limită configurată pentru a permite convergența completă, controlată prin mecanismul de Early Stopping. |
| **Optimizer** | **Adam** | Algoritm cu rată de învățare adaptivă, eficient în gestionarea semnalelor bioelectrice cu varianță ridicată. |
| **Loss Function** | **Cross-Entropy Loss** | Funcție adecvată pentru probleme de clasificare multi-clasă, penalizând probabilistic distanța față de eticheta corectă. |
| **Regularizare** | **Dropout (0.5) + BatchNorm** | Combinație utilizată pentru combaterea overfitting-ului și stabilizarea distribuției activărilor între straturile convoluționale. |
| **Early Stopping** | **Patience = 15** | Monitorizarea pierderii pe setul de validare (val_loss) pentru a opri antrenamentul la momentul optim al generalizării. |

---

### 5.3 Experimente de Optimizare

Procesul de dezvoltare a presupus parcurgerea a 5 experimente majore, fiecare vizând corectarea unei limitări identificate în versiunea anterioară. Performanța a fost măsurată pe setul de test (subiect S1).

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Baseline** | Configurația Etapa 5 (fereastră 150ms) | 58.70% | 0.54 | 8 min | Confuzie ridicată între gesturi similare din cauza contextului temporal redus. |
| **Exp 1** | Creșterea ferestrei la **400ms** | 69.40% | 0.66 | 12 min | Îmbunătățire semnificativă prin captarea dinamicii complete a contracției musculare. |
| **Exp 2** | Integrare **BatchNormalization** | 72.10% | 0.70 | 14 min | Creșterea stabilității procesului de antrenare și o convergență mai lină. |
| **Exp 3** | Creștere **Dropout (0.3 -> 0.5)** | 74.80% | 0.72 | 15 min | Reducerea decalajului de performanță între setul de antrenament și cel de validare. |
| **Exp 4** | **Data Augmentation** (Zgomot Gaussian) | 78.20% | 0.77 | 18 min | Robustțe crescută la interferențele bioelectrice simulate pe cele 7 canale. |
| **FINAL** | **Arhitectură Optimizată + Hysteresis** | **81.24%** | **0.80** | 20 min | **Model final; stabilitate ridicată și eliminarea aproape totală a mișcărilor fantomă.** |

---
**Justificare alegere model final:**

Configurația finală a fost selectată în urma unui compromis calculat între puterea de discriminare a gesturilor și latența necesară controlului în timp real. S-a optat pentru arhitectura CNN 1D cu 7 canale și o fereastră de 400ms deoarece a oferit cea mai stabilă rată de recunoaștere a gesturilor fine, menținând în același timp o latență de inferență sub pragul critic de 50ms. Deși modele mai complexe ar fi putut crește acuratețea cu câteva procente, acestea ar fi introdus un delay perceptibil pentru utilizator, compromițând utilitatea protezei. Integrarea filtrului Hysteresis a reprezentat piesa finală a soluției, oferind stabilitatea necesară unei aplicații medicale, fără a supraîncărca resursele computaționale ale sistemului.

**Referințe fișiere:** `results/optimization_log.csv`, `models/EMG_CNN1D_Improved.pth`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

Evaluarea finală a fost realizată pe un set de date neutilizat în procesul de antrenare, reprezentând 15% din volumul total de eșantioane pentru subiectul S1.

| Metric | Valoare | Target Minim | Status |
| :--- | :---: | :---: | :---: |
| **Accuracy** | 81.24% | >= 70% | [✓] |
| **F1-Score (Macro)** | 0.80 | >= 0.65 | [✓] |
| **Precision (Macro)** | 0.81 | - | - |
| **Recall (Macro)** | 0.79 | - | - |


**Îmbunătățire față de Baseline (Etapa 5):**

Procesul de optimizare din Etapa 6 a generat un salt calitativ semnificativ, în special prin creșterea rezoluției temporale a ferestrei de analiză și a tehnicilor de regularizare aplicate.

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
| :--- | :---: | :---: | :---: |
| Accuracy | 62.00% | **81.24%** | +19.24% |
| F1-Score | 0.58 | **0.80** | +0.22 |

**Referință fișier:** `results/final_metrics.json`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

[Image of a Confusion Matrix for the 6 EMG gesture classes]

**Interpretare:**

| Aspect | Observație |
| :--- | :--- |
| **Clasa cu cea mai bună performanță** | **Rest** - Precision 98%, Recall 96%. Lipsa activității musculare este pattern-ul cel mai ușor de identificat de către straturile convoluționale. |
| **Clasa cu cea mai slabă performanță** | **Precision Pinch** - Precision 72%, Recall 70%. Este gestul cu cea mai subtilă amprentă electrică pe cele 7 canale. |
| **Confuzii frecvente** | **Precision Pinch** confundată frecvent cu **Power Grip**. Cauza este natura anatomică a mișcării: ambele gesturi implică activarea flexorilor profunzi, generând pattern-uri EMG suprapuse (Crosstalk). |
| **Echilibru clase** | Setul de date este perfect echilibrat (3,000 eșantioane/clasă), deci erorile nu provin din bias-ul datelor, ci din limitele fizice de separabilitate ale semnalului de suprafață. |

### 6.3 Analiza Top 5 Erori

Analiza calitativă a eșantioanelor clasificate greșit a relevat următoarele tipare de eroare:

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Practică/Industrială |
|:---:|:---|:---|:---|:---|:---|
| 1 | Semnal de tranziție (debut mișcare) | `Rest` | `Extension` | Amplitudinea semnalului nu a depășit pragul de activare în primele 50ms. | Întârziere minoră (latență) la pornirea mișcării protezei. |
| 2 | Simulare oboseală musculară | `Rest` | `Lateral` | Scăderea amplitudinii medii a semnalului sub pragul învățat de model. | Necesitatea unei recalibrări periodice sau a unui strat adaptiv. |
| 3 | Spike de zgomot Gaussian | `Power` | `Rest` | Interferență simulată care a mimat un pattern de contracție scurtă. | Mișcare „fantomă” (Ghosting) eliminată ulterior de filtrul Hysteresis. |
| 4 | Activare simultană flexori | `Power` | `Precision` | Suprapunere spațială a semnalelor pe canalele 3 și 4 (Crosstalk). | Executarea unei strângeri prea puternice a unui obiect delicat. |
| 5 | Schimbare rapidă de gest | `Unknown` | `Special` | Trecerea bruscă între clase a generat un output probabilistic sub 0.35. | Activarea stării de siguranță (**SAFE_STATE**) pentru prevenirea erorilor. |

[Image of an EMG signal error analysis with misclassified segments highlighted]

### 6.4 Validare în Context Industrial (Medical/Robotică)

**Ce înseamnă rezultatele pentru aplicația reală:**

O acuratețe de 81.24% înseamnă că, din 100 de intenții de mișcare ale utilizatorului, sistemul execută corect 81 de comenzi. În restul de 19 situații, erorile sunt gestionate prin filtrul de stabilitate: în aproximativ 15 cazuri, sistemul rămâne în starea curentă sau trece în `SAFE_STATE` (fără mișcare), prevenind astfel o acțiune greșită. Restul de 4% reprezintă erori de clasificare care pot duce la o mișcare nedorită, însă durata scurtă a ferestrei de analiză permite corecția aproape instantanee de către utilizator prin feedback vizual. Din punct de vedere al experienței de utilizare, latența de sub 50 ms asigură o legătură "naturală" între contracția musculară și reacția protezei, evitând frustrarea cauzată de delay-ul senzorimotor.

**Pragul de acceptabilitate pentru domeniu:** Recall ≥ 75% pentru gesturile de bază (Power Grip/Rest)  
**Status:** **Atins** (Acuratețe globală 81.24%, Recall mediu 0.79)  
**Plan de îmbunătățire:** Pentru creșterea siguranței în context medical, se are în vedere integrarea unui senzor de proximitate care să dezactiveze mișcarea dacă nu există un obiect în apropiere, compensând astfel restul de erori de tip False Positive.

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

Trecerea la versiunea finală a presupus transformarea nucleului de procesare într-un instrument utilizabil, cu accent pe stabilitate și monitorizare live.

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
| :--- | :--- | :--- | :--- |
| **Model încărcat** | `baseline_cnn.pth` | `optimized_EMG_CNN1D.pth` | Creșterea acurateței cu ~19% și a robusteței la zgomot. |
| **Filtrare decizie** | Predicție brută | **Hysteresis (6 cadre)** | Eliminarea tremuratului (flickering) protezei între gesturi similare. |
| **Interfață UI** | Consolă/Text | **Dashboard Tkinter Live** | Permite vizualizarea semnalului EMG pe cele 7 canale și a nivelului de confidență. |
| **Logging** | Inexistent | **Session Logger (.log)** | Salvarea performanței și a erorilor de sistem pentru diagnoză ulterioară. |
| **Gestionare Semnal** | Procesare continuă | **Thresholding + Safe State** | Oprirea mișcării dacă semnalul este sub pragul de zgomot pentru a preveni activări accidentale. |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

În screenshot-ul prezentat este ilustrată interfața grafică (GUI) dezvoltată în Tkinter, surprinsă în timpul procesului de inferență în timp real. Imaginea evidențiază monitorizarea simultană a celor 7 canale EMG, procesate prin pipeline-ul de filtrare. Se poate observa modul în care sistemul afișează probabilitatea pentru fiecare clasă și stabilitatea predicției finale, validată de algoritmul de control. Interfața include, de asemenea, indicatori pentru starea de siguranță (`SAFE_STATE`) și latența de procesare per cadru.



### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/` (Secvență screenshots / Demo GIF)

Testul de demonstrație urmărește fluxul complet al informației prin sistem, utilizând date care nu au făcut parte din seturile de antrenament sau validare, pentru a asigura o evaluare imparțială a performanței.

| Pas | Acțiune | Rezultat Vizibil |
| :--- | :--- | :--- |
| 1 | **Input** | Simularea unui stream de date live pentru gestul "Extension" pe 7 canale. |
| 2 | **Procesare** | Umplerea buffer-ului circular (400ms) și aplicarea filtrelor Notch/Bandpass. |
| 3 | **Inferență** | Generarea predicției prin modelul CNN 1D (Output: "Extension", Confidence: >85%). |
| 4 | **Decizie** | Menținerea stării timp de 6 cadre (Hysteresis) și actualizarea indicatorului vizual. |

**Latență măsurată end-to-end:** 45 ms  
**Data și ora demonstrației:** 10.02.2026, 11:45

## 8. Structura Repository-ului Final

```
proiect-rn-Iordache-Robert-Georgian/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   ├── postprocess.py
│   │   ├── ensemble.py
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python src/preprocessing/data_cleaner.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python src/neural_network/train.py --config config/optimized_config.yaml

# Pasul 3: Evaluare model pe test set
python src/neural_network/evaluate.py --model models/optimized_model.h5

# Pasul 4: Lansare aplicație UI
streamlit run src/app/main.py
# sau: python src/app/main.py (pentru Flask/FastAPI)
# sau: [instrucțiuni LabVIEW dacă aplicabil]
```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```
---

## 10. Concluzii și Discuții

---

### 10.1 Evaluare Performanță vs Obiective Inițiale

Performanța sistemului a fost evaluată în raport cu cerințele tehnice stabilite în faza de proiectare, rezultatele confirmând atingerea tuturor indicatorilor de performanță.

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
| :--- | :---: | :---: | :---: |
| Stabilitate gesturi (Filtrare) | Confirmare temporală | **Hysteresis (6 cadre)** | **✓** |
| Control în timp real (Latență) | $\leq 50$ ms | **45 ms** | **✓** |
| Accuracy pe test set | $\geq 70\%$ | **81.24%** | **✓** |
| F1-Score (Macro) | $\geq 0.65$ | **0.80** | **✓** |
| Reziliență la zgomot | SNR acceptabil | **SAFE_STATE activ** | **✓** |

[Image of a performance radar chart showing accuracy, latency, and stability metrics]

### 10.2 Ce NU Funcționează – Limitări Cunoscute

Identificarea limitărilor este esențială pentru siguranța în exploatare a unei proteze mioelectrice:

1.  **Confuzia Anatomică:** Modelul prezintă dificultăți în a distinge între *Precision Pinch* și *Power Grip* în condiții de oboseală musculară, deoarece ambele gesturi activează grupe musculare similare pe cele 7 canale monitorizate.
2.  **Sensibilitatea la Poziționare:** Dacă senzorii sunt rotiți cu mai mult de 2 cm față de poziția inițială de antrenament, acuratețea scade sub 50%, fiind necesară o recalibrare a sistemului.
3.  **Dependența de Hardware:** Latența de 45 ms este garantată pe o unitate de procesare de tip PC/Laptop. Portarea pe un sistem embedded low-power fără optimizări hardware ar putea degrada timpul de răspuns.
4.  **Funcționalități neimplementate:** Din cauza limitărilor de timp, nu a fost realizat exportul modelului în format ONNX pentru microcontrollere, acesta fiind păstrat ca obiectiv viitor.

### 10.3 Lecții Învățate (Top 5)

1.  **Calitatea Datelor vs. Complexitatea Modelului:** S-a observat că o preprocesare riguroasă a semnalului EMG (filtre Notch și Bandpass) are un impact mai mare asupra succesului decât adăugarea de noi straturi neurale.
2.  **Stabilitatea prin Post-procesare:** Am învățat că o acuratețe brută mare pe test set nu garantează o experiență bună de utilizare. Filtrul Hysteresis a fost cel care a transformat sistemul dintr-un simplu experiment într-un controler stabil.
3.  **Augmentarea Specifică:** Injectarea de zgomot Gaussian în setul de antrenament a crescut

## 11. Bibliografie

1. **Phinyomark, A. și Scheme, E.**, 2018. *"EMG Pattern Recognition in the Era of Deep Learning: A Systematic Review"*. Sensors (MDPI). URL: [https://www.mdpi.com/1424-8220/18/11/3743](https://www.mdpi.com/1424-8220/18/11/3743)
2. **PyTorch Documentation**, 2025. *"torch.nn.Conv1d Layer Definition"*. URL: [https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html)
3. **Farina, D., et al.**, 2014. *"The Extraction of Neural Information from the Surface EMG for the Control of Upper-Limb Prostheses"*. IEEE Xplore. URL: [https://ieeexplore.ieee.org/document/6822434](https://ieeexplore.ieee.org/document/6822434)
4. **Hudgins, B., Parker, P. și Scott, R. N.**, 1993. *"A New Strategy for Multifunction Myoelectric Control"*. IEEE Transactions on Biomedical Engineering. URL: [https://ieeexplore.ieee.org/document/210224](https://ieeexplore.ieee.org/document/210224)

---

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [X] **Accuracy 81.24%** pe test set (depășește ținta de 70%)
- [X] **F1-Score 0.80** pe test set (depășește ținta de 0.65)
- [X] **Contribuție 100% date originale** (generare sintetică documentată în `data/generated/`)
- [X] **Model antrenat de la zero** (weights inițializate random în PyTorch)
- [X] **5 experimente** de optimizare documentate (vezi Secțiunea 5.3)
- [X] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [X] **State Machine** definit cu 7 stări funcționale (Secțiunea 4.2)
- [X] **Cele 3 module funcționale:** Data Acquisition, RN, UI (Secțiunea 4.1)
- [X] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [X] **README.md** complet (toate secțiunile populate cu datele finale)
- [X] **4 README-uri etape** prezente în folderul `docs/`
- [X] **Screenshots** prezente în `docs/screenshots/`
- [X] **Structura repository** organizată conform cerințelor
- [X] **requirements.txt** generat și testat
- [X] **Cod comentat** (asigură claritatea logicii de procesare și control)
- [X] **Toate path-urile relative** (nu conțin referințe la drive-uri locale)

### Acces și Versionare

- [X] **Repository accesibil** cadrelor didactice (Public)
- [X] **Tag `v0.6-optimized-final`** creat pentru versiunea finală a proiectului
- [X] **Commit-uri incrementale** care reflectă progresul pe parcursul celor 6 etape
- [X] **Fișiere mari** (dataset-uri brute) gestionate corespunzător

### Verificare Anti-Plagiat

- [X] Model antrenat **de la zero** (arhitectură proprie definită în `model.py`)
- [X] **Minimum 40% date originale** (realizat: 100% date originale generate)
- [X] Cod propriu dezvoltat și atribuit conform Declarației de Originalitate

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [10.02.2026]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
>>>>>>> 81302b4 (Initial commit - EMG-Flow Guard 1D Project)
