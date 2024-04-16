from django.shortcuts import redirect, render
from .models import Formulario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required 
def index(request):
    # print(request.user, request.user.first_name, request.user.last_name)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        new_form = User.objects.create_user(nome=nome, password=senha)

        new_form.save()

        return redirect('index')
    else:
        all_forms = Formulario.objects.filter(author=request.user).order_by('-data_criacao')
        return render(request, 'formulario/index.html', {'notes': all_forms, 'user': request.user})




