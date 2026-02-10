import torch
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

def clean_emg_data(input_path, output_path):
    """
    Aplica rectificare si eliminare offset pentru datele brute.
    """
    data = torch.load(input_path, weights_only=False)
    raw_x = data['x']
    
    # 1. Eliminare DC Offset (centrare pe zero)
    clean_x = raw_x - torch.mean(raw_x, dim=0)
    
    # 2. Rectificare (Full-wave rectification)
    # Transforma semnalul din oscilatie +/- in valori strict pozitive
    clean_x = torch.abs(clean_x)
    
    torch.save({'x': clean_x, 'y': data.get('gesture', 'unknown')}, output_path)
    print(f"✅ Date curatate salvate la: {output_path}")

if __name__ == "__main__":
    # Exemplu pentru un gest
    raw_path = os.path.join(PROJECT_ROOT, "data", "raw", "raw_Power.pt")
    out_path = os.path.join(PROJECT_ROOT, "data", "processed", "clean_Power.pt")
    if os.path.exists(raw_path):
        clean_emg_data(raw_path, out_path)