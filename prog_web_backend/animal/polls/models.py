from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    raca= models.CharField(max_length=200)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Tutor(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Atendimento(models.Model):
    relato = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)
    recomedacoes = models.CharField(max_length=200)
