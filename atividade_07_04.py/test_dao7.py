import sqlite3
import unittest

# ==========================================
# 1. CLASSE DAO (Expandida com Atualizar)
# ==========================================
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

    # NOVO MÉTODO: ATUALIZAR
    def atualizar(self, id_produto, novo_nome):
        self.cursor.execute(
            "UPDATE produtos SET nome = ? WHERE id = ?",
            (novo_nome, id_produto)
        )
        self.conn.commit()

    def deletar(self, id_produto):
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


# ==========================================
# 2. CLASSE DE TESTE EXPANDIDA
# ==========================================
class TestProdutoDAO(unittest.TestCase):

    def setUp(self):
        self.dao = ProdutoDAO()

    def tearDown(self):
        self.dao.fechar_conexao()

    def test_deletar_objeto(self):
        id_p = self.dao.salvar("Monitor", 10)
        self.dao.deletar(id_p)
        self.assertIsNone(self.dao.buscar_por_id(id_p))

    # NOVO TESTE: VALIDANDO ATUALIZAÇÃO RELACIONAL
    def test_atualizar_objeto(self):
        # 1. Salve um registro inicial
        nome_inicial = "Teclado Comum"
        id_produto = self.dao.salvar(nome_inicial, 5)

        # 2. Atualize o registro
        novo_nome_esperado = "Teclado Mecânico RGB"
        self.dao.atualizar(id_produto, novo_nome_esperado)

        # 3. Busque novamente do banco (linha física na RAM do SQLite)
        produto_atualizado = self.dao.buscar_por_id(id_produto)

        # 4. Assert: Confirma que o novo_nome sobrescreveu o antigo
        # Lembre-se: o retorno do fetchone é uma tupla (id, nome, quantidade)
        # O nome está no índice [1]
        self.assertEqual(
            produto_atualizado[1], 
            novo_nome_esperado, 
            "O nome do produto não foi atualizado corretamente no banco de dados."
        )
        
        # Garantir que o ID continua o mesmo (integridade referencial)
        self.assertEqual(produto_atualizado[0], id_produto)

if __name__ == '__main__':
    unittest.main()