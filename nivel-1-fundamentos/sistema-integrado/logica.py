def criar_ocorrencia (ocorrencias, tipo, local, descricao, unit_number):
    ocorrencia = {
        'tipo' : tipo,
        'local' : local,
        'descricao' : descricao,
        'prefixo' : unit_number,
    }
    
    ocorrencias.append(ocorrencia)
    return ocorrencia

def filtrar_viaturas_elegiveis(fire_trucks):
    viaturas_elegiveis = []
    for truck in fire_trucks:
        if truck['situacao'].upper() in ('ATIVA', 'RESERVA'):
            viaturas_elegiveis.append(truck)
    
    return viaturas_elegiveis

def listar_prefixos_viaturas(ocorrencias):
    conjunto_prefixos = set()
    for ocorrencia in ocorrencias:
        conjunto_prefixos.add(ocorrencia['prefixo'])
    lista_prefixos = list(conjunto_prefixos)
    return lista_prefixos

def ocorrencia_prefixo_selecionado(ocorrencias, opcao):
    ocorrencias_filtradas = []
    for ocorrencia in ocorrencias:
        if opcao.upper() == ocorrencia['prefixo'].upper():
            ocorrencias_filtradas.append(ocorrencia)
    return ocorrencias_filtradas