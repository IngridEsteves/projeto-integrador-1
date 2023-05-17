from django.shortcuts import render, get_object_or_404
from .forms import FormRelatorio
from django.http import HttpResponse, FileResponse
from .models import Relatorio
from fpdf import FPDF
from io import BytesIO


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


def baixar_os(request, identificador):
    relatorio = get_object_or_404(Relatorio, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240, 240, 240)
    pdf.cell(35, 10, 'Título:', 1, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(0, 10, f'{relatorio.titulo}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Relatórios:', 1, 0, 'L', 1)
    categorias_relatorio = relatorio.categoria_relatorio.all()
    for i, relatoriox in enumerate(categorias_relatorio):
        pdf.cell(0, 10, f' - {relatoriox.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_relatorio) - 1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(35, 10, 'Data Geração:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{relatorio.data_geracao}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{relatorio.protocolo}', 1, 1, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin1')  # Salvar o pdf em memória
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os_{relatorio.titulo}.pdf")
