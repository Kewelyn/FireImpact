from django.db import models

# Create your models here.
class BiomaAmazonia(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def  __str__(self):
        return self.total

class BiomaCerrado(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def __str__(self):
        return self.total

class BiomaCaatinga(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def __str__(self):
        return self.total

class BiomaPampa(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def __str__(self):
        return self.total

class BiomaPantanal(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def __str__(self):
        return self.total

class BiomaMataAtlantica(models.Model):
    maxima = models.CharField(max_length=40)
    media = models.IntegerField()
    minima = models.CharField(max_length=10)
    anos = models.CharField(max_length=11)
    total = models.CharField(max_length=8)
    janeiro = models.CharField(max_length=20)
    fevereiro = models.CharField(max_length=20)
    marco = models.CharField(max_length=80)
    abril = models.CharField(max_length=40)
    maio = models.CharField(max_length=15)
    junho = models.CharField(max_length=15)
    julho = models.CharField(max_length=15)
    agosto = models.CharField(max_length=15)
    setembro = models.CharField(max_length=15)
    outubro = models.CharField(max_length=15)
    novembro = models.CharField(max_length=15)
    dezembro = models.CharField(max_length=15)

    def __str__(self):
        return self.total