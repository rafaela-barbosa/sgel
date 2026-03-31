from django.contrib import admin
from .models import Cliente, Livro, Emprestimo

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Livro)
admin.site.register(Emprestimo)