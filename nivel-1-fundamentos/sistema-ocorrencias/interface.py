import storage
from logica import (
    buscar_ocorrencias,
    excluir_ocorrencia,
)
from service import (
    registrar_ocorrencia_service,
    editar_ocorrencia_service,
)

def verificar_lista_vazia(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return True
    return False

def registrar_ocorrencia(ocorrencias):
    tipo = input("Digite o tipo da ocorrência: ").strip().lower()
    local = input("Digite o local da ocorrência: ").strip().lower()
    descricao = input("Digite a descrição da ocorrência: ").strip().lower()

    ocorrencia = registrar_ocorrencia_service(ocorrencias, tipo, local, descricao)
        
    print(f"Ocorrência registrada: {ocorrencia['tipo']} - {ocorrencia['local']} - {ocorrencia['descricao']}")

def listar_ocorrencias(ocorrencias):
    if verificar_lista_vazia(ocorrencias):
        return

    for i, ocorrencia in enumerate(ocorrencias, start=1):
        print(f"Talão {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")
        print("===============")

def pesquisar_ocorrencias(ocorrencias):
    if verificar_lista_vazia(ocorrencias):
        return

    termo = input("Digite o termo que deseja buscar: ").lower().strip()

    resultado = buscar_ocorrencias(ocorrencias, termo)

    if resultado:
        for i, ocorrencia in resultado:
            print(f"ID {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")
    else:
        print("Não foram encontradas ocorrências!")

def remover_ocorrencia(ocorrencias):
    if verificar_lista_vazia(ocorrencias):
        return

    for i, ocorrencia in enumerate(ocorrencias, start=1):
        print(f"{i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")

    try:
        opcao = int(input("Digite o número da ocorrência que deseja remover: "))
    except ValueError:
        print("Digite apenas números!")
        return

    if opcao < 1 or opcao > len(ocorrencias):
        print("Opção inválida!")
        return

    indice = opcao - 1

    removido = excluir_ocorrencia(ocorrencias, indice)

    storage.salvar(ocorrencias)
    
    print(f"Ocorrência removida: {removido['tipo']} - {removido['local']}")

def editar_ocorrencia(ocorrencias):

    if verificar_lista_vazia(ocorrencias):
        return

    for i, ocorrencia in enumerate(ocorrencias, start = 1):
        print(f"ID: {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas números!")
        return

    if opcao < 1 or opcao > len(ocorrencias):
        print("Digite um ID válido!")
        return

    indice = opcao - 1
    ocorrencia = ocorrencias[indice]

    novo_tipo = input(f"Descreva o novo tipo para [{ocorrencia['tipo']}]: ").strip().lower()
    novo_local = input(f"Descreva o novo local para [{ocorrencia['local']}]: ").strip().lower()
    nova_descricao = input(f"Descreva a nova descrição para [{ocorrencia['descricao']}]: ").strip().lower()

    ocorrencia_atualizada = editar_ocorrencia_service(ocorrencias, indice, novo_tipo, novo_local, nova_descricao)
  
    print(f"Ocorrência editada: {ocorrencia_atualizada['tipo']} - {ocorrencia_atualizada['local']} - {ocorrencia_atualizada['descricao']}")
