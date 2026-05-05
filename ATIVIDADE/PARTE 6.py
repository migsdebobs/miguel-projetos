import sqlite3
from datetime import datetime

def obter_conexao(caminho_banco):

    try:
        conexao = sqlite3.connect(caminho_banco)
        print("Conexão estabelecida com sucesso!")
        return (True, conexao)
        
    except sqlite3.Error as e:
        mensagem_erro = f"{datetime.now()} - Erro ao conectar ao banco de dados: {e}"
    
    
        with open("erros_log.txt", "a", encoding="utf-8") as arquivo_log:
            arquivo_log.write(mensagem_erro + "\n")
            
        return (False, str(e))

if __name__ == "__main__":
   
    status, resultado = obter_conexao('estoque.db')
    
    if status:
        print("Status: Sucesso!")
       
        resultado.close()
        print("Conexão fechada com segurança.")
    else:
        print("Status: Falha!")
    
        print(f"Motivo do erro: {resultado}")