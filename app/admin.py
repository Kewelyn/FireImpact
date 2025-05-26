from django.contrib import admin
from .models import Amazonia, Cerrado, Caatinga, Pampa, Pantanal, MataAtlantica

# Register your models here.

admin.site.register(Amazonia)
admin.site.register(Cerrado)
admin.site.register(Caatinga)
admin.site.register(Pampa)
admin.site.register(Pantanal)
admin.site.register(MataAtlantica)
