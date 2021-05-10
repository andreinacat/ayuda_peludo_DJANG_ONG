from django.contrib import admin
from django.urls import path
from .views import index,gatitos, perritos, registro

urlpatterns = [
    
    path('',index,name='IND'),
    path('perros/',perritos,name='perros'),
    path('gatos/',gatitos,name='gatos'),
    path('registro/',registro,name='REG'),
    
]