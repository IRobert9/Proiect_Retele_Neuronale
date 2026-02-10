import torch
import os

def combine_all_gestures(processed_dir, final_path):
    all_x = []
    all_y = []
    gestures = ['Rest', 'Power', 'Precision', 'Lateral', 'Extension', 'Special']
    
    for idx, g in enumerate(gestures):
        file_path = os.path.join(processed_dir, f"clean_{g}.pt")
        if os.path.exists(file_path):
            data = torch.load(file_path, weights_only=False)
            all_x.append(data['x'])
            all_y.append(torch.full((data['x'].shape[0],), idx))
    
    final_x = torch.cat(all_x, dim=0)
    final_y = torch.cat(all_y, dim=0)
    
    torch.save({'x': final_x, 'y': final_y, 'class_names': gestures}, final_path)
    print(f"📦 Dataset FINAL combinat salvat la: {final_path}")