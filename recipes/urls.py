from django.urls import path

from recipes.views import home

urlpatterns = [
    path('', home),  # Home
    # path('contato/', contato),  # Contato
    # path('sobre/', sobre),  # sobre
]
