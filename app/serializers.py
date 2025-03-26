from .models import BiomaAmazonia, BiomaCerrado, BiomaCaatinga, BiomaPampa, BiomaPantanal, BiomaMataAtlantica
from rest_framework import serializers

class BiomaAmazoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaAmazonia
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCerradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaCerrado
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCaatingaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaCaatinga
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPampaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaPampa
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPantanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaPantanal
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaMataAtlanticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomaMataAtlantica
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']