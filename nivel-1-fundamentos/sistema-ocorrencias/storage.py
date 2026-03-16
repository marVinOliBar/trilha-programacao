import json

def salvar(ocorrencias):
    with open("ocorrencias.json", "w") as arquivo:
        json.dump(ocorrencias, arquivo)

def carregar():
    try:
        with open("ocorrencias.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []