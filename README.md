# Projet de veille OSINT automatisée

Ce projet interroge quotidiennement GitHub pour détecter les dépôts récents liés à l'OSINT (Open Source Intelligence). Il filtre les résultats selon des mots-clés pertinents, puis les exporte automatiquement dans un fichier CSV horodaté.

## 🔧 Fonctionnalités
- Requête vers l’API GitHub
- Filtrage par mots-clés OSINT
- Export CSV automatique dans un dossier `exports/`
- Exécution planifiée chaque jour à 08h

## 📦 Installation

`pip install -r requirements.txt`

## ▶️ Lancement
`python veille_osint.py`

## 📁 Résultats
Les fichiers `.csv` sont enregistrés dans le dossier `exports/`.

## 📌 Exemple d'application
- Veille sur les nouveaux outils OSINT open-source
- Détection d'outils exploitables pour des moteurs d'analyse
- Apprentissage personnel en automatisation + cyberveille
