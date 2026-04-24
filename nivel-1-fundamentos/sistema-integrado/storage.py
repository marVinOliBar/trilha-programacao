import json

def salvar(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    
def carregar(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []