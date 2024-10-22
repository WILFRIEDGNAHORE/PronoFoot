from django.urls import path
from . import views

urlpatterns = [
    path('', views.football_pronostics_view, name='football_pronostics'),
]
