from django.urls import path
from . import views  # Remplace 'your_app' par le nom de ton application

urlpatterns = [
    path('', views.scrape_and_cache, name='scrape_and_cache'),  # Afficher les résultats du scraping
    
]
