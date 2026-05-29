from django.urls import path
from .views import listar_livros, listar_clientes, listar_emprestimos


urlpatterns =  [
    path('livros/', listar_livros),
    path('clientes/', listar_clientes),
    path('emprestimos/', listar_emprestimos),
]


