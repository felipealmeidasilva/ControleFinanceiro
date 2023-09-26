from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cadastro
from .forms import CadastroNovo
# Create your views here.

def cadastros(request):
    cadastros = Cadastro.objects.all()
    return render(request,'home.html', {'cadastros': cadastros})

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        form = CadastroNovo(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/')
            return render(request, 'cadastro.html')
        else:
            print('forms inválido')
            form = CadastroNovo()
        return render(request, 'cadastro.html', {'form': form})