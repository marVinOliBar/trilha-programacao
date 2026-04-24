import storage

from logica import (
    criar_ocorrencia,
    filtrar_viaturas_elegiveis,
)

def registrar_ocorrencia_service(ocorrencias, fire_trucks, tipo, local, descricao, unit_number):
    if not tipo or not local or not descricao or not unit_number:   
        return (False, "Os campos não podem ficar em branco!")

    elegiveis = filtrar_viaturas_elegiveis(fire_trucks)

    if not elegiveis:
        return (False, "Não há viaturas na Ativa ou na Reserva!")
  
    encontrado = False
    for elegivel in elegiveis:
        if unit_number == elegivel['prefixo'].upper():
            encontrado = True

    if not encontrado:
        return (False, "Viatura não está Ativa ou na Reserva!")

    dado = criar_ocorrencia(ocorrencias, tipo, local, descricao, unit_number)
    storage.salvar("ocorrencias.json", ocorrencias)
    return (True, dado)