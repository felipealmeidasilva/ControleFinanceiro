from django.shortcuts import render
from home.forms import CadastroNovo

# Create your views here.
def cadastro(request):
        form = CadastroNovo(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/')
            return render(request, 'cadastro.html')
        else:
            form = CadastroNovo()
        return render(request, 'cadastro.html', {'form': form})