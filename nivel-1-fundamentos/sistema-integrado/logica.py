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