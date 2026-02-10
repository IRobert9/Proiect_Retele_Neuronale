# Modul 2: Arhitectura și Antrenarea Rețelei Neuronale

Acest modul reprezintă centrul decizional al sistemului, fiind responsabil pentru extragerea trăsăturilor din semnalele EMG brute și clasificarea acestora în cele 6 gesturi specifice. Implementarea este realizată în **PyTorch**, utilizând o arhitectură de tip rețea neuronală convoluțională unidimensională (CNN 1D).

## 1. Structura Modulului

| Fișier | Funcționalitate | Etapa Proiect |
|:---|:---|:---|
| `model.py` | Definirea clasei `EMG_CNN1D_Improved`. Conține arhitectura straturilor. | Etapa 4 |
| `train.py` | Pipeline-ul de antrenare, inclusiv logica de Backpropagation și Early Stopping. | Etapa 5 |
| `evaluate.py` | Calcularea metricilor pe setul de test (Accuracy, F1-Score, Precision, Recall). | Etapa 5 |
| `optimize.py` | Script pentru rularea experimentelor de tip Grid Search / Fine-tuning. | Etapa 6 |
| `visualize.py` | Generarea de grafice pentru Loss/Accuracy și Confusion Matrix. | Etapa 5/6 |

## 2. Arhitectura Detaliată (CNN 1D)

Arhitectura a fost selectată pentru capacitatea de a învăța automat filtre spațio-temporale peste cele 7 canale EMG, eliminând necesitatea extragerii manuale a trăsăturilor (feature engineering).



### Specificații Straturi:
1.  **Input Layer**: Dimensiune $[Batch, 7, 400]$ (7 canale, fereastră de 400ms).
2.  **Conv Block 1**: `Conv1d` (64 filtre, kernel 5) + `BatchNorm1d` + `ReLU`.
3.  **Pooling**: `MaxPool1d` (kernel 2) - reduce dimensiunea temporală la jumătate.
4.  **Conv Block 2**: `Conv1d` (128 filtre, kernel 3) + `BatchNorm1d` + `ReLU`.
5.  **Fully Connected**:
    * `Flatten`
    * `Linear` (128 neuroni) + `ReLU` + **`Dropout (0.5)`**
    * `Output Layer` (6 neuroni) + `Softmax`.

### Funcția de Pierdere (Loss Function):
Se utilizează **Cross-Entropy Loss**, definită matematic ca:
$$L = -\frac{1}{N} \sum_{i=1}^{N} \sum_{c=1}^{C} y_{i,c} \log(p_{i,c})$$
unde $C=6$ (numărul de clase) și $N$ este dimensiunea batch-ului.



## 3. Procesul de Antrenare și Optimizare

Antrenarea modelului a fost optimizată în Etapa 6 prin următoarele tehnici:
* **Adaptive Learning Rate**: Utilizarea optimizatorului Adam cu $LR = 0.001$.
* **Regularizare**: Introducerea straturilor de Dropout și Batch Normalization pentru a preveni memorarea zgomotului din semnalul EMG.
* **Early Stopping**: Procesul este întrerupt dacă `val_loss` nu se îmbunătățește timp de 15 epoci, prevenind astfel *overfitting*-ul.

## 4. Evaluare și Rezultate

Modelul final obține o acuratețe de **81.24%** pe setul de date al subiectului S1. Performanța este validată prin scriptul `evaluate.py`, care generează rapoarte detaliate de clasificare.



### Instrucțiuni Rulare:

1.  **Antrenare**:
    ```bash
    python train.py --epochs 150 --batch_size 32
    ```
2.  **Evaluare**:
    ```bash
    python evaluate.py --model_path ../models/optimized_model.pth
    ```
3.  **Optimizare (Etapa 6)**:
    ```bash
    python optimize.py --search_space grid
    ```

---
**Notă:** Toate modelele antrenate sunt salvate în directorul principal `/models/` în format `.pth`.