from service import listar_ocorrencia_service
from fastapi import FastAPI
app = FastAPI()

@app.get("/ocorrencia")
def listar_ocorrencia():
    sucesso, dado = listar_ocorrencia_service()
    return dado