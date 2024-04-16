from django.shortcuts import render
from .models import Formulario

def index(request):
    return render(request, 'formulario/index.html')
