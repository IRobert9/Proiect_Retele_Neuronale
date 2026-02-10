import numpy as np

class EMGPostProcessor:
    def __init__(self, window_size=7, hysteresis_threshold=6):
        self.window_size = window_size
        self.hysteresis_threshold = hysteresis_threshold
        self.history = []
        self.current_state = 0 # Implicit 'Rest'

    def process_prediction(self, raw_pred):
        self.history.append(raw_pred)
        if len(self.history) > self.window_size:
            self.history.pop(0)
        
        counts = np.bincount(self.history, minlength=6)
        most_frequent = np.argmax(counts)
        
        # Logica de Hysteresis: schimbam starea doar daca noul gest e foarte sigur
        if counts[most_frequent] >= self.hysteresis_threshold:
            self.current_state = most_frequent
            
        return self.current_state