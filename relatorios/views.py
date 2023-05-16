from django.shortcuts import render
from .forms import FormRelatorio
from django.http import HttpResponse


# Create your views here.
def novo_relatorio(request):
    if request.method == "GET":
        form = FormRelatorio()
        return render(request, 'novo_relatorio.html', {'form': form})
    elif request.method == "POST":
        form = FormRelatorio(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com Sucesso")
        else:
            return render(request, 'novo_relatorio.html', {'form': form})


def listar_relatorio(request):
    if request.method == "GET":
        return render(request, 'listar_relatorio.html')
