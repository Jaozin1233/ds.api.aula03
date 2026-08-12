from fastapi import FastAPI 

app= FastAPI(title= "Minhas Primeira Api")

alunos = [
    {"id": 1, "nome": "Jhonnathan Reis", "Telefone": "119999999"}
]

@app.get("/")
def home():
    return {"Mensagem" : "Api rodando com sucesso"}

@app.get("/alunos")
def listar_alunos():
    return alunos    
