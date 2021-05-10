from django.contrib import admin
from django.urls import path
from .views import index,gatitos, perritos, registro, ficha, filtro_categoria, filtro_descripcion

urlpatterns = [
    
    path('',index,name='IND'),
    path('perros/',perritos,name='perros'),
    path('gatos/',gatitos,name='gatos'),
    path('filtro_d',filtro_descripcion,name='FILTROD'),
    path('registro/',registro,name='REG'),
    path('ficha/<id>/',ficha,name='FICHA'),
    path('filtro_c/',filtro_categoria,name='FILTROC'),
    
]