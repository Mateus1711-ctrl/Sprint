from django.contrib import admin
from django.urls import include, path

from formulario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('deletar/<int:id_formulario>',views.deletar_formulario,name='deletar'),
    path('novo/', views.cria_formulario, name='criar_formulario'),
    path('formulario-feito/', views.formulario_feito, name='formulario_feito') ,
    path('cadastro/', views.cadastro , name='cadastro') ,
    path('perguntas/',views.perguntas,name='perguntas') ,
    path('perguntas-feitas/', views.perguntas_feitas, name='perguntas_feitas') ,
    path('listagem-perguntas/', views.listagem_perguntas, name='listagem_perguntas'),
    path('editar/<int:id_formulario>',views.edita_formulario,name='editar') ,
    path('deletar-pergunta/<int:id_pergunta>',views.deletar_perguntas,name='deletar_pergunta'),
    path('perguntas_forms/<int:id_formulario>', views.listagem_perg_em_forms, name='perguntas_forms')
]