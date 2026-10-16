from fastapi import FastAPI
from datetime import datetime

APP = FastAPI()

@app.post("/notificar")
async def notificar(id_tarefa: int, titulo: str):
    return {
        "mensagem": f"Notificação enviada para a tarefa {titulo}",
        "data": datetime.now()
    }