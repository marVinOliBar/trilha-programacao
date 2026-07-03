import sqlite3
from storage import(registrar_viatura_storage,
                    buscar_viatura_storage,
                    remover_viatura_storage,
                    editar_viatura_storage,
                    listar_viatura_storage,
                    registrar_ocorrencia_storage)

SITUACOES_VALIDAS = ("operando", "manutencao", "baixada")

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
    

def buscar_viatura_service(termo):
    if not termo:
            return (False, "Digite um termo para a busca.")
    
    resultado = buscar_viatura_storage(termo.lower().strip())
    
    if not resultado:
        return (False, "Nenhuma viatura encontrada.")
    else:
        return (True, resultado)
    

def remover_viatura_service(prefixo):
    if not prefixo:
        return (False, "É necessário digitar um prefixo.")
    
    try:
        resultado = remover_viatura_storage(prefixo)
    except sqlite3.IntegrityError:
        return (False, "Não é possível remover a viatura. Ela possui atendimentos registrados.")
    
    if resultado == 0:
        return (False, "Nenhuma viatura foi registrada com esse prefixo.")
    else:
        return (True, resultado)
    
def editar_viatura_service(prefixo, quilometragem, estacao, situacao):
    if not prefixo:
        return (False, "É necessário indicar o prefixo da viatura: ")
    if not quilometragem:
        return (False, "É necessário indicar a quilometragem da viatura: ")
    if not estacao:
        return (False, "É necessário indicar a estação da viatura: ")
    if not situacao:
        return (False, "É necessário indicar a situação da viatura: ")
    
    if situacao not in SITUACOES_VALIDAS:
        return (False, "a situação deve ser: operando | manutenção | baixada")
    
    try:
        resultado = editar_viatura_storage(prefixo, quilometragem, estacao, situacao)
    except sqlite3.IntegrityError:
        return (False, "a situação deve ser: operando | manutenção | baixada")
    
    if resultado == 0:
        return (False, "A viatura não foi editada")
    else:
        return (True, resultado)

def listar_viatura_service():
    resultado = listar_viatura_storage()
    if not resultado:
        return (False, "Nenhuma viatura registrada.")
    else:
        return (True, resultado)
        
def registrar_ocorrencia_service(sdo, data, tipo, local, descricao):
    if not sdo:
        return (False, "É necessário preencher o número do SDO.")
    if not data:
        return (False, "É necessário preencher a data.")
    if not tipo:
        return (False, "É necessário preencher o tipo de ocorrência.")
    if not local:
        return (False, "É necessário preencher o local da ocorrência.")
    if not descricao:
        return (False, "É necessário preencher a descrição da ocorrencia.")
    
    try:
        id_gerado = registrar_ocorrencia_storage(sdo, data, tipo, local, descricao)
    except sqlite3.IntegrityError:
        return (False, f"Esse SDO já existe na data {data}")
    
    return (True, id_gerado)