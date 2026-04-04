from service import (
    registrar_ocorrencia_service,
    editar_ocorrencia_service,
    remover_ocorrencia_service,
    pesquisar_ocorrencia_service,
    listar_ocorrencias_service,
)
def registrar_ocorrencia(ocorrencias):
    tipo = input("Digite o tipo da ocorrência: ").strip().lower()
    local = input("Digite o local da ocorrência: ").strip().lower()
    descricao = input("Digite a descrição da ocorrência: ").strip().lower()
    sucesso, dado = registrar_ocorrencia_service(ocorrencias, tipo, local, descricao)
    if sucesso:
        ocorrencia = dado
        print(f"Ocorrência registrada: {ocorrencia['tipo']} - {ocorrencia['local']} - {ocorrencia['descricao']}")
    else:
        print(dado)
def listar_ocorrencias(ocorrencias):
    sucesso, dados = listar_ocorrencias_service(ocorrencias)
    if sucesso:
        for i, dado in enumerate(dados, start=1):
            print(f"Talão {i} - Tipo: {dado['tipo']} - Local: {dado['local']} - Descrição: {dado['descricao']}")
            print("===============")
    else:
        print(dados)
def pesquisar_ocorrencias(ocorrencias):
    termo = input("Digite o termo que deseja buscar: ").lower().strip()
    sucesso, resultado = pesquisar_ocorrencia_service(ocorrencias, termo)
    if sucesso:
        for i, ocorrencia in resultado:
            print(f"ID {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")
    else:
        print(resultado)
def remover_ocorrencia(ocorrencias):
    tem, lista = listar_ocorrencias_service(ocorrencias)
    if not tem:
        print(lista)
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
    sucesso, dado = remover_ocorrencia_service(ocorrencias, indice)
    if not sucesso:
        print(dado)
    else:
        removido = dado
        print(f"Ocorrência removida: {removido['tipo']} - {removido['local']}")
def editar_ocorrencia(ocorrencias):
    tem, lista = listar_ocorrencias_service(ocorrencias)
    if not tem:
        print(lista)
        return
    for i, ocorrencia in enumerate(ocorrencias, start=1):
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
    sucesso, dado = editar_ocorrencia_service(ocorrencias, indice, novo_tipo, novo_local, nova_descricao)
    if sucesso:
        ocorrencia_atualizada = dado
        print(f"Ocorrência editada: {ocorrencia_atualizada['tipo']} - {ocorrencia_atualizada['local']} - {ocorrencia_atualizada['descricao']}")
    else:
        print(dado)