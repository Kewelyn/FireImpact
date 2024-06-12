from django.urls import path, include
from rest_framework import routers
from .viewsets import BiomaAmazoniaViewSet, BiomaCerradoViewSet, BiomaCaatingaViewSet, BiomaPampaViewSet, BiomaPantanalViewSet, BiomaMataAtlanticaViewSet
from .views import home, listar_amazonia, listar_cerrado, listar_caatinga, listar_pampa, listar_pantanal, listar_atlantica, delete_amazonia, delete_cerrado, delete_caatinga, delete_pampa, delete_pantanal, delete_atlantica

router = routers.DefaultRouter()
router.register(r'biomaamazonia', BiomaAmazoniaViewSet, basename="BiomaAmazonia")
router.register(r'biomacerrado', BiomaCerradoViewSet, basename="BiomaCerrado")
router.register(r'biomacaatinga', BiomaCaatingaViewSet, basename="BiomaCaatinga")
router.register(r'biomapampa', BiomaPampaViewSet, basename="BiomaPampa")
router.register(r'biomapantanal', BiomaPantanalViewSet, basename="BiomaPantanal")
router.register(r'biomamataatlantica', BiomaMataAtlanticaViewSet, basename="BiomaMataAtlantica")


urlpatterns = [
    path('', home, name='home'),
    path('listar_amazonia', listar_amazonia, name='listar_amazonia'),
    path('listar_cerrado', listar_cerrado, name='listar_cerrado'),
    path('listar_caatinga', listar_caatinga, name='listar_caatinga'),
    path('listar_pampa', listar_pampa, name='listar_pampa'),
    path('listar_pantanal', listar_pantanal, name='listar_pantanal'),
    path('listar_atlantica', listar_atlantica, name='listar_atlantica'),
    path('delete_amazonia/<int:id>', delete_amazonia, name='delete_amazonia'),
    path('delete_cerrado/<int:id>', delete_cerrado, name='delete_cerrado'),
    path('delete_caatinga/<int:id>', delete_caatinga, name='delete_caatinga'),
    path('delete_pampa/<int:id>', delete_pampa, name='delete_pampa'),
    path('delete_pantanal/<int:id>', delete_pantanal, name='delete_pantanal'),
    path('delete_atlantica/<int:id>', delete_atlantica, name='delete_atlantica'),
    path('api/', include(router.urls)),
]