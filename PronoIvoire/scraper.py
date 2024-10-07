import requests
from bs4 import BeautifulSoup
import json
import os
import logging

def pronostics_football_aujourdhui():
    json_file_path = os.path.join('', 'pronostics_football.json')  # Définir le chemin du fichier JSON

    # Vérifier si les données sont déjà stockées dans le fichier JSON
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                cached_data = json.load(json_file)
                return cached_data  # Retourner les données depuis le fichier JSON
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Erreur lors de la lecture du fichier JSON : {e}")
            return {'error': 'Erreur lors de la lecture des données stockées.'}

    # Si le fichier n'existe pas ou s'il y a une erreur de lecture, on scrape les données
    url = 'https://pronosticsfootball365.com/pronostics-football-aujourdhui/'  # URL à scraper
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Gérer les erreurs HTTP
    except requests.RequestException as e:
        logging.error(f"Échec de la récupération des données depuis {url}: {e}")
        return {'error': f'Erreur lors de la récupération des données: {str(e)}'}

    # Analyse du HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    competitions = []

    # Extraction des compétitions et des matchs
    for competition_div in soup.find_all('div', class_='competition'):
        competition_name_div = competition_div.find('div', class_='name')
        competition_name = competition_name_div.get_text(strip=True) if competition_name_div else 'Nom de compétition non disponible'

        matches = []

        # Extraction des matchs pour chaque compétition
        for match_div in competition_div.find_all('div', class_='cmatch'):
            match_time_div = match_div.find('div', class_='time')
            teams_div = match_div.find('div', class_='teams')
            tip_div = match_div.find('div', class_='tip').find('div', class_='value') if match_div.find('div', 'tip') else None

            match_time = match_time_div.get_text(strip=True) if match_time_div else 'Heure non disponible'
            teams = teams_div.get_text(strip=True) if teams_div else 'Match non disponible'
            pronostic = tip_div.get_text(strip=True) if tip_div else 'Pronostic non disponible'

            # Ajout des coefficients et valeurs
            inforow_div = match_div.find_next('div', class_='inforow')
            coefficients = []
            values = []

            if inforow_div:
                coef_row = inforow_div.find('div', class_='coefrow')
                if coef_row:
                    coefficients = [coef.get_text(strip=True) for coef in coef_row.find_all('div', class_='value')]
                    values = [value.get_text(strip=True) for value in coef_row.find_all('div', class_='coefbox')]

            # Ajout du match aux matches
            matches.append({
                'match_time': match_time,
                'teams': teams,
                'pronostic': pronostic,
                'coefficients': coefficients,
                'values': values,
            })

        # Ajout de la compétition aux compétitions
        competitions.append({
            'competition_name': competition_name,
            'matches': matches,
        })

    # Enregistrement des données dans un fichier JSON
    json_data = {'competitions': competitions}

    try:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        logging.info(f"Données enregistrées dans {json_file_path}")
    except IOError as e:
        logging.error(f"Erreur lors de l'enregistrement du fichier JSON: {e}")
        return {'error': f"Erreur lors de l'enregistrement du fichier JSON: {str(e)}"}

    return json_data  # Retourner les données extraites
