from django.shortcuts import render, redirect
from app.forms import FormUsuario
from app.models import Usuario, Simulado, Historico, Pergunta, Alternativa, RespostaCorreta

def home(request):
    return render(request, 'pages/home.html')

def iniciarQuiz(request):
    formulario = FormUsuario(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            # formulario.save()
            return redirect('/quiz')
    return render(request, 'pages/iniciar-quiz.html', {'form': formulario})

def perguntar(request):
    _perguntas = Pergunta.objects.all().values()
    _alternativas = Alternativa.objects.all().values()
    return render(request, 'pages/simulado.html', {'perguntas': _perguntas, 'alternativas': _alternativas})