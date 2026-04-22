from logica import (
    criar_ocorrencia
)

def registrar_ocorrencia_service(ocorrencias, fire_trucks, tipo, local, descricao, unit_number):
    if not tipo or not local or not descricao or not unit_number:   
        return (False, "Os campos não podem ficar em branco!")

    result = False
    
    for truck in fire_trucks:
        if unit_number == truck['prefixo'] and truck['situacao'] == 'ativa':
            result = True
    
    if not result:
        return (False, "Digitar uma viatura válida!")
    
    dado = criar_ocorrencia(ocorrencias, tipo, local, descricao, unit_number)
    storage.save(ocorrencias)
    return (True, dado)
        