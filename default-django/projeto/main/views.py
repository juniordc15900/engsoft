from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from . import models
from django.core.mail import send_mail
from . import validator_forallz

def index(request):
    data = {}
    data['current_title'] = 'Menu'
    return render(request, 'mains/home1.html',data)

def registerAula(request):
    data = {}
    data['current_title'] = 'Registrar Aula'
    if request.method == 'POST':
        materia = request.POST.get("materia")
        date = request.POST.get("date")
        professor = request.POST.get("professor")
        nova_aula = models.Aula(
            materia=materia,
            date=date,
            professor=professor,
        )
        nova_aula.save()
        data['message'] = "Aula registrada com sucesso!"
        return render(request,'mains/registrar-aula.html',data)
    else:
        return render(request,'mains/registrar-aula.html',data)


def registerAtividade(request):
    data = {}
    data['current_title'] = 'Registrar Atividade'
    if request.method == 'POST':
        materia = request.POST.get("materia")
        questoes = request.POST.get("questoes")
        valor = request.POST.get("valor")
        professor = request.POST.get("professor")
        nova_atividade = models.Atividade(
            materia=materia,
            questoes=questoes,
            valor=valor,
            professor=professor,
        )
        nova_atividade.save()
        data['message'] = "Atividade registrada com sucesso!"
        return render(request,'mains/registrar-atividade.html',data)
    else:
        return render(request,'mains/registrar-atividade.html',data)

def listaAtividades(request):
    data = {}
    data['atividades'] = models.Atividade.objects.all()
    return render(request,'mains/listar-atividades.html',data)

def listaAulas(request):
    data = {}
    data['aulas'] = models.Aula.objects.all()
    return render(request,'mains/listar-aulas.html',data)

def delete(request,delete_type,delete_pk):
    data = {}
    if(delete_type == 'atividade'):
        op=1
        delete_atividade = models.Atividade.objects.get(pk=delete_pk)
        delete_atividade.delete() 
        

    elif(delete_type == 'aula'):
        op=2
        delete_aula = models.Aula.objects.get(pk=delete_pk)
        delete_aula.delete()

    else:
        print("Erro no sistema.")
    
    if op==1:
        render(request,'mains/listar-atividades.html',data)
        return redirect(listaAtividades)
    if op==2:
        render(request,'mains/listar-aulas.html',data)
        return redirect(listaAulas)

def edit(request,edit_type,edit_pk):
    data={}
    if(edit_type=='atividade'):
        op=1
        edit_atividade = models.Atividade.objects.get(pk=edit_pk)
        if request.method == 'POST':
            if 'edit' in request.POST:
                materia = request.POST.get("materia")
                questoes = request.POST.get("questoes")
                valor = request.POST.get("valor")
                professor = request.POST.get("professor")
                try:
                    edit_atividade.materia = materia
                    edit_atividade.questoes = questoes
                    edit_atividade.valor = valor
                    edit_atividade.professor = professor
                    edit_atividade.save()
                    data['tipo'] = op
                    render(request,'mains/listar-atividades.html',data)
                    return redirect(listaAtividades)
                except:
                    print("Deu erro na criação")    
            
    if(edit_type=='aula'):
        op=2
        edit_aula = models.Aula.objects.get(pk=edit_pk)
        if request.method == 'POST':
            if 'edit' in request.POST:
                materia = request.POST.get("materia")
                date = request.POST.get("date")
                professor = request.POST.get("professor")
                try:
                    edit_aula.materia = materia
                    edit_aula.date = date
                    edit_aula.professor = professor
                    edit_aula.save()
                    render(request,'mains/listar-aulas.html',data)
                    return redirect(listaAulas)
                except:
                    print("Deu erro na criação")  
    else:
        print("erro no sistema.")
    if op==1:
        data['tipo'] = op
    if op==2:
        data['tipo'] = op

    return render(request,'mains/edit.html',data)
           
    
def error_404(request, *args, **kwargs):
    data={}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request,'mains/404page1.html',data)