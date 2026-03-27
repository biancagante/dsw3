from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome= models.CharField(max_length=100)
    

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=180)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return [self.nome, self.email, self.assunto, self.mensagem, self.data_envio]