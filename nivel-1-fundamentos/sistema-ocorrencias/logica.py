def adicionar_ocorrencia(ocorrencias, tipo, local, descricao):
    ocorrencia = {
        "tipo": tipo,
        "local": local,
        "descricao": descricao,
    }
    ocorrencias.append(ocorrencia)
    return ocorrencia
def buscar_ocorrencia(ocorrencias, termo):
    resultado = []
    for i, ocorrencia in enumerate(ocorrencias, start=1):
        for valor in ocorrencia.values():
            if termo in str(valor).lower():
                resultado.append((i, ocorrencia))
                break
    return resultado
def excluir_ocorrencia(ocorrencias, indice):
    removido = ocorrencias.pop(indice)
    return removido
def atualizar_ocorrencia(ocorrencias, indice, novo_tipo, novo_local, nova_descricao):
    ocorrencia = ocorrencias[indice]
    if novo_tipo:
        ocorrencia['tipo'] = novo_tipo
    if novo_local:
        ocorrencia['local'] = novo_local
    if nova_descricao:
        ocorrencia['descricao'] = nova_descricao
    return ocorrencia