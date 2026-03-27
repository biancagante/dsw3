from django import forms
from app.models import Categoria, Contato

class FormCategoria(forms.ModelForm):
    # especificar as config do modelo a ser utilizado
    class Meta():
        model = Categoria
        fields = ['nome']

class FormContato(forms.ModelForm):
    class Meta():
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@email.com',
                'required': True
            })
        }