import torch
import numpy as np
from model import EMG_CNN1D_Improved

def run_ensemble():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Se incarca ambele modele
    model1 = EMG_CNN1D_Improved().to(device)
    model1.load_state_dict(torch.load("proiect-rn-Iordache-Robert-Georgian/models/trained_model.pth", map_location=device)['model_state_dict'])
    
    model2 = EMG_CNN1D_Improved().to(device)
    model2.load_state_dict(torch.load("proiect-rn-Iordache-Robert-Georgian/models/optimized_model.pth", map_location=device)['model_state_dict'])
    
    model1.eval()
    model2.eval()
    
    # Simulare Ensemble pe un singur batch de test
    test_data = torch.load("../../data/test/test_set_S1.pt", weights_only=False)
    sample_input = test_data['x'][:10].to(device)
    
    with torch.no_grad():
        out1 = torch.softmax(model1(sample_input), dim=1)
        out2 = torch.softmax(model2(sample_input), dim=1)
        
        # Media probabilitatilor (Soft Voting)
        final_probs = (out1 + out2) / 2
        predictions = torch.argmax(final_probs, dim=1)
        
    print(f"🤖 Ensemble Predictions: {predictions.cpu().numpy()}")

if __name__ == "__main__":
    run_ensemble()