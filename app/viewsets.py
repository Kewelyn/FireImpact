from rest_framework import viewsets
from .serializers import BiomaAmazoniaSerializer, BiomaCerradoSerializer, BiomaCaatingaSerializer, BiomaPampaSerializer, BiomaPantanalSerializer, BiomaMataAtlanticaSerializer
from .models import BiomaAmazonia, BiomaCerrado, BiomaCaatinga, BiomaPampa, BiomaPantanal, BiomaMataAtlantica

class BiomaAmazoniaViewSet(viewsets.ModelViewSet):
    model = BiomaAmazonia
    serializer_class = BiomaAmazoniaSerializer
    queryset = BiomaAmazonia.objects.all()
    filter_fields = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaCerradoViewSet(viewsets.ModelViewSet):
    model = BiomaCerrado
    serializer_class = BiomaCerradoSerializer
    queryset = BiomaCerrado.objects.all()
    filter_fields = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaCaatingaViewSet(viewsets.ModelViewSet):
    model = BiomaCaatinga
    serializer_class = BiomaCaatingaSerializer
    queryset = BiomaCaatinga.objects.all()
    filter_class = ('maxima','media','minima', 'anos','total', 'janeiro', 'fevereiro','marco', 'abril', 'maio',
                  'junho', 'julho','agosto','setembro','outubro','novembro','dezembro')

class BiomaPampaViewSet(viewsets.ModelViewSet):
    model = BiomaPampa
    serializer_class = BiomaPampaSerializer
    queryset = BiomaPampa.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

class BiomaPantanalViewSet(viewsets.ModelViewSet):
    model = BiomaPantanal
    serializer_class = BiomaPantanalSerializer
    queryset = BiomaPantanal.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


class BiomaMataAtlanticaViewSet(viewsets.ModelViewSet):
    model = BiomaMataAtlantica
    serializer_class = BiomaMataAtlanticaSerializer
    queryset = BiomaMataAtlantica.objects.all()
    filter_class = ('maxima', 'media', 'minima', 'anos', 'total', 'janeiro', 'fevereiro', 'marco', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


