import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

# Helper function to load JSON data
def load_pronostics_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None  # Return None if file is not found
    except json.JSONDecodeError:
        return None  # Return None if there's an error in the JSON format

# View to handle the homepage
def home(request):
    return render(request, 'home.html', {})

# View for pronostics today
def display_pronostics_aujourdhui(request):
    # Load data from JSON file
    pronostics_data = load_pronostics_data('prono_foot_aujourdhui.json')
    
    if pronostics_data is None:
        return render(request, 'pronostics_aujourdhui.html', {'error': 'Les données de pronostics sont introuvables.'})
    
    # Paginate the pronostics data
    paginator = Paginator(pronostics_data, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pronostics_aujourdhui.html', {'pronostics': page_obj})

# View for pronostics tomorrow
def display_pronostics_Demain(request):
    # Load data from JSON file
    pronostics_data = load_pronostics_data('prono_foot_demain.json')
    
    if pronostics_data is None:
        return render(request, 'pronostics_demain.html', {'error': 'Les données de pronostics sont introuvables.'})
    
    # Paginate the pronostics data
    paginator = Paginator(pronostics_data, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pronostics_demain.html', {'pronostics': page_obj})

# View for the best pronostics of the day
def display_pronostics_Meilleur(request):
    # Load data from JSON file
    pronostics_data = load_pronostics_data('meilleur_prono_foot_aujourdhui.json')
    
    if pronostics_data is None:
        return render(request, 'pronostics_Meilleurs_prono_du_jour.html', {'error': 'Les données de pronostics sont introuvables.'})
    
    # Paginate the pronostics data
    paginator = Paginator(pronostics_data, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pronostics_Meilleurs_prono_du_jour.html', {'pronostics': page_obj})
