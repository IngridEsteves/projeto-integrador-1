from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Autorizacao
from django.core import serializers
import json
from django.shortcuts import get_object_or_404


# Create your views here.
def autorizacao(request):
    if request.method == "GET":
        autorizacoes_list = Autorizacao.objects.all()
        return render(request, 'autorizacao.html', {'autorizacoes': autorizacoes_list})
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
            area_rest=area_rest,
        )

        autorizacao.save()

        return HttpResponse('tessteee-bancoo')


def att_autorizacao(request):
    id_autorizacao = request.POST.get('id_autorizacao')
    autorizacao = Autorizacao.objects.filter(id=id_autorizacao)
    autorizacao_json = json.loads(serializers.serialize('json', autorizacao))[0]['fields']
    autorizacao_id = json.loads(serializers.serialize('json', autorizacao))[0]['pk']
    data = {'autorizacao': autorizacao_json, 'autorizacao_id': autorizacao_id}
    return JsonResponse(data)


def update_autorizacao(request, id):
    body = json.loads(request.body)

    categoria = body['categoria']
    tipo = body['tipo']
    numero = body['numero']
    emissao = body['emissao']
    validade = body['validade']
    proc_ADM = body['proc_ADM']
    tcaNum = body['tcaNum']
    compromitente = body['compromitente']
    cpfcnpj = body['cpfcnpj']
    insc_CAD = body['insc_CAD']
    endereco = body['endereco']
    quadra = body['quadra']
    lote = body['lote']
    bairro = body['bairro']
    area_lote = body['area_lote']
    sup_aut = body['sup_aut']
    matricula = body['matricula']
    anuencia_CETESB = body['anuencia_CETESB']
    anuencia_CONDEMA = body['anuencia_CONDEMA']
    compensacao_averbacao = body['compensacao_averbacao']
    observacao = body['observacao']
    objetivo = body['objetivo']
    local = body['local']
    nativos = body['nativos']
    exoticos = body['exoticos']
    euterpe = body['euterpe']
    transplante = body['transplante']
    vegetacao = body['vegetacao']
    estagio = body['estagio']
    area_aut = body['area_aut']
    recup_PRAD = body['recup_PRAD']
    app1 = body['app1']
    app2 = body['app2']
    reserva = body['reserva']
    restricao = body['restricao']
    area_rest = body['area_rest']

    autorizacao = get_object_or_404(Autorizacao, id=id)
    try:
        autorizacao.categoria = categoria
        autorizacao.tipo = tipo
        autorizacao.numero = numero
        autorizacao.emissao = emissao
        autorizacao.validade = validade
        autorizacao.proc_ADM = proc_ADM
        autorizacao.tcaNum = tcaNum
        autorizacao.compromitente = compromitente
        autorizacao.cpfcnpj = cpfcnpj
        autorizacao.insc_CAD = insc_CAD
        autorizacao.endereco = endereco
        autorizacao.quadra = quadra
        autorizacao.lote = lote
        autorizacao.bairro = bairro
        autorizacao.area_lote = area_lote
        autorizacao.sup_aut = sup_aut
        autorizacao.matricula = matricula
        autorizacao.anuencia_CETESB = anuencia_CETESB
        autorizacao.anuencia_CONDEMA = anuencia_CONDEMA
        autorizacao.compensacao_averbacao = compensacao_averbacao
        autorizacao.observacao = observacao
        autorizacao.objetivo = objetivo
        autorizacao.local = local
        autorizacao.nativos = nativos
        autorizacao.exoticos = exoticos
        autorizacao.euterpe = euterpe
        autorizacao.transplante = transplante
        autorizacao.vegetacao = vegetacao
        autorizacao.estagio = estagio
        autorizacao.area_aut = area_aut
        autorizacao.recup_PRAD = recup_PRAD
        autorizacao.app1 = app1
        autorizacao.app2 = app2
        autorizacao.reserva = reserva
        autorizacao.restricao = restricao
        autorizacao.area_rest = area_rest
        autorizacao.save()
        return JsonResponse({'status': '200', 'numero': numero})
    except KeyError:
        return JsonResponse({'status': '500'})


def listar_autorizacao(request):
    if request.method == "GET":
        autorizacoes = Autorizacao.objects.all()
        return render(request, 'listar_autorizacao.html', {'autorizacoes': autorizacoes})


def autorizacao_list(request, id):
    autorizacao = get_object_or_404(Autorizacao, id=id)
    return render(request, 'autorizacao_list.html', {'autorizacao': autorizacao})


def baixar(request, id):
    relatorio = get_object_or_404(Autorizacao, id=id)

    return HttpResponse('TESTEEEE')