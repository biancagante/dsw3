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
    respostas_simulado = []
    contadorAcertos = 0
    
    if request.method == "POST":
        for i, pergunta in enumerate(perguntas):
            resposta_usuario = request.POST.get(f'pergunta_{i}')
            resposta_correta = pergunta["resposta"]

            respostas_simulado.append({
                "pergunta": pergunta["enunciado"],
                "resposta_usuario": resposta_usuario,
                "resposta_correta": resposta_correta,
                "acertou": resposta_usuario == resposta_correta
            })

            if resposta_usuario == resposta_correta:
                contadorAcertos += 1

    return render(request, 'pages/respostas.html', {'respostas_simulado': respostas_simulado, 'contador': contadorAcertos})