from .models import Amazonia, Cerrado, Caatinga, Pampa, Pantanal, MataAtlantica
from rest_framework import serializers

class BiomaAmazoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amazonia
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCerradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerrado
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCaatingaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caatinga
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPampaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pampa
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPantanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantanal
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaMataAtlanticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataAtlantica
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']