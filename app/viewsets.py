from rest_framework import viewsets
from .serializers import BiomaAmazoniaSerializer, BiomaCerradoSerializer, BiomaCaatingaSerializer, BiomaPampaSerializer, BiomaPantanalSerializer, BiomaMataAtlanticaSerializer
from .models import Amazonia, Cerrado, Caatinga, Pampa, Pantanal, MataAtlantica

class BiomaAmazoniaViewSet(viewsets.ModelViewSet):
    model = Amazonia
    serializer_class = BiomaAmazoniaSerializer
    queryset = Amazonia.objects.all()
    filter_fields = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaCerradoViewSet(viewsets.ModelViewSet):
    model = Cerrado
    serializer_class = BiomaCerradoSerializer
    queryset = Cerrado.objects.all()
    filter_fields = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaCaatingaViewSet(viewsets.ModelViewSet):
    model = Caatinga
    serializer_class = BiomaCaatingaSerializer
    queryset = Caatinga.objects.all()
    filter_class = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaPampaViewSet(viewsets.ModelViewSet):
    model = Pampa
    serializer_class = BiomaPampaSerializer
    queryset = Pampa.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

class BiomaPantanalViewSet(viewsets.ModelViewSet):
    model = Pantanal
    serializer_class = BiomaPantanalSerializer
    queryset = Pantanal.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


class BiomaMataAtlanticaViewSet(viewsets.ModelViewSet):
    model = MataAtlantica
    serializer_class = BiomaMataAtlanticaSerializer
    queryset = MataAtlantica.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


