# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Iordache Robert Georgian
**Data:** 06.12.2025  

---

## Introducere

Acest document descrie activitățile realizate în Etapa 3, concentrându-se pe procesarea semnalelor EMG din baza de date NinaPro DB2. Scopul a fost transformarea datelor brute (serii de timp) într-un format compatibil cu arhitectura Deep Learning (ResNet 1D), aplicând tehnici avansate de ferestruire, normalizare și augmentare sintetică pentru a asigura robustețea modelului.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── README_Etapa3.md       # <-- Acest fișier
├── docs/
│   └── datasets/          # Diagrame distribuție clase, grafice semnal brut vs filtrat
├── data/
│   ├── raw/               # Fișierele originale .mat (S1_E2_A1.mat ... S14_E2_A1.mat)
│   ├── processed/         # Datele ferestruite și normalizate (în memorie/binar)
│   ├── train/             # Setul de antrenare (inclusiv date augmentate)
│   ├── validation/        # Setul de validare (stratificat)
│   └── test/              # Setul de testare (stratificat)
├── src/
│   ├── preprocessing/     # Scripturi pentru Windowing și Normalizare Z-Score
│   ├── data_acquisition/  # Scriptul de generare date sintetice (Augmentare)
│   └── neural_network/    # Definiția modelului ResNet (pregătire pentru Etapa 4)
├── config/                # Parametri (window_size=150, step=20)
└── requirements.txt       # tensorflow, scipy, sklearn, numpy
```

---

## 2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** NinaPro DB2 (Non-Invasive Adaptive Prosthetics Database), standard academic pentru proteze mioelectrice.
* **Modul de achiziție:**
    * **Senzori reali:** Electrozi Delsys Trigno Wireless (frecvență eșantionare redusă la 1000 Hz pentru eficiența procesării).
    * **Generare programatică:** Augmentare prin zgomot Gaussian și scalare pentru creșterea robusteții modelului.
* **Condițiile colectării:** Datele provin de la subiecți sănătoși (Exercițiul 2), cu utilizarea subiectului **S1** ca set de testare independent (Hold-out).

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** Datele sunt segmentate în ferestre temporale de **400 ms**, rezultând seturi de date salvate sub formă de tensori.
* **Număr de caracteristici (features):** **7 canale EMG** (corespunzătoare celor 7 senzori utilizați în inferență).
* **Tipuri de date:** * **Numerice** (Serii de timp normalizate Z-score).
    * **Categoriale** (Etichete pentru cele 6 mișcări).
* **Format fișiere:** * `.mat` (Sursă originală).
    * `.pt` (Format procesat PyTorch, utilizat în antrenare și simulare).

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
| :--- | :--- | :--- | :--- | :--- |
| **emg_ch[1-7]** | numeric | μV (norm) | Semnal electric muscular (**7 electrozi**) normalizat. | ~ -3.0 ... +3.0 (după Z-score) |
| **stimulus** | categorial | - | Eticheta mișcării (Ground Truth). | 0–5 (pentru cele 6 clase) |
| **window_time** | temporal | ms | Durata unei ferestre de analiză fixă. | **400 ms** |
| **subject_id** | categorial | - | Identificatorul subiectului utilizat pentru validare. | S1 |

---

## 3. Analiza Exploratorie a Datelor (EDA)

### 3.1 Statistici descriptive aplicate

* **Distribuții:** Analiza histogramelor a relevat că mișcările de apucare (Power, Precision) au o densitate mai mare de eșantioane față de mișcările de extensie.
* **Semnal:** S-au calculat media ($\mu$) și deviația standard ($\sigma$) pentru fiecare canal în scopul normalizării necesare antrenării.

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă:** Nu s-au identificat valori nule (NaN), integritatea datelor fiind asigurată prin alinierea eșantioanelor la frecvența de 1000 Hz.
* **Zgomot:** Segmentele de repaus ("Rest") au fost procesate pentru eliminarea DC offset-ului, centrând semnalul pe axa zero.

### 3.3 Probleme identificate

* **Problemă:** Confuzie ridicată între mișcările fine la utilizarea setului original de 23 de clase.
* **Soluție:** Implementarea strategiei de **Grupare Funcțională** (reducere la **6 clase robuste**) pentru a asigura o performanță de **81.24%**.
* **Problemă:** Instabilitatea predicțiilor la tranziția între stări.
* **Soluție:** Integrarea algoritmului de post-procesare de tip **Hysteresis** cu un prag de stabilitate de **6 cadre**.
---

## 4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Filtrare:** Spre deosebire de setul brut, clasa "Rest" (stimulus=0) este păstrată ca stare neutră de control, fiind curățată de zgomotul electronic prin eliminarea DC offset-ului.
* **Corecție:** Trunchierea vectorilor și alinierea eșantioanelor la frecvența de 1000 Hz pentru a asigura sincronizarea perfectă între cele 7 canale.
* **Eliminare clase rare:** S-a renunțat la clasele anatomice cu reprezentare insuficientă în favoarea celor 6 clase robuste selectate pentru sistemul de control.

### 4.2 Transformarea caracteristicilor

* **Windowing (Ferestruire):** * **Tehnică:** Fereastră fixă (Static Window) pentru a minimiza latența în aplicația de simulare live.
    * **Dimensiune:** **400 samples** (corespunzătoare unei durate de **400 ms**), oferind un echilibru între rezoluția informației și timpul de răspuns.
* **Mapping (Grupare):** Transformarea mișcărilor complexe NinaPro în 6 comenzi funcționale de control:
    * **Rest, Power, Precision, Lateral, Extension, Special**.
* **Normalizare:** Aplicarea standardizării Z-Score: $z = \frac{x - \mu}{\sigma}$.

### 4.3 Structurarea seturilor de date

**Împărțire (Strategie Interleaved):**
* **Train (Repetițiile 1, 2, 4, 6):** Folosit pentru optimizarea ponderilor rețelei CNN1D.
* **Validation (Repetițiile 3 și 5):** Folosit pentru monitorizarea generalizării și reglarea hiperparametrilor în timpul antrenării.
* **Test (Subiect S1):** Date de tip Hold-out, complet neatinse în faza de antrenare, folosite pentru validarea finală a sistemului și generarea metricilor de performanță.

### 4.4 Salvarea rezultatelor preprocesării

* **Format date:** Datele procesate sunt stocate sub formă de tensori PyTorch (**torch.Tensor**) în fișiere de tip `.pt`, optimizate pentru antrenare rapidă pe GPU/CPU.
* **Normalizare:** Parametrii statistici (media $\mu$ și deviația standard $\sigma$) sunt salvați în `config/preprocessing_params.pkl` pentru a fi aplicați identic în timpul inferenței live în `main.py`.
* **Artefacte salvate:**
    * `models/optimized_model.pth` – Modelul PyTorch final (arhitectură + ponderi + istoric).
    * `config/optimized_config.yaml` – Configurația finală a hiperparametrilor și a pragurilor de post-procesare.

---

## 5. Fișiere Generate în Această Etapă

* `data/train/train_set.pt`, `data/validation/val_set.pt` – Seturile de antrenament și validare rezultate.
* `data/test/test_set_S1.pt` – Datele de test pentru subiectul S1.
* `src/preprocessing/data_cleaner.py` – Scriptul de eliminare a zgomotului și rectificare.
* `src/preprocessing/data_splitter.py` – Scriptul care implementează logica de split pe repetiții.
* `docs/results/learning_curves_final.png` – Vizualizarea convergenței modelului.

---

##  6. Stare Etapă (de completat de student)

[x] Structură repository configurată
[x] Dataset analizat (Identificat probleme etichete și variabilitate)
[x] Date preprocesate (Windowing, Normalizare, Grupare 7 clase)
[x] Date augmentate (40% contribuție proprie)
[x] Seturi train/val/test generate (Stratified Split)
[x] Documentație actualizată în README + README_Etapa3.md

---