from service import listar_ocorrencia_service
from fastapi import FastAPI
app = FastAPI()

@app.get("/ocorrencia")
def listar_ocorrencia():
    _, dado = listar_ocorrencia_service()
    ocorrencias_etiquetadas = [{'sdo': ocorrencia[0], 'data': ocorrencia[1], 'tipo': ocorrencia[2], 'local': ocorrencia[3], 'descricao': ocorrencia[4]}
                              for ocorrencia in dado]
    return ocorrencias_etiquetadas