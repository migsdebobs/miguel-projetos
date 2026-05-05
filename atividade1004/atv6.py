import sqlite3

conexao = sqlite3.connect("ATV.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

def estruturar_banco_2fn():
    cursor.execute("DROP TABLE IF EXISTS aluno;")
    cursor.execute("DROP TABLE IF EXISTS disciplina;")

    cursor.execute(""" 
        CREATE TABLE aluno (
            ID_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT NOT NULL UNIQUE
            nome_aluno TEXT NOT NULL 
        );
    """)



    cursor.execute(""" 
        CREATE TABLE disciplina (
            ID_disciplina INTEGER PRIMARY KEY AUTOINCREMENT
            nome_disciplina NOT NULL,
            nota_final TEXT NOT NULL,
            
        );
    """)

    


    
    conexao.commit()

estruturar_banco_2fn()

conexao.close()