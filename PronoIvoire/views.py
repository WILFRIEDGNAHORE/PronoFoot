from django.shortcuts import render
from .scraper import pronostics_football_aujourdhui  # Importez la fonction de scraping

def scrape_and_cache(request):
    result = pronostics_football_aujourdhui()
    if 'error' in result:
        return render(request, 'pronostics_football_aujourdhui.html', {'error': result['error']})

    return render(request, 'pronostics_football_aujourdhui.html', {'pronostics': result['competitions']})
