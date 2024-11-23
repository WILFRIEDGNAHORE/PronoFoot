import requests
from bs4 import BeautifulSoup
import json

# URL à scraper
url = 'https://pronosticsfootball365.com/les-meilleurs-pronostics-foot-du-jour/'

# Envoyer une requête pour récupérer le contenu de la page
response = requests.get(url)

# Vérifier si la requête est réussie
if response.status_code == 200:
    html_content = response.text
    
    # Parse le HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Trouver toutes les compétitions
    competitions = soup.find_all('div', class_='competition')

    # Liste pour stocker les données
    all_data = []

    # Parcourir chaque compétition
    for competition in competitions:
        competition_data = {}
        
        # Extraire les informations générales de la compétition
        competition_name = competition.find('div', class_='name')
        competition_data['competition_name'] = competition_name.text.strip() if competition_name else 'N/A'
        
        # Trouver tous les matchs de la compétition
        matches = competition.find_all('div', class_='match')
        
        match_list = []
        
        # Parcourir chaque match
        for match in matches:
            match_data = {}
            
            # Extraire l'heure
            match_time_div = match.find('div', class_='date')
            match_data['date'] = match_time_div.get_text(strip=True) if match_time_div else 'Heure non disponible'
            
            # Extraire les équipes
            host_team = match.find('div', class_='hostteam')
            guest_team = match.find('div', class_='guestteam')
            match_data['host_team'] = host_team.find('div', class_='name').text.strip() if host_team else 'N/A'
            match_data['guest_team'] = guest_team.find('div', class_='name').text.strip() if guest_team else 'N/A'
            
            # Extraire le pronostic
            tip = match.find('div', class_='value')
            match_data['tip'] = tip.text.strip() if tip else 'N/A'
            
            # Extraire les cotes
            coefs = match.find('div', class_='coefrow').find_all('div', class_='coefbox')
            coef_values = [coef.find('div', class_='value').text.strip() for coef in coefs if coef.find('div', class_='value')]
            match_data['coef'] = coef_values if coef_values else 'N/A'
            
            # Ajouter le match aux données
            match_list.append(match_data)
        
        # Ajouter les matchs à la compétition
        competition_data['matches'] = match_list
        
        # Ajouter la compétition aux données globales
        all_data.append(competition_data)

    # Enregistrer les données dans un fichier JSON
    with open('meilleur_prono_foot_aujourdhui.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print("Les données ont été enregistrées dans prono_foot_aujourdhui.json")
else:
    print(f"Erreur lors de la récupération des données : {response.status_code}")
