from django import forms
from app.models import Categoria, Contato, Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormCategoria(forms.ModelForm):
    # especificar as config do modelo a ser utilizado
    class Meta:
        model = Categoria
        fields = ['nome']


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@email.com',
                'required': True
            })
        }

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem', 'quantidade', 'preco', 'categoria']

class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Nome', 'email': 'E-mail'}

class FormEditarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Nome', 'email': 'E-mail'}