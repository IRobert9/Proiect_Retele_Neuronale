import torch
import os

# --- REGLARE CAI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

def split_and_save_data():
    # 1. Cautam datele in folderul de date procesate
    DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "data_preprocessed_FINAL.pt")
    CALIB_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "data_CALIBRATION.pt")
    
    if not os.path.exists(DATA_PATH):
        print(f"❌ Eroare: Nu gasesc {DATA_PATH}. Ruleaza intai preprocessing-ul.")
        return

    data = torch.load(DATA_PATH, map_location='cpu', weights_only=False)
    x, y, reps = data['x'], data['y'], data['reps']
    
    # 2. LOGICA TA DE SPLIT (Interleaved - FOARTE BUNA)
    # Antrenament: 1, 2, 4, 6 | Validare: 3, 5
    train_mask = (reps == 1) | (reps == 2) | (reps == 4) | (reps == 6)
    val_mask = (reps == 3) | (reps == 5)
    
    x_train, y_train = x[train_mask], y[train_mask]
    x_val, y_val = x[val_mask], y[val_mask]
    
    # 3. Incarcare subiect S1 (Hold-out)
    test_data = torch.load(CALIB_PATH, map_location='cpu', weights_only=False)
    
    # 4. Definire cai de salvare finale
    train_dir = os.path.join(PROJECT_ROOT, "data", "train")
    val_dir = os.path.join(PROJECT_ROOT, "data", "validation")
    test_dir = os.path.join(PROJECT_ROOT, "data", "test")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # 5. Salvare in locatiile corecte
    torch.save({'x': x_train, 'y': y_train}, os.path.join(train_dir, "train_set.pt"))
    torch.save({'x': x_val, 'y': y_val}, os.path.join(val_dir, "val_set.pt"))
    torch.save(test_data, os.path.join(test_dir, "test_set_S1.pt"))
    
    print(f"✅ Date salvate corect in structura:")
    print(f"📂 Train: {os.path.join(train_dir, 'train_set.pt')} ({len(x_train)} samples)")
    print(f"📂 Val: {os.path.join(val_dir, 'val_set.pt')} ({len(x_val)} samples)")
    print(f"📂 Test: {os.path.join(test_dir, 'test_set_S1.pt')} ({len(test_data['x'])} samples)")

if __name__ == "__main__":
    split_and_save_data()