from django.db import models

# Create your models here.
from django.db import models

class Formulario(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=2000, blank=True, null=True)
    pergunta = models.CharField(max_length=2000, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    