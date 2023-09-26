from django.forms import forms
from .models import Cadastro
from django import forms

class CadastroNovo(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ('data','responsavel','descricao','tipo', 'valor')