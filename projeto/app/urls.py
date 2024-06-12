from django.urls import path, include
from rest_framework import routers
from .viewsets import BiomaAmazoniaViewSet, BiomaCerradoViewSet, BiomaCaatingaViewSet, BiomaPampaViewSet, BiomaPantanalViewSet, BiomaMataAtlanticaViewSet
from .views import home, readBiomaAmazonia, readBiomaCerrado, readBiomaCaatinga, readBiomaPampa, readBiomaPantanal, readBiomaMataAtlantica, deleteBiomaAmazonia, deleteBiomaCerrado, deleteBiomaCaatinga, deleteBiomaPampa, deleteBiomaPantanal, deleteBiomaMataAtlantica

router = routers.DefaultRouter()
router.register(r'biomaamazonia', BiomaAmazoniaViewSet, basename="BiomaAmazonia")
router.register(r'biomacerrado', BiomaCerradoViewSet, basename="BiomaCerrado")
router.register(r'biomacaatinga', BiomaCaatingaViewSet, basename="BiomaCaatinga")
router.register(r'biomapampa', BiomaPampaViewSet, basename="BiomaPampa")
router.register(r'biomapantanal', BiomaPantanalViewSet, basename="BiomaPantanal")
router.register(r'biomamataatlantica', BiomaMataAtlanticaViewSet, basename="BiomaMataAtlantica")


urlpatterns = [
    path('', home, name='home'),
    path('readBiomaAmazonia', readBiomaAmazonia, name='readBiomaAmazonia'),
    path('readBiomaCerrado', readBiomaCerrado, name='readBiomaCerrado'),
    path('readBiomaCaatinga', readBiomaCaatinga, name='readBiomaCaatinga'),
    path('readBiomaPampa', readBiomaPampa, name='readBiomaPampa'),
    path('readBiomaPantanal', readBiomaPantanal, name='readBiomaPantanal'),
    path('readBiomaMataAtlantica', readBiomaMataAtlantica, name='readBiomaMataAtlantica'),
    path('deleteBiomaAmazonia/<int:id>', deleteBiomaAmazonia, name='deleteBiomaAmazonia'),
    path('deleteBiomaCerrado/<int:id>', deleteBiomaCerrado, name='deleteBiomaCerrado'),
    path('deleteBiomaCaatinga/<int:id>', deleteBiomaCaatinga, name='deleteBiomaCaatinga'),
    path('deleteBiomaPampa/<int:id>', deleteBiomaPampa, name='deleteBiomaPampa'),
    path('deleteBiomaPantanal/<int:id>', deleteBiomaPantanal, name='deleteBiomaPantanal'),
    path('deleteBiomaMataAtlantica/<int:id>', deleteBiomaMataAtlantica, name='deleteBiomaMataAtlantica'),
    path('api/', include(router.urls)),
]