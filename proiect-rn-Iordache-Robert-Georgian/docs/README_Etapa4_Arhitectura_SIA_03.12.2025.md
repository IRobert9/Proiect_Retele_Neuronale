# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Iordache Robert Georgian  
**Link Repository GitHub**
**Data:** [Data]  
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
| :--- | :--- | :--- |
| Control mioelectric stabil pentru proteze de mână în timp real | Clasificare semnale EMG cu **6 clase fundamentale** $\rightarrow$ predicție stabilă cu latență de **50ms** și acuratețe de **$81.24\%$** pe subiectul S1. | `EMG_CNN1D_Improved` + `main.py` |
| Eliminarea „tremuratului” (flicker) la tranziția între gesturi | Implementare algoritm de post-procesare **Hysteresis** (prag de confirmare de **6 cadre**) pentru a preveni activările accidentale. | `EMGPostProcessor` |
| Analiza precisă a activării musculare profunde | Procesare simultană pe **7 canale EMG** cu ferestre fixe de **400 samples (400ms)** la 1000Hz pentru captarea semnăturii spectrale a gestului. | `Temporal Windowing` + `data_splitter.py` |

---

### 2. Contribuția Voastră Originală la Setul de Date – Etapa 3 + Etapa 4

### Contribuția originală la setul de date:

**Total observații finale:** $\approx 230,000$ ferestre EMG (după segmentare și augmentare)  
**Observații originale:** $\approx 95,000$ ferestre (**$41.3\%$**)

**Tipul contribuției:**
[X] Date generate prin simulare fizică (Augmentări calibrate)  
[ ] Date achiziționate cu senzori proprii  
[X] Etichetare/adnotare manuală (Grupare funcțională în 6 clase)  
[X] Date sintetice prin metode avansate (Augmentare semnal)

**Descriere detaliată:**

**1. Simulare realistă semnale EMG (Augmentare):**
Am dezvoltat un pipeline de generare date sintetice pentru a crește robustețea modelului la variabilitatea naturală a semnalelor bioelectrice:
* **Zgomot Gaussian calibrat (SNR 2%)**: Implementat pentru a simula interferența electronică a senzorilor reali și zgomotul de fond muscular.
* **Variabilitatea amplitudinii ($\pm 10\%$)**: Modelează schimbările forței de contracție și oboseala musculară pe parcursul sesiunii.
* **Resantionare la 1000Hz**: Asigură conformitatea datelor cu cerințele de latență scăzută pentru aplicațiile real-time.

**2. Strategie de Split Temporal și Validare:**
Pentru a evita fenomenul de *data leakage* și a simula utilizarea reală, am implementat un sistem de split bazat pe repetiții (Interleaved Split):
* **Set Antrenament**: Repetițiile **1, 2, 4 și 6**.
* **Set Validare**: Repetițiile **3 și 5**.
* **Set Test (Hold-out)**: Subiectul **S1** (complet exclus din antrenament) pentru a măsura performanța reală de inferență.

**Locația codului:**
* `src/data_acquisition/generate.py`: Logica de augmentare și modelare fizică a zgomotului.
* `src/preprocessing/data_splitter.py`: Implementarea segmentării și a logicii de split pe repetiții.

**Dovezi Rezultate Măsurabile:**
* **Îmbunătățire Performanță**: Utilizarea datelor augmentate și a filtrării Hysteresis a ridicat acuratețea de la un baseline de $\approx 58\%$ la **$81.24\%$**.
* **Latență Control**: Sistemul realizează procesarea completă și actualizarea UI în sub **50ms**.
* **Stabilitate**: Reducerea erorilor de tranziție prin necesitatea a 6 predicții consecutive identice pentru validarea gestului.

**Descriere detaliată:**

**1. Simulare realistă semnale EMG (Augmentare date):**
Am implementat un generator de semnale EMG sintetice bazat pe modelarea fizică a activității musculare pentru a crește robustețea modelului. Metodologia include:
- **Zgomot Gaussian calibrat (SNR 2%)**: Simulează interferența electrică și variabilitatea naturală a semnalelor bioelectrice, parametrii fiind calibrați pentru a replica condițiile de achiziție reală.
- **Variabilitatea amplitudinii (±10%)**: Modelează oboseala musculară și schimbările de forță de contracție în timp real, asigurând generalizarea rețelei pe parcursul întregii sesiuni de utilizare.
- **Frecvență de eșantionare 1000Hz**: Datele sunt procesate la 1000Hz pentru a asigura un echilibru optim între rezoluția spectrală și latența de calcul.

**2. Split temporal și strategie de validare:**
- **Interleaved Split**: Implementarea unei strategii de împărțire pe repetiții pentru a evita *data leakage* și a simula utilizarea cronologică reală.
- **Antrenare (Train)**: Repetițiile **1, 2, 4 și 6** (acoperă dinamica musculară de la începutul și finalul exercițiilor).
- **Validare (Val)**: Repetițiile **3 și 5** (utilizate pentru monitorizarea performanței în timpul antrenamentului).
- **Testare (Hold-out)**: Subiectul **S1** este utilizat exclusiv pentru validarea finală, asigurând că modelul este evaluat pe date complet noi.

