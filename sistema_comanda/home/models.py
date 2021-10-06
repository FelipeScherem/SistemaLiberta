from django.db import models

# Create your models here.
class bebida (models.Model):
    produto = models.CharField(max_length=30)
    preco = models.FloatField()


class comida (models.Model):
    produto = models.CharField(max_length=30)
    preco = models.FloatField()

class usuario (models.Model):
    nome = models.CharField(max_length=30)
    num = models.IntegerField()
    gasto = models.FloatField()
