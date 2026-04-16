from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Simulado(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Historico(models.Model):
    pontuacao = models.IntegerField()
    realizado_em = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} — {self.simulado} ({self.realizado_em})"

class Pergunta(models.Model):
    enunciado = models.CharField(max_length=200)
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    alternativa = models.CharField(max_length=255)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pergunta} → {self.alternativa}"

class RespostaCorreta(models.Model):
    pergunta = models.OneToOneField(Pergunta, on_delete=models.CASCADE)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pergunta} ✓ {self.alternativa}"