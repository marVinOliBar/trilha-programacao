import storage
from logica import adicionar_ocorrencia

def registrar_ocorrencia_service(ocorrencias, tipo, local, descricao):
    ocorrencia = adicionar_ocorrencia(ocorrencias, tipo, local, descricao)
    storage.salvar(ocorrencias)
    return ocorrencia