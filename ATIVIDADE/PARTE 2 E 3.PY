import sqlite3

def tabela_categoria():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("DROP TABLE IF EXISTS tb_categoria")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tb_categoria(
                id_descricao_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                preco REAL NOT NULL
                )""")


    comando_sql = "INSERT INTO tb_categoria (item, preco) VALUES (?, ?)"

    dados_do_item = ("Teclado Mecânico", 150.00) 
    cursor.execute(comando_sql, dados_do_item)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("Banco de dados criado e item inserido com sucesso!")

tabela_categoria()