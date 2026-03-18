import storage

def registrar_talao(ocorrencias):
    tipo = input("Digite o tipo da ocorrência: ").strip()
    local = input("Digite o local da ocorrência: ").strip()
    descricao = input("Digite a descrição da ocorrência: ").strip()

    talao = {
        "tipo": tipo,
        "local": local,
        'descricao': descricao,
    }

    ocorrencias.append(talao)
    storage.salvar(ocorrencias)

def listar_ocorrencias(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return

    for i, talao in enumerate(ocorrencias, start=1):
        print(f"Talão {i} - Tipo: {talao['tipo']} - Local: {talao['local']} - Descrição: {talao['descricao']}")
        print("===============")

def pesquisar_ocorrencias(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return

    termo = input("Digite o local da ocorrência que está procurando: ").lower().strip()

    resultado = []

    for i, talao in enumerate(ocorrencias, start=1):
        if termo in talao["local"].strip().lower():
            resultado.append((i, talao))

    if resultado:
        for i, talao in resultado:
            print(f"ID {i} - Tipo: {talao['tipo']} - Local: {talao['local']} - Descrição: {talao['descricao']}")
    else:
        print("Não foram encontradas ocorrências!")

def remover_ocorrencia(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return

    for i, talao in enumerate(ocorrencias, start=1):
        print(f"{i} - Tipo: {talao['tipo']} - Local: {talao['local']} - Descrição: {talao['descricao']}")

    try:
        opcao = int(input("Digite o número da ocorrência que deseja remover: "))
    except ValueError:
        print("Digite apenas números!")
        return

    if opcao < 1 or opcao > len(ocorrencias):
        print("Opção inválida!")
        return

    indice = opcao - 1

    removido = ocorrencias.pop(indice)

    print(f"Ocorrência removida: {removido['tipo']} - {removido['local']}")

    storage.salvar(ocorrencias)

def editar_ocorrencia(ocorrencias):

	if len(ocorrencias) == 0:
		print("Não há ocorrências cadastradas!")
		return

	for i, talao in enumerate(ocorrencias, start = 1):
		print(f"ID: {i} - Tipo: {talao['tipo']} - Local: {talao['local']} - Descrição: {talao['descricao']}")

	try:
		opcao = int(input("Digite a opcao desejada: "))
	except ValueError:
		print("Digite apenas números!")
		return

	if opcao < 1 or opcao > len(ocorrencias):
		print("Digite um ID válido!")
		return

	indice = opcao - 1	

	novo_tipo = input("Descreva o novo tipo de ocorrência: ").strip().lower()
	novo_local = input("Descreva o novo local de ocorrência: ").strip().lower()
	nova_descricao = input("Descreva a nova descricao da ocorrência: ").strip().lower()

	if novo_tipo:
		ocorrencias[indice]['tipo'] = novo_tipo

	if novo_local:
		ocorrencias[indice]['local'] = novo_local

	if nova_descricao:
		ocorrencias[indice]['descricao'] = nova_descricao

	storage.salvar(ocorrencias)
	print("Ocorrência editada com sucesso!")


def main():

    ocorrencias = storage.carregar()

    while True:

        try:
            opcao = int(input(
                "1 Registrar | 2 Listar | 3 Pesquisar | 4 Remover | 5 Editar 0 Sair\nEscolha: "
            ))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            registrar_talao(ocorrencias)

        elif opcao == 2:
            listar_ocorrencias(ocorrencias)

        elif opcao == 3:
            pesquisar_ocorrencias(ocorrencias)

        elif opcao == 4:
            remover_ocorrencia(ocorrencias)

        elif opcao == 5:
             editar_ocorrencia(ocorrencias)

        elif opcao == 0:
            print("Até logo!")
            break

        else:
            print("Escolha uma opção válida!")


if __name__ == "__main__":
    main()