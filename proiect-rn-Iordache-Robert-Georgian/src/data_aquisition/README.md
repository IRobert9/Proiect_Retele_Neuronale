# 📥 Modul 1: Achizitia Datelor EMG

## 1. Descriere
Acest modul reprezinta prima etapa a pipeline-ului de procesare. El se ocupa de captarea semnalelor bio-electrice de la nivelul antebratului folosind o configuratie de **7 canale de achizitie**.

## 2. Metodologie
Semnalul EMG (Electromiografic) captat este unul stocastic (aleator), avand amplitudini cuprinse de obicei intre $0$ si $10$ mV. 
Modelul matematic utilizat pentru simularea achizitiei este:
$$EMG(t) = \sum_{n=1}^{N} MUAP_n(t-t_n) + w(t)$$
unde $MUAP$ reprezinta potentialul de actiune al unitatilor motorii, iar $w(t)$ este zgomotul alb de fond.

## 3. Scripturi incluse
* **`generate.py`**: Simuleaza procesul de achizitie si salveaza datele in format brut (`.pt`) in folderul `data/raw/`.
* **Configuratie**: Frecventa de esantionare utilizata este de **1000 Hz**, respectand teorema Nyquist pentru semnalele musculare.

## 4. Output
Rezultatul acestui modul consta in fisiere de tip tensor care contin:
* **Semnalul Brut**: Matrice de dimensiune $[Timp \times 7]$.
* **Eticheta**: Gestul efectuat in timpul inregistrarii.