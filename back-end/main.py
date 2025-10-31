#Usar o .venv/Scripts/activate
# #Lembrar que para rodar o uvicorn tem que usar no terminal (cd e acessar a pasta desejada.)
from fastapi import FastAPI
import funcao

#Como executar o fastapi
#Python -m uvicorn main:app --reload

app = FastAPI(title="Gerenciador de filmes")
#Criando uma rota 
@app.get("/")
def home():
    return {"Mensagem": "Bem-vindo ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return{"200": "Filme cadastrado com sucesso!"}

#Criando uma rota get
@app.get("/filmes")
def listar_filmes():
    #Chamando a função listar filmes do arquivo função
    filmes = funcao.listar_filmes()
    #Criando lista para exibir filmes com for
    lista = []
    for linha in filmes:
        lista.append(
            {
                "id": linha[0],
                "titulo": linha[1],
                "genero": linha [2],
                "ano": linha [3],
                "nota": linha [4]
            }
        )
    #Retornando a lista para o usuario
    return {"filmes": lista}