**3. Optimizări pentru aplicații real-time:**
Toate datele generate și procesate respectă constrângerile temporale ale unei proteze mioelectrice:
- **Window size**: **400 samples (400ms)** pentru a oferi modelului suficientă informație pentru o clasificare precisă.
- **Latență sistem**: Arhitectura permite o latență de inferență și actualizare UI de **< 50ms**.
- **Normalizare per-window**: Adaptare dinamică la variabilitatea semnalului folosind parametrii Z-Score stocați în `config/preprocessing_params.pkl`.

**Locația codului:** - `src/data_acquisition/generate.py` (Logica de augmentare și generare date sintetice).
- `src/preprocessing/data_splitter.py` (Funcția de segmentare și split pe repetiții).

**Locația datelor:** - **Dataset original**: NinaPro DB2 (Sursă .mat).
- **Date procesate**: `data/train/`, `data/validation/` și `data/test/` (formate `.pt` PyTorch).
- **Parametri configurare**: `config/optimized_config.yaml` și `config/preprocessing_params.pkl`.

**Dovezi:**

**1. Statistici comparative date reale vs sintetice:**
```text
Dataset final: ~230,000 ferestre
├─ Date reale NinaPro DB2:    ~135,000 ferestre (58.7%)
└─ Date sintetice (zgomot/augmentare): ~95,000 ferestre (41.3%)
Total contribuție originală: 41.3% (Simulare fizică + Augmentare variabilitate)
```

**2. Validare efectivitate augmentare:**
- **Baseline accuracy (fără augmentare):** ~58.74%
- **Cu augmentare și post-procesare:** 81.24% test accuracy pe subiectul S40
- **Stabilitate decizională:** Creștere a fiabilității prin filtrarea Hysteresis (prag 6)

**3. Parametri calibrați științific:**
- Zgomot Gaussian: μ=0, σ=0.02 (bazat pe caracteristicile SNR ale sistemelor EMG clinice)
- Scalare amplitude: [0.90, 1.10] (simulează variabilitatea forței de contracție ±10%)
- Fereastră temporală: 400ms (echilibru optim între rezoluția datelor și timpul de reacție)

**4. Rezultate măsurabile:**
```
Îmbunătățiri cu pipeline-ul optimizat:
├─ Test accuracy (S40): 81.24% (+22.5% față de baseline)
├─ Stabilitate temporală: Reducere erori de tranziție prin confirmare la 6 cadre
├─ Timp real: < 50ms latență pentru predicție și update UI
└─ Eficiență senzori: Analiză simultană pe 7 canale EMG
```

Această abordare demonstrează că augmentarea nu este doar o multiplicare artificială a datelor, ci o simulare fizic validă a variabilității reale a semnalelor EMG în aplicații de control proteze, cu parametri științifici justificați și validare pe metrici obiective.

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Locație fișier:** `docs/state_machine.png`

![Diagrama State Machine](docs/state_machine.png)

### Justificarea State Machine-ului ales:

Am ales o arhitectură de tip **Procesare Continuă în Timp Real (Streaming)** deoarece o proteză trebuie să răspundă instantaneu la comenzile utilizatorului. Arhitectura separă clar achiziția datelor de inferența neuronală pentru a preveni blocarea fluxului de execuție și pentru a asigura o latență de procesare sub **50ms**.

**Stările principale sunt:**
1.  **ACQUIRE_EMG:** Simularea achiziției de la cei **7 senzori** care alimentează un buffer de **400 samples** (corespunzător ferestrei de analiză de **400ms**).
2.  **RN_INFERENCE:** Pasul critic unde rețeaua neuronală **CNN 1D Improved** clasifică intenția de mișcare pe baza tensorilor normalizați Z-Score.
3.  **CLASSIFY_MOTION (Decision Logic):** Implementarea filtrului de stabilitate **Hysteresis**. Decizia nu este transmisă protezei decât după confirmarea aceleiași clase pe parcursul a **6 cadre consecutive**, eliminând astfel activările accidentale.

**Tranzițiile critice sunt:**
-   **[ACQUIRE_EMG] → [PREPROCESS]:** Se declanșează automat la fiecare ciclu de ceas al simulării (50ms) pentru a prelua cele mai recente date din buffer-ul circular.
-   **[CLASSIFY_MOTION] → [SAFE_STATE]:** Dacă sistemul detectează o clasă incertă sau dacă buffer-ul de Hysteresis nu este plin, proteza rămâne în starea de repaus (**Rest**), prevenind mișcările haotice.

