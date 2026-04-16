from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('iniciar-quiz', views.iniciarQuiz, name='iniciarQuiz'),
    path('quiz', views.perguntar, name='perguntar'),
    path('respostas', views.responder, name='respostas')
]