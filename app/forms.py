from django.forms import ModelForm
from django import forms
from .models import Amazonia, Cerrado, Caatinga, Pampa, Pantanal, MataAtlantica

class UploadFileForm(forms.Form):
    file = forms.FileField()
    bioma = forms.ChoiceField(choices=[
        ('Amazonia', 'Amazonia'),
        ('Cerrado', 'Cerrado'),
        ('Caatinga', 'Caatinga'),
        ('Pampa', 'Pampa'),
        ('Pantanal', 'Pantanal'),
        ('MataAtlantica', 'Mata Atlantica')
    ])

class BiomaAmazoniaForm(ModelForm):
    class Meta:
        model = Amazonia
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCerradoForm(ModelForm):
    class Meta:
        model = Cerrado
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaCaatingaForm(ModelForm):
    class Meta:
        model = Caatinga
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPampaForm(ModelForm):
    class Meta:
        model = Pampa
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaPantanalForm(ModelForm):
    class Meta:
        model = Pantanal
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

class BiomaMataAtlanticaForm(ModelForm):
    class Meta:
        model = MataAtlantica
        fields = ['maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']