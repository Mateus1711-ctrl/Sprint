from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
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
        print(all_forms)
        return render(request, 'formulario/index.html', {'formularios': all_forms, 'user': request.user})

@login_required 
def cria_formulario(request) :
    if request.method == 'POST' :
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        pergunta = request.POST.get('pergunta')
        author=request.user
        formulario = Formulario(nome=nome, descricao=descricao, pergunta=pergunta,author=author)
        formulario.save()
        return redirect('formulario_feito')
    else :
        return render(request, 'formulario/criar_formulario.html')
    
def edita_formulario(request):
    if request.method == 'POST':
        id_formulario = request.POST.get('id_formulario')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        pergunta = request.POST.get('pergunta')
        formulario = Formulario.objects.get(id=id_formulario)
        formulario.nome = nome
        formulario.descricao = descricao
        formulario.pergunta = pergunta
        formulario.save()
        return redirect('index')
    else:
        id_formulario = request.GET.get('id_formulario')
        formulario = Formulario.objects.get(id=id_formulario)
        return render(request, 'formulario/editar_formulario.html', {'formulario': formulario})

@login_required 
def formulario_feito(request) :
    return render(request, 'formulario/formulario_feito.html')

def deletar_formulario(request,id_formulario):
    form=get_object_or_404(Formulario,id=id_formulario)
    if request.method=='POST':
        form.delete()
        return redirect('index')
    else:
        return HttpResponseRedirect('/')
    