import torch
import numpy as np
import os

# --- CONFIGURARE CAI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

def generate_raw_emg_signal(duration_sec=10, fs=1000, num_channels=7):
    """
    Simuleaza achizitia de semnal EMG brut (Raw).
    EMG este modelat ca zgomot alb filtrat/modulat.
    """
    t = np.linspace(0, duration_sec, duration_sec * fs)
    # Generam zgomot de baza (zgomot termic al electrozilor)
    raw_signal = np.random.normal(0, 0.02, (len(t), num_channels))
    
    # Simulam o contractie (activitate musculara) intre secunda 3 si 7
    # Folosim o anvelopa sinusoidala pentru realism
    envelope = np.zeros(len(t))
    envelope[3*fs:7*fs] = np.sin(np.linspace(0, np.pi, 4*fs))
    
    for i in range(num_channels):
        raw_signal[:, i] += np.random.normal(0, 0.15, len(t)) * envelope
        
    return torch.tensor(raw_signal, dtype=torch.float32)

def save_raw_dataset():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("🚀 Incepere generare date brute pentru 6 gesturi...")
    
    # Generam cate un fisier brut pentru fiecare gest
    gestures = ['Rest', 'Power', 'Precision', 'Lateral', 'Extension', 'Special']
    
    for g in gestures:
        data = generate_raw_emg_signal()
        file_path = os.path.join(OUTPUT_DIR, f"raw_{g}.pt")
        torch.save({'x': data, 'gesture': g}, file_path)
        print(f"✅ Salvat semnal brut pentru: {g}")

if __name__ == "__main__":
    save_raw_dataset()
    print(f"\n📂 Datele brute au fost salvate in: {OUTPUT_DIR}")