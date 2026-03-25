import storage
from logica import (
    adicionar_ocorrencia,
    atualizar_ocorrencia,
    excluir_ocorrencia,
)

def registrar_ocorrencia_service(ocorrencias, tipo, local, descricao):
    if not tipo: # if tipo == "":
        return (False, "Erro! O campo tipo deve ser preenchido.")
    if not local:
        return (False, "Erro! O campo local deve ser preenchido.")
    if not descricao:
        return (False, "Erro! O campo descrição deve ser preenchido.")
    else:
        ocorrencia = adicionar_ocorrencia(ocorrencias, tipo, local, descricao)
        storage.salvar(ocorrencias)
        return (True, ocorrencia)

def editar_ocorrencia_service(ocorrencias, indice, novo_tipo, novo_local, nova_descricao):
    if not novo_tipo:
        return (False, "Erro! O campo tipo deve ser preenchido.")
    elif not novo_local:
        return (False, "Erro! O campo local deve ser preenchido.")
    elif not nova_descricao:
        return (False, "Erro! O campo descrição deve ser preenchido.")
    else:
        ocorrencia = atualizar_ocorrencia(ocorrencias, indice, novo_tipo, novo_local, nova_descricao)
        storage.salvar(ocorrencias)
        return (True, ocorrencia)

def remover_ocorrencia_service(ocorrencias, indice):

	if indice < 0 or indice >= len(ocorrencias):
		return (False, "Escolher uma ocorrências válida")
	else:
		removido = excluir_ocorrencia(ocorrencias, indice)
		storage.salvar(ocorrencias)
		return (True, removido)



        
