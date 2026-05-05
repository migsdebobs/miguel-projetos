import sqlite3

conexao = sqlite3.connect("hospital.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

def estruturar_banco_2fn():
    cursor.execute("DROP TABLE IF EXISTS Plantoes;")
    cursor.execute("DROP TABLE IF EXISTS Medicos;")

    cursor.execute(""" 
        CREATE TABLE Medicos (
            ID_Medico INTEGER PRIMARY KEY AUTOINCREMENT,
            CRM_Medico TEXT NOT NULL UNIQUE
        );
    """)
    
    cursor.execute(""" 
        CREATE TABLE Plantoes (
            ID_Plantao INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Medico INTEGER NOT NULL,
            ID_Ala TEXT NOT NULL,
            Data_Plantao TEXT NOT NULL,
            FOREIGN KEY (ID_Medico) REFERENCES Medicos(ID_Medico)
        );
    """)
    
    conexao.commit()

estruturar_banco_2fn()

conexao.close()