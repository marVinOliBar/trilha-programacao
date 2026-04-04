import storage
from interface import (
    registrar_ocorrencia,
    listar_ocorrencias,
    pesquisar_ocorrencias,
    remover_ocorrencia,
    editar_ocorrencia,
)
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