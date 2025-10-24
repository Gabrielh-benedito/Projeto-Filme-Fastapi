from conexao import connector

def criar_tabela():
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes(
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INT NOT NULL,   
                nota FLOAT
                )               
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()


def cadastrar_filme(titulo, genero, ano, nota):
        conexao, cursor = connector()
        if conexao:
            try:
                 cursor.execute(
                      "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (%s, %s, %s, %s)",
                      (titulo, genero, ano, nota)
                      )
                 conexao.commit()
            except Exception as erro:
                 print(f"ERRO ao cadastrar o filme {erro}")
            finally:
                 cursor.close()
                 conexao.commit()

def listar_filmes():
    conexao, cursor = connector() 
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY id"  
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os filmes: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

# print(f"Lista de filmes {listar_filmes}")

# filmes = listar_filmes()
# for filme in filmes:
#     print(filme)
       