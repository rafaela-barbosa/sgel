from django.http import JsonResponse
from .models import Cliente, Livro, Emprestimo

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all().values()
    return JsonResponse(list(livros, safe=False))

def listar_clientes(request):
    clientes = Cliente.objects.all().values()
    return JsonResponse(list(clientes, safe=False))

def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all().values()
    return JsonResponse(list(emprestimos, safe=False))


