from django.db import models
# Paginas do Site
class HomePage(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

#classes

class Aula(models.Model):
    materia = models.CharField(max_length=100)
    date = models.DateField()
    professor = models.CharField(max_length=100)

class Atividade(models.Model):
    materia = models.CharField(max_length=100)
    questoes = models.BigIntegerField()
    valor = models.BigIntegerField()
    professor = models.CharField(max_length=100)