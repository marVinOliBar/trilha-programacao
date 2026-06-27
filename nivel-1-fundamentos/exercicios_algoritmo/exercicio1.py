
def texto_obrigatorio_valido(valor):
    if valor is None:
        return False
    
    if not isinstance(valor, str):
        return False
    
    if valor.strip() == "":
        return False
    
    return True

def validar_ocorrencia(ocorrencia):
    
    if not isinstance(ocorrencia, dict):
        return False
        
    campos_texto_obrigatorios = ["numero", "data", "natureza", "bairro"]
    
    for campo in campos_texto_obrigatorios:
        valor = ocorrencia.get(campo)
        
        if not texto_obrigatorio_valido(valor):
            return False 
    
    tempo_resposta_min = ocorrencia.get("tempo_resposta_min")
            
    if tempo_resposta_min is None:
        return False
    
    if type(tempo_resposta_min) is not int:
        return False
    
    if tempo_resposta_min < 0:
        return False
    
    viaturas = ocorrencia.get("viaturas")
            
    if viaturas is None:
        return False
    
    if not isinstance(viaturas, list):
        return False
    
    if len(viaturas) == 0:
        return False
    
    return True
