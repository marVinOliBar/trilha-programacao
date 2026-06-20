from storage import(registrar_viatura_storage)

def registrar_viatura_service(prefixo, quilometragem, estacao, situacao):
    if not prefixo:
        return (False, "É obrigatório registrar um prefixo!")
    if not quilometragem:
        return (False, "É obrigatório registrar uma quilometragem!")
    if not estacao:
        return (False, "É obrigatório registrar uma estação!")
    if not situacao:
        return (False, "É obrigatório registrar uma situação!")
    
    registrar_viatura_storage(prefixo, quilometragem, estacao, situacao)
    
    return (True, prefixo)