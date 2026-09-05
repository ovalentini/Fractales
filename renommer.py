import os
import re
import subprocess

# Dossier contenant les images (à adapter si besoin)
folder = "compositions/pictures"

for filename in os.listdir(folder):
    if filename.lower().endswith(".jpg"):
        # Cherche le motif "Bing X" ou "Pause contemplative X" avec un espace avant le numéro
        match = re.match(r"^(.+?) (\d+)\.jpg$", filename, re.IGNORECASE)
        if match:
            base_name = match.group(1)
            number = match.group(2)
            new_filename = f"{base_name}-{number}.jpg"
            
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)
            
            if old_path != new_path:
                print(f"Renommage : {filename} → {new_filename}")
                # Utilise git mv pour que Git suive le renommage correctement
                subprocess.run(["git", "mv", old_path, new_path])