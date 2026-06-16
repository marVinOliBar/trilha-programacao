import json

def salvar(livros):
    with open("livros.json", "w", encoding='utf-8') as arquivo:
        return json.dump(livros, arquivo, indent=4, ensure_ascii=False)

def carregar():
    try:
        with open("livros.json", "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []