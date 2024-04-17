from django.contrib import admin
from django.urls import include, path

from formulario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('deletar/<int:id_formulario>',views.deletar_formulario,name='deletar'),
    path('novo/', views.cria_formulario, name='criar_formulario'),
    path('formulario-feito/', views.formulario_feito, name='formulario_feito')
]