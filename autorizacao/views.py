from django.shortcuts import render
from django.http import HttpResponse
from .models import Autorizacao


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

        autorizacao = Autorizacao.objects.filter(numero=numero)

        if autorizacao.exists():
            return HttpResponse('Autorização já existe')

        autorizacao = Autorizacao(
            categoria=categoria,
            tipo=tipo,
            numero=numero,
            emissao=emissao,
            validade=validade,
            proc_ADM=proc_ADM,
            tcaNum=tcaNum,
            compromitente=compromitente,
            cpfcnpj=cpfcnpj,
            insc_CAD=insc_CAD,
            endereco=endereco,
            quadra=quadra,
            lote=lote,
            bairro=bairro,
            area_lote=area_lote,
            sup_aut=sup_aut,
            matricula=matricula,
            anuencia_CETESB=anuencia_CETESB,
            anuencia_CONDEMA=anuencia_CONDEMA,
            compensacao_averbacao=compensacao_averbacao,
            observacao=observacao,
            objetivo=objetivo,
            local=local,
            nativos=nativos,
            exoticos=exoticos,
            euterpe=euterpe,
            transplante=transplante,
            vegetacao=vegetacao,
            estagio=estagio,
            area_aut=area_aut,
            recup_PRAD=recup_PRAD,
            app1=app1,
            app2=app2,
            reserva=reserva,
            restricao=restricao,
            area_rest=area_rest
        )

        autorizacao.save()

        return HttpResponse('tessteee-bancoo')
