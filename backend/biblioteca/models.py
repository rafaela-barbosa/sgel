from django.db import models

# Create your models here.

class Livro(models.Model):
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('DISPONIVEL', 'Disponivel'),
    ]
    titulo = models.CharField(max_length=200, verbose_name="Título do Livro")
    autor = models.CharField(max_length=200, verbose_name="Autor do Livro")
    isbn = models.CharField(max_length=50, unique=True, verbose_name="ISBN")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='DISPONIVEL')
    qtd_estoque = models.IntegerField(max_length=50, unique=True, verbose_name="Quantidade em estoque")

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome e Sobrenome")
    email = models.CharField(max_length=200, verbose_name="Email")
    tel = models.CharField(max_length=50, unique=True, verbose_name="Telefone")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, verbose_name="Livro")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, verbose_name="Responsável")
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_prev_dev = models.DateTimeField(verbose_name="Previsao Devolucao")
    data_devolucao = models.DateTimeField(null=True, blank=True, verbose_name="Data Devolução")


    def __str__(self):
        status = 'Emprestado' if not self.data_devolucao else 'Devolvido'
        return f'{self.cliente.nome} - {self.livro.titulo} ({status})'
    
    def save(self, *args, **kwargs):
        if not self.data_devolucao:
            self.livro.status = 'EMPRESTADO'
            
        else:
            self.livro.status = 'DISPONIVEL'
          

        self.livro.save()
        super().save(*args, **kwargs)
