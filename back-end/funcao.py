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
# cadastrar_filme("Avatar", "Ação", 2009, 10)

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
       
def atulizar_nota(id_filme,nova_nota):
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET nota = %s WHERE id = %s ",
                (nova_nota, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"ERRO ao atulizar nota: {erro}")
        finally:
            cursor.close()
            conexao.close()
# id_filme = int(input("Digite o id do filme que deseja atualizar: "))
# nova_nota = input("Digite a nota que deseja atualizar: ")

# atulizar_nota(id_filme, nova_nota)

def deletar_filme(id_filme):
       conexao, cursor = connector()
       if conexao:
           try:
               cursor.execute(
                   "DELETE FROM filmes WHERE id = %s",
                   (id_filme,)
               )
               conexao.commit()
               if cursor.rowcount > 0:
                   print("O filme foi removido com sucesso!")
               else:
                   print("Nenhum filme foi encontrado com o id fornecido. ")
           except Exception as erro:
               print(f"Erro tentar deletar filme: {erro}")
           finally:
               cursor.close()
               conexao.close()

# id_filme = int(input("Digite o id do filme que deseja deletar: "))
# deletar_filme(id_filme)

def buscar_filme(id_filme):
       conexao, cursor = connector()
       if conexao:
           try:
               cursor.execute(
                   "SELECT * FROM filmes WHERE id = %s",
                   (id_filme,)
               )
               return cursor.fetchone()
           except Exception as erro:
               print(f"Erro tentar deletar filme: {erro}")
           finally:
               cursor.close()
               conexao.close()