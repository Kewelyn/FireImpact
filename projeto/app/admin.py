from django.contrib import admin
from .models import BiomaAmazonia, BiomaCerrado, BiomaCaatinga, BiomaPampa, BiomaPantanal, BiomaMataAtlantica

# Register your models here.

admin.site.register(BiomaAmazonia)
admin.site.register(BiomaCerrado)
admin.site.register(BiomaCaatinga)
admin.site.register(BiomaPampa)
admin.site.register(BiomaPantanal)
admin.site.register(BiomaMataAtlantica)
