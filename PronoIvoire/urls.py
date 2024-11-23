from django.urls import path
from . import views  # Remplace 'your_app' par le nom de ton application

urlpatterns = [
    path('', views.home, name='home'),
    path('pronostics-football-aujourdhui/', views.display_pronostics_aujourdhui, name='display_pronostics_aujourdhui'), 
    path('pronostics-football-pour-demain/', views.display_pronostics_Demain, name='display_pronostics_Demain'),
    path('les-meilleurs-pronostics-foot-du-jour/', views.display_pronostics_Meilleur, name='display_pronostics_Meilleur'),
    
]
