from django.shortcuts import render, redirect
from app.forms import FormUsuario
from app.models import Usuario, Simulado, Historico, Pergunta, Alternativa, RespostaCorreta
from app.lista import perguntas

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
    _perguntas = perguntas
        # for a in perguntas:
        #     _alternativas = a['alternativas']
    # _perguntas = perguntas
    # _alternativas = perguntas
    # _perguntas = Pergunta.objects.all().values()
    # _alternativas = Alternativa.objects.all().values()
    # 'alternativas': _alternativas
    return render(request, 'pages/simulado.html', {'perguntas': _perguntas})