import sqlite3

def configurar_banco():
    conexao = sqlite3.connect("gestao_empresa.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Empresa (
        cnpj CHAR(14) INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Diretor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_diretor TEXT NOT NULL,
            fk_empresa_cnpj TEXT NOT NULL,
            FOREIGN KEY (fk_empresa_cnpj) REFERENCES Empresa(cnpj)
        )
        """)

    cnpj_exemplo = "12345678000199"

    cursor.execute("INSERT OR IGNORE INTO Empresa (cnpj, nome) VALUES (?, ?)", 
                    (cnpj_exemplo, "Tech Solutions LTDA"))

    diretores = [("Ana Silva",), ("Carlos Oliveira",), ("Beatriz Souza",)]

    comando_diretor = "INSERT INTO Diretor (nome, matricula) VALUES (?, ?)"
    for d in diretores:
            cursor.execute(comando_diretor, (d[0], cnpj_exemplo))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("Banco de dados 1FN configurado e dados inseridos!")

if __name__ == "__main__":
    configurar_banco()