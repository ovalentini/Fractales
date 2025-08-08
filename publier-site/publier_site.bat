@echo off
cd ..

echo 📦 Passage dans le dossier du projet...
cd Fractales

echo 🚀 Ajout des fichiers modifiés...
git add .

echo ✏️ Commit avec message automatique...
git commit -m "Mise à jour du site responsive (auto)"

echo 🌐 Envoi sur GitHub...
git push origin main

echo ✅ Publication terminée !
pause
