import sqlite3

def obter_conexao():
    conexao = None  
    try:
        conexao = sqlite3.connect('estoque.db')
        print("Conexão estabelecida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    
    return conexao  

if __name__ == "__main__": 
    con = obter_conexao()
    if con:
        con.close()
        print("Conexão fechada.")
