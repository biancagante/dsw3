from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/iniciar-quiz', views.iniciarQuiz, name='iniciar-quiz')
]