**Starea ERROR_HANDLER:**
Aceasta asigură robustețea sistemului (Fail-Safe). În contextul unei proteze reale, erorile de procesare sau zgomotul excesiv nu blochează aplicația, ci forțează sistemul într-o stare de oprire controlată (`SAFE_STOP`), protejând utilizatorul de mișcări involuntare cauzate de semnale corupte.

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module sunt implementate în limbajul Python și sunt integrate în pachetul `src`, demonstrând o arhitectură modulară funcțională, decuplată și optimizată pentru procesare în timp real.

| **Modul** | **Implementare (Python)** | **Funcționalitate realizată (la predare)** |
|:---|:---|:---|
| **1. Data Logging / Acquisition** | `src/preprocessing/` & `src/data_acquisition/` | Gestionează încărcarea tensorilor PyTorch, rectificarea semnalului ($|EMG|$), ferestruirea la **400ms** (400 esantioane) și normalizarea Z-score bazată pe statistici pre-calculate. |
| **2. Neural Network Module** | `src/neural_network/model.py` | Definirea arhitecturii **CNN 1D Improved**, procesul de antrenare și optimizarea hiperparametrilor. Modelele sunt salvate în folderul `models/` în format **.pth** (PyTorch State Dict). |
| **3. UI / Simulation** | `src/app/main.py` (Interfață Grafică) | Interfață Desktop (Tkinter) care rulează simularea live pe subiectul S1, afișează simultan cele **7 canale EMG** și rulează inferența cu post-procesare **Hysteresis**. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [X] **Cod rulează fără erori:** Pipeline-ul de preprocesare este integrat și testat unitar.
- [X] **Format compatibil:** Ieșirea este sub formă de matrici NumPy (`.npy`) gata de antrenare, salvate în `data/train` și `data/test`.
- [X] **Pregătire pentru Augmentare:** Structura de cod permite generarea de date sintetice în versiunile viitoare (V2.0).
- [X] **Documentație în cod:** Docstring-uri clare în clasele `EMGPipeline` și `DataGenerator`.

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] **Arhitectură definită:** Model CNN 1D (Conv1D + Dropout + Dense) compilat fără erori.
- [X] **Persistență:** Modelul poate fi salvat și reîncărcat (`models/trained_model.h5`).
- [X] **Justificare arhitectură:** CNN 1D este ideal pentru serii de timp EMG datorită invarianței la translație temporală și eficienței computaționale față de RNN-uri.
- [X] **Stare antrenament:** Include modelul antrenat (`trained`) și cel optimizat (`optimized`).

#### **Modul 3: User Interface (UI)**

**Funcționalități MINIME obligatorii:**
- [X] **Input de la user:** Butoane funcționale pentru "Încărcare Simulare" și "Start/Stop".
- [X] **Vizualizare:** Afișează semnalul brut (simulat) și clasa predicționată în timp real cu bare de încredere.
- [X] **Demonstrație:** Screenshot inclus în `docs/interface_screenshot.png`.

**Scop:** Demonstrație că pipeline-ul end-to-end funcționează: input simulare → preprocess → model CNN → afișare rezultat pe ecran.
## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
proiect-rn-[nume-prenume]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [x] Tabelul Nevoie → Soluție → Modul complet (completat în README principal)
- [x] Declarație contribuție 40% date originale (acoperită prin procesul de augmentare/simulare)
- [x] Cod generare/achiziție date funcțional și documentat (`src/preprocessing/`)
- [x] Dovezi contribuție originală: grafice + log + statistici în `docs/` sau `results/`
- [x] Diagrama State Machine creată și salvată în `docs/state_machine.png`
- [x] Legendă State Machine scrisă în README (justificarea arhitecturii Real-Time)
- [x] Repository structurat conform modelului (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [x] Cod rulează fără erori (`python src/preprocessing/pipeline.py` sau echivalent)
- [x] Produce/Structurează datele pentru dataset-ul final
- [x] Format compatibil: Ieșirea este `.npy` gata de antrenare (compatibil cu Etapa 3)
- [x] Documentație tehnică (în docstrings și README):
  - [x] Metodă de generare/achiziție explicată (Windowing, Filtrare)
  - [x] Parametri folosiți (Frecvență 2000Hz, Fereastră 150ms)
  - [x] Justificare relevanță date (Serii de timp pentru control proteză)
- [x] Fișiere în `data/` conform structurii

### Modul 2: Neural Network
- [x] Arhitectură RN definită și documentată în cod (`src/neural_network/model.py`) - versiunea CNN 1D
- [x] Detalii arhitectură curentă incluse în documentație

### Modul 3: Web Service / UI
- [x] Propunere Interfață ce pornește fără erori (`python -m app.main gui`)
- [x] Screenshot demonstrativ în `docs/interface_screenshot.png` (sau `ui_demo.png`)
- [x] Instrucțiuni lansare (comenzi exacte) incluse în README
---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`