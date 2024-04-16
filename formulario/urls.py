from django.contrib import admin
from django.urls import include, path

from formulario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.cria_formulario, name='criar_formulario'),
    path('formulario-feito/', views.formulario_feito, name='formulario_feito')
]