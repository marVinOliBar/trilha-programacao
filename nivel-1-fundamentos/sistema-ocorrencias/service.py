import storage
from logica import (
    adicionar_ocorrencia,
    atualizar_ocorrencia,
)

def registrar_ocorrencia_service(ocorrencias, tipo, local, descricao):
    ocorrencia = adicionar_ocorrencia(ocorrencias, tipo, local, descricao)
    storage.salvar(ocorrencias)
    return ocorrencia

def editar_ocorrencia_service(ocorrencias, indice, novo_tipo, novo_local, nova_descricao):
    if not novo_tipo:
        print()
    elif not novo_local:
        print()
    elif nova_descricao:
        print()
    else:
        ocorrencia = atualizar_ocorrencia(ocorrencias, indice, novo_tipo, novo_local, nova_descricao)
        storage.salvar(ocorrencias)
        return (True, ocorrencia)
        
