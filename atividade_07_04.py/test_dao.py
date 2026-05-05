import sqlite3

class ProdutoDAO:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade_estoque INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def salvar(self, nome, quantidade):
        self.cursor.execute(
            "INSERT INTO produtos (nome, quantidade_estoque) VALUES (?, ?)", 
            (nome, quantidade)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def buscar_por_id(self, id_produto):
        self.cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        return self.cursor.fetchone()

    def fechar_conexao(self):
        self.conn.close()