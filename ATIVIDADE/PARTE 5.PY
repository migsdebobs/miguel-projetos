import sqlite3
from datetime import datetime

def obter_conexao():
    conexao = None
    try:
        conexao = sqlite3.connect('estoque.db')
        print("Conexão estabelecida com sucesso!")
    except sqlite3.Error as e:
        mensagem_erro = f"{datetime.now()} - Erro ao conectar ao banco de dados: {e}\n"
        
       
        print(mensagem_erro)
        
       
        with open("erros_log.txt", "a", encoding="utf-8") as arquivo_log:
            arquivo_log.write(mensagem_erro)
            
    return conexao

if __name__ == "__main__":
    con = obter_conexao()
    if con:
        con.close()
        print("Conexão fechada.")