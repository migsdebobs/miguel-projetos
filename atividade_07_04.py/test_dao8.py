import sqlite3
import unittest

# ==========================================
# 1. CLASSE DAO (Com Erro Proposital no UPDATE)
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

    # ERRO PROPOSITAL: Sem o self.conn.commit() e com breakpoint()
    def atualizar(self, id_produto, novo_nome):
        self.cursor.execute(
            "UPDATE produtos SET nome = ? WHERE id = ?",
            (novo_nome, id_produto)
        )
        breakpoint() # O código vai pausar aqui para você inspecionar!
        # self.conn.commit() <--- ESQUECEMOS DE PROPÓSITO PARA FORÇAR O BUG

    def deletar(self, id_produto):
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


# ==========================================
# 2. CLASSE DE TESTE
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

    def test_atualizar_objeto(self):
        # 1. Salve um registro inicial
        nome_inicial = "Teclado Comum"
        id_produto = self.dao.salvar(nome_inicial, 5)

        # 2. Atualize o registro (O código vai parar no breakpoint aqui dentro)
        novo_nome_esperado = "Teclado Mecânico RGB"
        self.dao.atualizar(id_produto, novo_nome_esperado)

        # 3. Busque novamente do banco
        produto_atualizado = self.dao.buscar_por_id(id_produto)

        # 4. Assert: Este teste vai FALHAR propositalmente
        self.assertEqual(
            produto_atualizado[1], 
            novo_nome_esperado, 
            "Falha proposital: O nome não atualizou porque faltou o commit no DAO."
        )

if __name__ == '__main__':
    unittest.main()