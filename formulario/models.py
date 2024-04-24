from django.db import models

# Create your models here.
from django.db import models

class Formulario(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=2000, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Perguntas (models.Model):
    pergunta_de_texto = models.TextField(max_length=2000, blank=True, null=True)
    pergunta_intervalo = models.TextField(max_length=2000, blank=True, null=True)
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.pergunta_de_texto , self.pergunta_intervalo
    
class Intervalos(models.Model):
    
    intervalo = models.PositiveIntegerField()
    
    def __str__(self):
        return self.intervalo
    
class FormularioPergunta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    def __str__(self):
        return self.formulario.nome + ' - ' + self.pergunta.pergunta_de_texto
