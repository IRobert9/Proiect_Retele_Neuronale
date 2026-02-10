import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import sys

# Importam modelul din fisierul model.py aflat in acelasi folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model import EMG_CNN1D_Improved 

def train():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    TRAIN_DATA = "proiect-rn-Iordache-Robert-Georgian/data/train/train_set.pt"
    VAL_DATA = "proiect-rn-Iordache-Robert-Georgian/data/validation/val_set.pt"
    SAVE_PATH = "proiect-rn-Iordache-Robert-Georgian/models/trained_model.pth"
    
    os.makedirs("proiect-rn-Iordache-Robert-Georgian/models", exist_ok=True)
    
    # Incarcam seturile de date
    train_data = torch.load(TRAIN_DATA, weights_only=False)
    val_data = torch.load(VAL_DATA, weights_only=False)
    
    train_loader = DataLoader(TensorDataset(train_data['x'], train_data['y']), batch_size=64, shuffle=True)
    val_loader = DataLoader(TensorDataset(val_data['x'], val_data['y']), batch_size=64)

    model = EMG_CNN1D_Improved(num_classes=6).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=0.0008)
    criterion = nn.CrossEntropyLoss() # Baseline simplu
    
    # Antrenare scurta (Baseline)
    for epoch in range(50):
        model.train()
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(inputs), labels)
            loss.backward()
            optimizer.step()
            
    torch.save({'model_state_dict': model.state_dict()}, SAVE_PATH)
    print(f"✅ Baseline model salvat în {SAVE_PATH}")

if __name__ == "__main__":
    train()