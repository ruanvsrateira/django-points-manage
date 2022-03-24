from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Participantes

def index_page(req):
    participantes = Participantes.objects.all().order_by('pontuacao').reverse()

    return render(req, 'index.html', {"participantes": participantes})

def add_aluno_page(req):
    
    return render(req, 'add_aluno.html')

def add_aluno_view(req):
    
    nome = req.POST.get('nome')
    pontos = req.POST.get('pontos_iniciais')

    participantes = Participantes(nome=nome, pontuacao=pontos)
    participantes.save()

    return redirect('/')

def remover_aluno_page(req):
    participantes = Participantes.objects.all().order_by('pontuacao').reverse()

    return render(req, 'remover_aluno.html', {"participantes": participantes})

def remover_aluno_view(req):
    aluno = Participantes.objects.filter(nome=req.POST.get('option_delete_aluno'))

    aluno.delete()

    return redirect('/')

def menos_um_ponto(req, id):
    participante = get_object_or_404(Participantes, pk=id)

    participante.pontuacao = participante.pontuacao - 1
    participante.save()

    return redirect('/')

def mais_um_ponto(req, id):
    participante = get_object_or_404(Participantes, pk=id)

    participante.pontuacao = participante.pontuacao + 1
    participante.save()

    return redirect('/')