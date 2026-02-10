import torch
import numpy as np
import tkinter as tk
from tkinter import messagebox
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- CAI ABSOLUTE ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
sys.path.append(os.path.join(PROJECT_ROOT, "src", "neural_network"))

try:
    from model import EMG_CNN1D_Improved #
    from postprocess import EMGPostProcessor #
except ImportError:
    print("Eroare: Nu gasesc modulele necesare in src/neural_network/")
    sys.exit(1)

class EMGAppSimulareFinal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulare Live 7-Channel EMG - Robert Iordache")
        self.geometry("1000x850")
        self.configure(bg="#f0f0f0")
        
        # Gestionare inchidere corecta
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.is_active = True
        
        # Cai resurse
        self.MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "optimized_model.pth")
        self.DATA_PATH = os.path.join(PROJECT_ROOT, "data", "test", "test_set_S1.pt")
        self.STATS_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "data_preprocessed_FINAL.pt")
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.class_names = ['Rest', 'Power', 'Precision', 'Lateral', 'Extension', 'Special']
        self.idx = 0
        
        # Initializam 7 liste pentru istoria celor 7 canale
        self.data_history = [[] for _ in range(7)] 

        self.load_resources()
        self.setup_ui()
        self.run_simulation() 

    def load_resources(self):
        try:
            ckpt = torch.load(self.MODEL_PATH, map_location=self.device, weights_only=False)
            self.model = EMG_CNN1D_Improved().to(self.device) #
            self.model.load_state_dict(ckpt['model_state_dict'])
            self.model.eval()

            stats = torch.load(self.STATS_PATH, weights_only=False)
            self.mean, self.std = stats['x'].mean(0), stats['x'].std(0) + 1e-8
            
            data_test = torch.load(self.DATA_PATH, weights_only=False)
            self.x_test_raw = data_test['x']
            self.x_test_norm = (self.x_test_raw - self.mean) / self.std
            self.y_test = data_test['y']
            
            self.processor = EMGPostProcessor(hysteresis_threshold=6) #
        except Exception as e:
            print(f"Eroare la incarcare: {e}")
            sys.exit(1)

    def setup_ui(self):
        # Configurare Plot Multi-Canal
        self.fig, self.ax = plt.subplots(figsize=(8, 4.5))
        self.ax.set_title("Activitate Live - 7 Senzori EMG", fontsize=12, fontweight='bold')
        self.ax.set_xlabel("Timp (Esantioane)")
        self.ax.set_ylabel("Amplitudine (uV)")
        
        # Culori distincte pentru fiecare canal
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FF00FF', '#00FFFF', '#FFA500', '#800080']
        self.lines = []
        for i in range(7):
            line, = self.ax.plot([], [], lw=1.2, color=colors[i], label=f"CH{i+1}", alpha=0.8)
            self.lines.append(line)
        
        self.ax.set_ylim([-1.3, 1.3])
        self.ax.set_xlim([0, 100])
        self.ax.grid(True, linestyle='--', alpha=0.5)
        self.ax.legend(loc='upper right', ncol=4, fontsize='8')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(pady=15, fill="both", expand=True)

        # Labels UI
        self.info_frame = tk.Frame(self, bg="#f0f0f0")
        self.info_frame.pack(pady=5)

        self.lbl_real = tk.Label(self.info_frame, text="Real: ---", font=("Arial", 11), bg="#f0f0f0")
        self.lbl_real.pack()

        self.lbl_pred = tk.Label(self.info_frame, text="Predictie AI: ---", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.lbl_pred.pack(pady=5)

        self.lbl_status = tk.Label(self, text="STATUS: INITIALIZARE", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.lbl_status.pack(pady=15)

    def run_simulation(self):
        if not self.is_active:
            return

        if self.idx < len(self.x_test_norm):
            # Predictie
            sample = self.x_test_norm[self.idx].unsqueeze(0).to(self.device)
            with torch.no_grad():
                out = self.model(sample).argmax(1).item()
            
            stable = self.processor.process_prediction(out) #
            real = self.y_test[self.idx].item()

            # Update date pentru toate cele 7 canale
            for i in range(7):
                val = self.x_test_raw[self.idx][i].item()
                self.data_history[i].append(val)
                if len(self.data_history[i]) > 100:
                    self.data_history[i].pop(0)
                
                # Actualizam fiecare linie individual
                self.lines[i].set_data(range(len(self.data_history[i])), self.data_history[i])

            # UI Update
            is_correct = (stable == real)
            status_text = "IDENTIFICAT CORECT" if is_correct else "EROARE DETECTIE"
            status_color = "#2ecc71" if is_correct else "#e74c3c"

            try:
                self.canvas.draw_idle()
                self.lbl_real.config(text=f"Subiectul executa: {self.class_names[real]}")
                self.lbl_pred.config(text=f"Decizie Sistem: {self.class_names[stable]}", fg=status_color)
                self.lbl_status.config(text=status_text, fg=status_color)
            except tk.TclError:
                return 

            self.idx += 1
            self.after(50, self.run_simulation)
        else:
            self.lbl_status.config(text="SIMULARE FINALIZATA", fg="black")

    def on_closing(self):
        self.is_active = False
        self.quit()
        self.destroy()
        sys.exit(0)

if __name__ == "__main__":
    app = EMGAppSimulareFinal()
    app.mainloop()