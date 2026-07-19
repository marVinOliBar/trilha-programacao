from service import listar_ocorrencia_service
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/ocorrencia")
def listar_ocorrencia():
    sucesso, dado = listar_ocorrencia_service()
    if sucesso:
        return dado
    raise HTTPException(status_code=404, detail=dado)