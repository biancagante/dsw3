from django import forms
from app.models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira seu nome', 'required': True})
        }