from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de Videogame
class Videogame(BaseModel):
    id: int
    nome: str
    quantidade: int
    preco: float

# Lista para armazenar os videogames (simula um banco de dados em memória)
videogames: List[Videogame] = []

# Rota GET: Listar todos os videogames
@app.get("/videogames", response_model=List[Videogame])
def listar_videogames():
    return videogames

# Rota GET: Buscar videogame pelo ID
@app.get("/videogames/{videogame_id}", response_model=Videogame)
def buscar_videogame(videogame_id: int):
    for videogame in videogames:
        if videogame.id == videogame_id:
            return videogame
    raise HTTPException(status_code=404, detail="Videogame não encontrado")

# Rota POST: Adicionar novo videogame
@app.post("/videogames", response_model=Videogame)
def adicionar_videogame(videogame: Videogame):
    for vg in videogames:
        if vg.id == videogame.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    videogames.append(videogame)
    return videogame

# Rota PUT: Atualizar videogame existente pelo ID
@app.put("/videogames/{videogame_id}", response_model=Videogame)
def atualizar_videogame(videogame_id: int, videogame_atualizado: Videogame):
    for index, videogame in enumerate(videogames):
        if videogame.id == videogame_id:
            videogames[index] = videogame_atualizado
            return videogame_atualizado
    raise HTTPException(status_code=404, detail="Videogame não encontrado")

# Rota DELETE: Remover videogame pelo ID
@app.delete("/videogames/{videogame_id}")
def deletar_videogame(videogame_id: int):
    for index, videogame in enumerate(videogames):
        if videogame.id == videogame_id:
            del videogames[index]
            return {"message": "Videogame removido com sucesso"}
    raise HTTPException(status_code=404, detail="Videogame não encontrado")
