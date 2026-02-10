import torch
import matplotlib.pyplot as plt
import os
import sys

# 1. CALCULARE CAI ABSOLUTE (Anti-Eroare)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

# Folderele de salvare
RESULTS_DIR = os.path.join(PROJECT_ROOT, "docs", "results")
OPTIM_DIR = os.path.join(PROJECT_ROOT, "docs", "optimization")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "optimized_model.pth")

def run_visualizer():
    # Cream folderele fortat
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(OPTIM_DIR, exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print(f"❌ EROARE: Nu gasesc modelul la: {MODEL_PATH}")
        return

    print(f"🔄 Incarcare model din: {MODEL_PATH}")
    checkpoint = torch.load(MODEL_PATH, map_location='cpu', weights_only=False)
    
    if 'history' not in checkpoint:
        print("❌ EROARE: Modelul nu are istoric de antrenare.")
        return

    h = checkpoint['history']
    epochs = range(1, len(h['train_loss']) + 1)

    print("📊 Generare grafice pentru RESULTS...")

    # --- 1. loss_curve.png ---
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, h['train_loss'], label='Train Loss')
    plt.plot(epochs, h['val_loss'], label='Val Loss')
    plt.title("Evolutie Loss (Etapa 5)")
    plt.legend(); plt.grid(True)
    plt.savefig(os.path.join(RESULTS_DIR, "loss_curve.png"))
    plt.close()

    # --- 2. metrics_evolution.png ---
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, h['train_acc'], label='Train Acc')
    plt.plot(epochs, h['val_acc'], label='Val Acc')
    plt.axhline(y=70, color='r', linestyle='--', label='Target 70%')
    plt.title("Evolutie Metrici (Etapa 6)")
    plt.legend(); plt.grid(True)
    plt.savefig(os.path.join(RESULTS_DIR, "metrics_evolution.png"))
    plt.close()

    # --- 3. learning_curves_final.png ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(h['train_loss']); ax1.set_title("Loss Final")
    ax2.plot(h['train_acc']); ax2.set_title("Accuracy Final")
    plt.savefig(os.path.join(RESULTS_DIR, "learning_curves_final.png"))
    plt.close()

    print("📈 Generare grafice pentru OPTIMIZATION...")

    # --- 4. accuracy_comparison.png ---
    plt.figure(figsize=(8, 5))
    labels = ['Model Brut', 'Sistem Optimizat']
    values = [58.74, 81.24] # Valorile tale reale
    plt.bar(labels, values, color=['gray', 'green'])
    plt.title("Comparatie Acuratete")
    plt.ylabel("%")
    plt.savefig(os.path.join(OPTIM_DIR, "accuracy_comparison.png"))
    plt.close()

    # --- 5. f1_comparison.png ---
    plt.figure(figsize=(8, 5))
    f1_vals = [0.55, 0.80]
    plt.bar(labels, f1_vals, color=['orange', 'blue'])
    plt.title("Comparatie Scor F1")
    plt.savefig(os.path.join(OPTIM_DIR, "f1_comparison.png"))
    plt.close()

    print(f"\n✅ TOTUL A FOST SALVAT IN:")
    print(f"📂 {RESULTS_DIR}")
    print(f"📂 {OPTIM_DIR}")

if __name__ == "__main__":
    run_visualizer()