# 🧠 README - Interfata de Control si Simulare EMG

## 1. Descriere Proiect
Aceasta aplicatie reprezinta interfata grafica (GUI) finala a sistemului de control pentru proteza inteligenta. Ea integreaza modelul antrenat (CNN1D) cu logica de post-procesare pentru a oferi o experienta de utilizare stabila si intuitiva.

## 2. Componente Tehnice
Sistemul este construit modular pentru a permite prezentarea clara a fluxului de date:
* **Arhitectura AI**: Incarca reteaua `EMG_CNN1D_Improved` capabila sa recunoasca 6 clase de gesturi.
* **Filtrare Temporala**: Utilizeaza algoritmul de Hysteresis din `postprocess.py` pentru a preveni fluctuatiile intre gesturi.
* **Validare Real-Time**: Simularea ruleaza pe setul de date `test_set_S1.pt`, demonstrand performanta pe un subiect complet nou pentru model.

## 3. Functionalitati Interfata
Interfata grafica (bazata pe `simulare.py`) include urmatoarele elemente cheie:
* **Grafic Temporal**: Vizualizarea in timp real a curbei de decizie (Ground Truth vs. AI Smooth).
* **Feedback Vizual**: Indicatori colorati (Verde/Rosu) pentru confirmarea instantanee a corectitudinii predictiei.
* **Control Simulare**: Butoane pentru Start/Pauza si navigare rapida prin setul de date (+1500 cadre/skip).
* **Monitorizare Status**: Afisarea etichetelor brute ale retelei in comparatie cu rezultatul filtrat (Smooth AI).

## 4. Performante Obtinute
Sistemul atinge urmatorii indicatori de performanta:
* **Acuratete pe subiect necunoscut (S1)**: **81.24%** (dupa post-procesare).
* **Viteza de raspuns**: Predictia este actualizata la fiecare 40-50ms, asigurand un control fluid.
* **Stabilitate**: Hysteresis-ul elimina peste 90% din "sariturile" eronate intre clasele de gesturi.

## 5. Lansarea Aplicatiei
Pentru a rula interfata, asigurati-va ca sunteti in radacina proiectului si executati:
```bash
python src/app/main.py