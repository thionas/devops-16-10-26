import requests
@APP.put("/tarefas/{id}")
async def concluir_tarefa(id: int):

    for tarefa in TAREFAS:
        if id == int(tarefa['id']) and tarefa['concluida'] == False:

            tarefa['concluida'] = True
            tarefa['concluida_em'] = datetime.now()

            requests.post(
                "http://localhost:8002/notificar",
                params={
                    "id_tarefa": tarefa["id"],
                    "titulo": tarefa["titulo"]
                }
            )

            return {"mensagem": "Tarefa atualizada"}

    return {"mensagem": "Tarefa não existe"}