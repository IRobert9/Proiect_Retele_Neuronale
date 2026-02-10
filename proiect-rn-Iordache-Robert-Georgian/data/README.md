# Documentație Dataset: Control Mioelectric (Subiect S40)

Acest director conține fluxul complet de date utilizat pentru antrenarea și validarea sistemului de recunoaștere a gesturilor. Întregul set de date reprezintă o **contribuție originală 100%**, fiind generat printr-un pipeline de simulare fizică și achiziție sintetică ce reproduce fidel semnalele electromiografice (EMG) de suprafață.

## 1. Structura Directorului

| Folder | Conținut | Rol în Proiect |
|:---|:---|:---|
| `raw/` | Fișiere `.csv` brute | Datele inițiale rezultate din generator, înainte de orice procesare. |
| `processed/` | Fișiere `.npy` / `.csv` | Date filtrate (Notch, Bandpass) și normalizate (Z-score). |
| `generated/` | Dataset original | **Nucleul contribuției proprii.** Conține eșantioanele pentru cele 6 clase. |
| `train/` | Subset antrenare (70%) | Utilizat pentru optimizarea ponderilor rețelei CNN 1D. |
| `validation/` | Subset validare (15%) | Utilizat pentru monitorizarea overfitting-ului și Early Stopping. |
| `test/` | Subset test (15%) | Date "unseen" folosite pentru raportarea metricilor finale. |



## 2. Caracteristicile Datelor

Eșantioanele simulează activitatea musculară a antebrațului (Subiect S1) captată prin 7 senzori plasați circular.

* **Număr Canale:** 7 (EMG_0 la EMG_6).
* **Frecvență de Eșantionare:** 1000 Hz.
* **Clase (6):** `Rest`, `Power Grip`, `Precision Pinch`, `Extension`, `Lateral Grip`, `Special Gesture`.
* **Volum Total:** 18,000 observații (3,000 per clasă).
* **Format:** Fereastră glisantă de 400 ms (400 eșantioane/fereastră).



## 3. Pipeline de Preprocesare

Pentru transformarea datelor din `raw/` în `processed/`, au fost aplicate următoarele etape:

1.  **Filtrare Notch (50 Hz):** Eliminarea interferențelor cauzate de rețeaua electrică.
2.  **Filtrare Bandpass (20-500 Hz):** Izolarea spectrului de frecvență caracteristic contracției musculare voluntare.
3.  **Normalizare Z-score:** Ajustarea mediei la 0 și a deviației standard la 1 pentru fiecare canal, asigurând o convergență rapidă a modelului.
4.  **Segmentare:** Împărțirea semnalului continuu în ferestre de 400 ms cu un overlap de 50%.

## 4. Declarație de Originalitate (Cerința Etapa 4)

Conform cerințelor disciplinei, confirm că **100% din datele prezente în acest director sunt rezultatul muncii proprii**. 
- Nu s-au utilizat dataset-uri publice (ex: NinaPro, UCI).
- Datele au fost create folosind scriptul `src/data_acquisition/generate.py`, implementând un model matematic de activare musculară și zgomot electronic specific senzorilor de suprafață.
- Fiecare observație a fost etichetată automat în momentul generării, asigurând un set de date "gold standard" pentru antrenare.



---
**Notă:** Pentru a regenera întregul set de date, se poate rula scriptul de achiziție cu parametrii specificați în `config/generation_params.json`.