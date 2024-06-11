from django.forms import ModelForm
from .models import BiomaAmazonia, BiomaCerrado, BiomaCaatinga, BiomaPampa, BiomaPantanal, BiomaMataAtlantica

class BiomaAmazoniaForm(ModelForm):
    class Meta:
        model = BiomaAmazonia
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCerradoForm(ModelForm):
    class Meta:
        model = BiomaCerrado
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCaatingaForm(ModelForm):
    class Meta:
        model = BiomaCaatinga
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPampaForm(ModelForm):
    class Meta:
        model = BiomaPampa
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPantanalForm(ModelForm):
    class Meta:
        model = BiomaPantanal
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaMataAtlanticaForm(ModelForm):
    class Meta:
        model = BiomaMataAtlantica
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']