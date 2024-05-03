from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('e-mail')
        usuario = request.POST.get('usuário')
        cria_senha = request.POST.get('senha')
        # confirma_senha = request.POST.get('confirme sua senha')
        new_form = User.objects.create_user(username=usuario, first_name=nome, last_name=sobrenome, email=email, password=cria_senha)
        # create não pede save

        return redirect('index')

    else:
        return render(request, 'registration/cadastro.html')


@login_required 
def index(request):
    # print(request.user, request.user.first_name, request.user.last_name)
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
        formulario = Formulario(nome=nome, descricao=descricao,author=author)
        formulario.save()
        return redirect('formulario_feito')
    else :
        return render(request, 'formulario/criar_formulario.html')
@login_required
def edita_formulario(request,id_formulario):
    form=get_object_or_404(Formulario,id=id_formulario)
    if request.method == 'POST':
        
        form.nome = request.POST.get('nome')
        form.descricao = request.POST.get('descricao')
        form.save()
        return redirect('index')
    else:
        return render(request, 'formulario/editar_formulario.html', {'formulario': form})

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
    
@login_required
def perguntas_de_texto(request):
    if request.method == 'POST':
        pergunta_de_texto = request.POST.get('pergunta de texto')
        tipo = 'texto'
        perguntas= Perguntas.objects.create(pergunta_de_texto=pergunta_de_texto, tipo=tipo)

        return redirect('perguntas_feitas')
    else :
        return render(request, 'perguntas/pergunta_de_texto.html')

@login_required
def listagem_perg_em_forms(request, id_formulario):
    perguntas = Perguntas.objects.all()
    formulario = Formulario.objects.get(id=id_formulario)
    relacoes = FormularioPergunta.objects.filter(formulario=formulario)
    ids_perguntas = []
    for rel in relacoes:
        ids_perguntas.append(rel.pergunta.id)

    return render(request, 'formulario/perguntas_form.html', {'perguntas_de_texto': perguntas, 'ids_perguntas': ids_perguntas, 'id_formulario':id_formulario})


def perguntas_de_intervalo(request):
    if request.method == 'POST':
        enunciado = request.POST.get('pergunta de intervalo')
        intervalo = request.POST.get('intervalo')
        tipo = 'intervalo'
        pergunta_de_intervalo = Perguntas.objects.create(pergunta_de_texto=enunciado, tipo=tipo)
        Intervalos.objects.create(enunciado_pergunta=pergunta_de_intervalo, intervalo=intervalo)
        return redirect('perguntas_feitas')
    else :
        return render(request, 'perguntas/pergunta_de_intervalo.html')


def seleciona_tipo(request):
    if request.method == 'POST':
        tipo_da_pergunta = request.POST.get('tipo da pergunta')
        if tipo_da_pergunta == 'texto':
            return redirect('pergunta_de_texto')
        elif tipo_da_pergunta == 'intervalo':  
            return redirect('pergunta_de_intervalo')

        return redirect('perguntas_feitas')
    else :
        return render(request, 'perguntas/tipo_da_pergunta.html')


@login_required
def perguntas_feitas(request):
   return render(request, 'perguntas/perguntas_feitas.html')

@login_required
def listagem_perguntas(request):
    perguntas = Perguntas.objects.all()
    return render(request, 'perguntas/listar_perguntas.html', {'perguntas_de_texto': perguntas})

# Função que adiciona pergunta ao formulário
def listagem_formularios(request, id_pergunta):
    if request.method == 'POST':
        all_forms = Formulario.objects.filter(author=request.user).order_by('-data_criacao')
        return render(request, 'formulario/adicionar_pergunta.html', {'formularios': all_forms, 'id_pergunta': id_pergunta})
    
def adicionar_pergunta(request):
    if request.method == 'POST':
        id_formulario = request.POST.get('id_formulario')
        id_pergunta = request.POST.get('id_pergunta')
        formulario = Formulario.objects.get(id=id_formulario)
        pergunta = Perguntas.objects.get(id=id_pergunta)
        FormularioPergunta.objects.create(formulario=formulario, pergunta=pergunta) 
        return redirect('perguntas_forms', id_formulario=id_formulario)
    else:
        return HttpResponseRedirect('/')

def listagem_perguntas(request):
    perguntas = Perguntas.objects.all()
    return render(request, 'perguntas/listar_perguntas.html', {'perguntas_de_texto': perguntas})

def deletar_perguntas(request,id_pergunta):
    perg=get_object_or_404(Perguntas,id=id_pergunta)

    perg.delete()
    return redirect('listagem_perguntas')


def editar_perguntas(request, id_pergunta):
    perg= get_object_or_404(Perguntas, id=id_pergunta)
    if request.method== 'POST':
        perg.pergunta_de_texto = request.POST.get('pergunta_de_texto')
        perg.save()
        return redirect('listagem_perguntas')
    else :
        return render(request,'perguntas/editar_pergunta.html', {'pergunta': perg})

def remover_pergunta (request) :
    if request.method == 'POST':
        id_formulario = request.POST.get('id_formulario')
        id_pergunta = request.POST.get('id_pergunta')
        formulario = Formulario.objects.get(id=id_formulario)
        pergunta = Perguntas.objects.get(id=id_pergunta)
        deletar = FormularioPergunta.objects.filter(formulario=formulario, pergunta=pergunta) 
        deletar.delete()
        return redirect('perguntas_forms', id_formulario=id_formulario)
    else:
        return HttpResponseRedirect('/')   