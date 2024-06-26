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
    pergunta_de_texto = models.TextField(max_length=2000, blank=True, null=True) ## classe para todos os tipos de pergunta (nome da variável está específico, mas devemos ignorar, só não trocamos porque ia quebrar todo o dódigo - ficaria melhor: 'pergunta')
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.pergunta_de_texto
    
class Intervalos(models.Model):
    enunciado_pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    intervalo = models.PositiveIntegerField()
    
    def __str__(self):
        return self.intervalo
    
class FormularioPergunta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    def __str__(self):
        return self.formulario.nome + ' - ' + self.pergunta.pergunta_de_texto
