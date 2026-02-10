import torch
import os

def extract_features(tensor_x):
    """
    In acest proiect, 'features' reprezinta semnalul normalizat.
    Putem adauga aici si Root Mean Square (RMS).
    """
    # Exemplu: calculam RMS pe ferestre mici daca e nevoie
    # Dar pentru arhitectura ta CNN1D, folosim direct semnalul normalizat
    return tensor_x 

def normalize_dataset(x, mean=None, std=None):
    if mean is None:
        mean = x.mean(dim=0)
    if std is None:
        std = x.std(dim=0) + 1e-8
    return (x - mean) / std, mean, std