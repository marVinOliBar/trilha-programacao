import json

def salvar(ocorrencias):
    with open("ocorrencias.json", "w") as arquivo:
        json.dump(ocorrencias, arquivo, indent=4, ensure_ascii=False)

def carregar():
    try:
        with open("ocorrencias.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
