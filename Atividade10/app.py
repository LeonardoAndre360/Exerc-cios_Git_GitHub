from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas = []

class NovaTarefa(BaseModel):
    nome: str
    descricao: str

@app.get("/lista")
def get_lista():
    if not tarefas:
        return {"message": "Não tem nenhuma tarefa registrada"}
    return {"lista": tarefas}

@app.post("/adiciona")
def post_lista(tarefa: NovaTarefa):
    for t in tarefas:
        if t["nome"] == tarefa.nome:
            raise HTTPException(status_code=400, detail="Esta tarefa já existe!")
    
    novo_dicionario_tarefa = {
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "concluida": False
    }
    tarefas.append(novo_dicionario_tarefa)
    
    return {"message": "A Tarefa foi criada com sucesso!"}

@app.put("/atualiza/{nome_tarefa}")
def put_lista(nome_tarefa: str):
    for t in tarefas:
        if t["nome"] == nome_tarefa:
            t["concluida"] = True
            return {"message": f"A tarefa '{nome_tarefa}' foi marcada como concluída!"}
            
    raise HTTPException(status_code=404, detail="Esta tarefa não foi encontrada!")

@app.delete("/deletar/{nome_tarefa}")
def delete_lista(nome_tarefa: str):
    for i, t in enumerate(tarefas):
        if t["nome"] == nome_tarefa:
            del tarefas[i]
            return {"message": "Sua tarefa foi deletada com sucesso!"}
            
    raise HTTPException(status_code=404, detail="Esta tarefa não foi encontrada!")