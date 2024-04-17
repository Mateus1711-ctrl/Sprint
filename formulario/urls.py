from django.contrib import admin
from django.urls import include, path

from formulario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formularios/<int:note_id>', views.editar, name='editar'),
    # path('novo/', views.novo_usuario, name='novo_formulario')
]