from django.shortcuts import render, get_object_or_404
from .forms import FormRelatorio
from django.http import HttpResponse
from .models import Relatorio


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
        relatorios = Relatorio.objects.all()
        return render(request, 'listar_relatorio.html', {'relatorios': relatorios})


def relatorio(request, identificador):
    relatorio = get_object_or_404(Relatorio, identificador=identificador)
    return render(request, 'relatorio.html', {'relatorio': relatorio})
