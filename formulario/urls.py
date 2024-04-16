from django.contrib import admin
from django.urls import include, path

from formulario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
    # path('novo/', views.novo_formulario, name='novo_formulario')
]