from django.shortcuts import render, redirect

def home(request):
    return render(request, 'pages/home.html')

def iniciarQuiz(request):
    return render(request, 'pages/iniciar-quiz.html')