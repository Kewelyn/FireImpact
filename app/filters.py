import django_filters

BIOMA_CHOICES = [
    ('Amazonia', 'Amazônia'),
    ('Cerrado', 'Cerrado'),
    ('Caatinga', 'Caatinga'),
    ('Pampa', 'Pampa'),
    ('Pantanal', 'Pantanal'),
    ('MataAtlantica', 'Mata Atlântica'),
]

class BiomaFilter(django_filters.FilterSet):
    Bioma = django_filters.ChoiceFilter(choices=BIOMA_CHOICES, label='Bioma')

    class Meta:
        model = None
        fields = ['Bioma']
