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

def responder(request):
    respostas_usuario = []
    respostas_simulado = []
    # Arrumar em outro formato para organizar: questão, resposta do usuário e resposta correta em uma única estrutura por linha
    if request.POST:
        for pergunta, alternativa_escolhida in request.POST.items():
            if pergunta.startswith('pergunta_'):
                respostas_usuario.append(alternativa_escolhida)

        for p in perguntas:
            for resposta_correta in p['resposta']:
                respostas_simulado.append(resposta_correta)

    return render(request, 'pages/respostas.html', {'respostas_usuario': respostas_usuario, 'respostas_simulado': respostas_simulado})