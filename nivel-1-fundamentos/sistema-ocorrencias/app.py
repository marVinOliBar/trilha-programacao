import storage

def registrar_ocorrencia(ocorrencias):
    tipo = input("Digite o tipo da ocorrência: ").strip().lower()
    local = input("Digite o local da ocorrência: ").strip().lower()
    descricao = input("Digite a descrição da ocorrência: ").strip().lower()

    ocorrencia = {
        "tipo": tipo,
        "local": local,
        'descricao': descricao,
    }

    ocorrencias.append(ocorrencia)
    storage.salvar(ocorrencias)

def listar_ocorrencias(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return

    for i, ocorrencia in enumerate(ocorrencias, start=1):
        print(f"Talão {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")
        print("===============")

def pesquisar_ocorrencias(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
        return

    termo = input("Digite o local da ocorrência que está procurando: ").lower().strip()

    resultado = []

    for i, ocorrencia in enumerate(ocorrencias, start=1):
        if termo in ocorrencia["local"].strip().lower():
            resultado.append((i, ocorrencia))

    if resultado:
        for i, ocorrencia in resultado:
            print(f"ID {i} - Tipo: {ocorrencia['tipo']} - Local: {ocorrencia['local']} - Descrição: {ocorrencia['descricao']}")
    else:
        print("Não foram encontradas ocorrências!")

def remover_ocorrencia(ocorrencias):
    if len(ocorrencias) == 0:
        print("Não há ocorrências registradas!")
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

    removido = ocorrencias.pop(indice)

    print(f"Ocorrência removida: {removido['tipo']} - {removido['local']}")

    storage.salvar(ocorrencias)

def editar_ocorrencia(ocorrencias):

	if len(ocorrencias) == 0:
		print("Não há ocorrências cadastradas!")
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

	if novo_tipo:
		ocorrencia['tipo'] = novo_tipo

	if novo_local:
		ocorrencia['local'] = novo_local

	if nova_descricao:
		ocorrencia['descricao'] = nova_descricao

	storage.salvar(ocorrencias)
	print("Ocorrência editada com sucesso!")


def main():

    ocorrencias = storage.carregar()

    while True:

        try:
            opcao = int(input(
                "1 Registrar | 2 Listar | 3 Pesquisar | 4 Remover | 5 Editar | 0 Sair \nEscolha: "
            ))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            registrar_ocorrencia(ocorrencias)

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
