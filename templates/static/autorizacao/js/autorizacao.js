console.log('teste')

function exibir_formulario(tipo){
    add_autorizacao = document.getElementById('adicionar-autorizacao')
    att_autorizacao = document.getElementById('atualizar-autorizacao')
    if(tipo=="1"){
        att_autorizacao.style.display="none"
        add_autorizacao.style.display="block"
    }else if(tipo=="2"){
        add_autorizacao.style.display="none"
        att_autorizacao.style.display="block"
    }
    
}

function dados_autorizacao(){
    autorizacao = document.getElementById('autorizacao-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_autorizacao = autorizacao.value

    data = new FormData()
    data.append('id_autorizacao', id_autorizacao)

    fetch("/autorizacao/atualiza_autorizacao/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        document.getElementById('form-att-autorizacao').style.display='block'

        categoria = document.getElementById('categoria')
        categoria.value = data['categoria']

        tipo = document.getElementById('tipo')
        tipo.value = data['tipo']

        numero = document.getElementById('numero')
        numero.value = data['numero']

        emissao = document.getElementById('emissao')
        emissao.value = data['emissao']

        validade = document.getElementById('validade')
        validade.value = data['validade']

        proc_ADM = document.getElementById('proc_ADM')
        proc_ADM.value = data['proc_ADM']

        tcaNum = document.getElementById('tcaNum')
        tcaNum.value = data['tcaNum']

        compromitente = document.getElementById('compromitente')
        compromitente.value = data['compromitente']

        cpfcnpj = document.getElementById('cpfcnpj')
        cpfcnpj.value = data['cpfcnpj']

        insc_CAD = document.getElementById('insc_CAD')
        insc_CAD.value = data['insc_CAD']

        endereco = document.getElementById('endereco')
        endereco.value = data['endereco']

        quadra = document.getElementById('quadra')
        quadra.value = data['quadra']

        lote = document.getElementById('lote')
        lote.value = data['lote']

        bairro = document.getElementById('bairro')
        bairro.value = data['bairro']

        area_lote = document.getElementById('area_lote')
        area_lote.value = data['area_lote']

        sup_aut = document.getElementById('sup_aut')
        sup_aut.value = data['sup_aut']

        matricula = document.getElementById('matricula')
        matricula.value = data['matricula']

        anuencia_CETESB = document.getElementById('anuencia_CETESB')
        anuencia_CETESB.value = data['anuencia_CETESB']

        anuencia_CONDEMA = document.getElementById('anuencia_CONDEMA')
        anuencia_CONDEMA.value = data['anuencia_CONDEMA']

        compensacao_averbacao = document.getElementById('compensacao_averbacao')
        compensacao_averbacao.value = data['compensacao_averbacao']

        observacao = document.getElementById('observacao')
        observacao.value = data['observacao']

        objetivo = document.getElementById('objetivo')
        objetivo.value = data['objetivo']

        local = document.getElementById('local')
        local.value = data['local']

        nativos = document.getElementById('nativos')
        nativos.value = data['nativos']

        exoticos = document.getElementById('exoticos')
        exoticos.value = data['exoticos']

        euterpe = document.getElementById('euterpe')
        euterpe.value = data['euterpe']

        transplante = document.getElementById('transplante')
        transplante.value = data['transplante']

        vegetacao = document.getElementById('vegetacao')
        vegetacao.value = data['vegetacao']

        estagio = document.getElementById('estagio')
        estagio.value = data['estagio']

        area_aut = document.getElementById('area_aut')
        area_aut.value = data['area_aut']

        recup_PRAD = document.getElementById('recup_PRAD')
        recup_PRAD.value = data['recup_PRAD']

        app1 = document.getElementById('app1')
        app1.value = data['app1']

        app2 = document.getElementById('app2')
        app2.value = data['app2']

        reserva = document.getElementById('reserva')
        reserva.value = data['reserva']

        restricao = document.getElementById('restricao')
        restricao.value = data['restricao']

        area_rest = document.getElementById('area_rest')
        area_rest.value = data['area_rest']
    })

}
