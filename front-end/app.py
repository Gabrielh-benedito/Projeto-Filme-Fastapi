# pip install streamlit request
#Rodar streamlit = python -m streamlit run app.pt
import streamlit as st
import requests

# URL da API fastapi
API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de Filmas")

menu = st.sidebar.radio("Menu", 
                 ["Listar Filmes", "Cadastrar Filmes"]
                 )
if menu == "Listar Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes",[])
    else:
        st.error("erro ao conectar com a API.") 