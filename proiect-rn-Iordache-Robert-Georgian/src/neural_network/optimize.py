import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import sys

# Import local
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model import EMG_CNN1D_Improved 

class FocalLoss(nn.Module):
    def __init__(self, alpha=None, gamma=3.0, label_smoothing=0.05):
        super().__init__()
        self.alpha, self.gamma, self.label_smoothing = alpha, gamma, label_smoothing
    
    def forward(self, inputs, targets):
        ce_loss = F.cross_entropy(inputs, targets, weight=self.alpha, reduction='none', label_smoothing=self.label_smoothing)
        pt = torch.exp(-ce_loss)
        return ((1 - pt) ** self.gamma * ce_loss).mean()

def optimize():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    DATA_PATH = "proiect-rn-Iordache-Robert-Georgian/data/processed/data_preprocessed_FINAL.pt"
    SAVE_PATH = "proiect-rn-Iordache-Robert-Georgian/models/optimized_model.pth"
    
    # Incarcare date
    data = torch.load(DATA_PATH, weights_only=False)
    x, y, reps = data['x'], data['y'], data['reps']
    
    # Normalizare si Split Interleaved
    x = (x - x.mean(0)) / (x.std(0) + 1e-8)
    train_mask = (reps == 1) | (reps == 2) | (reps == 4) | (reps == 6)
    val_mask = (reps == 3) | (reps == 5)
    
    train_loader = DataLoader(TensorDataset(x[train_mask], y[train_mask]), batch_size=256, shuffle=True)
    val_loader = DataLoader(TensorDataset(x[val_mask], y[val_mask]), batch_size=256)

    model = EMG_CNN1D_Improved().to(device)
    
    # Anti-Rest Bias: weights ajustate manual
    weights = torch.FloatTensor([0.6, 1.4, 1.4, 1.3, 1.3, 1.3]).to(device)
    criterion = FocalLoss(alpha=weights, gamma=3.0)
    optimizer = optim.AdamW(model.parameters(), lr=0.0008, weight_decay=1e-3)
    
    history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}
    best_acc = 0

    for epoch in range(150): # 150 Epoci 
        model.train()
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(inputs), labels)
            loss.backward()
            optimizer.step()
        
        # Validare
        model.eval()
        v_correct, v_total = 0, 0
        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                v_correct += (model(inputs).argmax(1) == labels).sum().item()
                v_total += labels.size(0)
        
        current_acc = v_correct / v_total
        history['val_acc'].append(current_acc)
        
        if current_acc > best_acc:
            best_acc = current_acc
            torch.save({'model_state_dict': model.state_dict(), 'history': history}, SAVE_PATH)

    print(f"✅ Optimizare completa. Best Acc: {best_acc:.4f} salvat în {SAVE_PATH}")

if __name__ == "__main__":
    optimize()