from django.urls import path
from .views import listar_livros
from .views import listar_clientes

urlpatterns =  [
    path('livros/', listar_livros),
    path('clientes/', listar_clientes),
]


