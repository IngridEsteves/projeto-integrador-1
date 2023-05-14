from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def autorizacao(request):
    if request.method == "GET":
        return render(request, 'autorizacao.html')
    elif request.method == "POST":
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
        emissao = request.POST.get('emissao')
        validade = request.POST.get('validade')
        proc_ADM = request.POST.get('proc_ADM')
        tcaNum = request.POST.get('tcaNum')
        compromitente = request.POST.get('compromitente')
        cpfcnpj = request.POST.get('cpfcnpj')
        insc_CAD = request.POST.get('insc_CAD')
        endereco = request.POST.get('endereco')
        quadra = request.POST.get('quadra')
        lote = request.POST.get('lote')
        bairro = request.POST.get('bairro')
        area_lote = request.POST.get('area_lote')
        sup_aut = request.POST.get('sup_aut')
        matricula = request.POST.get('matricula')
        anuencia_CETESB = request.POST.get('anuencia_CETESB')
        anuencia_CONDEMA = request.POST.get('anuencia_CONDEMA')
        compensacao_averbacao = request.POST.get('compensacao_averbacao')
        observacao = request.POST.get('observacao')
        objetivo = request.POST.get('objetivo')
        local = request.POST.get('local')
        nativos = request.POST.get('nativos')
        exoticos = request.POST.get('exoticos')
        euterpe = request.POST.get('euterpe')
        transplante = request.POST.get('transplante')
        vegetacao = request.POST.get('vegetacao')
        estagio = request.POST.get('estagio')
        area_aut = request.POST.get('area_aut')
        recup_PRAD = request.POST.get('recup_PRAD')
        app1 = request.POST.get('app1')
        app2 = request.POST.get('app2')
        reserva = request.POST.get('reserva')
        restricao = request.POST.get('restricao')
        area_rest = request.POST.get('area_rest')
        
        return HttpResponse('tessteee')

