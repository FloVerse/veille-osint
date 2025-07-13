import requests
import pandas as pd
import schedule
import time
from datetime import datetime
import os

dir = "exports"
os.makedirs(dir, exist_ok=True)

def run_osint_veille():
    print(f"Début de la veille à {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    keywords = [
    "osint", "leak", "recon", "reconnaissance", "crawler", "scraper",
    "footprinting", "intel", "intelligence", "github-dork", "search-engine",
    "metadata", "email-harvest", "social-media", "person-tracker", "profiling",
    "darkweb", "tor", "pastebin", "breach", "exposure", "monitoring",
    "whois", "subdomain", "dork", "geolocation", "api-osint"
]

    url = "https://api.github.com/search/repositories?q=osint&sort=updated&order=desc&per_page=15"
    response = requests.get(url)
    data = response.json()

    results = []

    for repo in data.get("items", []):
        name = repo["name"].lower()
        description = (repo.get("description") or "").lower()
        if any(kw in name or kw in description for kw in keywords):
            results.append({
                "Nom": repo["name"],
                "Description": repo.get("description"),
                "URL": repo["html_url"],
                "Date de mise à jour": repo["updated_at"]
            })

    # Enregistrement des résultats dans un fichier CSV
    if results: 
        df = pd.DataFrame(results)
        filename = f"veille_osint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = os.path.join(dir, filename)
        df.to_csv(filepath, index=False)
        print(f"{len(results)} dépôts filtrés enregistrés dans {filepath}")
    else:
        print("Aucun dépôt correspondant aux mots-clés.")

# Planfication de la tâche tous les jours à 08h00
schedule.every().day.at("08:00").do(run_osint_veille)
# Main
print("Script en veille...")
while True:
    schedule.run_pending()
    time.sleep(60)
