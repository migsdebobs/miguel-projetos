import sqlite3
import unittest

# ==========================================
# 1. CLASSE DAO (Com Regra de Negócio)
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
                quantidade_estoque INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """)
        self.conn.commit()

    def salvar(self, nome, quantidade, preco):
        # --- REGRA DE NEGÓCIO (Bloqueio de Base Corrompida) ---
        if preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        
        self.cursor.execute(
            "INSERT INTO produtos (nome, quantidade_estoque, preco) VALUES (?, ?, ?)", 
            (nome, quantidade, preco)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def buscar_por_id(self, id_produto):
        self.cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        return self.cursor.fetchone()

    def fechar_conexao(self):
        self.conn.close()


# ==========================================
# 2. CLASSE DE TESTE (Validação de Bloqueio)
# ==========================================
class TestProdutoDAO(unittest.TestCase):

    def setUp(self):
        self.dao = ProdutoDAO()

    def tearDown(self):
        self.dao.fechar_conexao()

    # TESTE DE CONFIABILIDADE: Validando o bloqueio de dados inválidos
    def test_salvar_produto_preco_negativo(self):
        """
        Prova que o sistema levanta ValueError e não salva 
        se o preço for menor que zero.
        """
        # O assertRaises verifica se a exceção ValueError é disparada
        with self.assertRaises(ValueError) as context:
            # Tentativa de salvar "lixo" (preço -10.0)
            self.dao.salvar("Produto Errado", 5, -10.0)
        
        # Opcional: Validar a mensagem do erro
        self.assertEqual(str(context.exception), "O preço do produto não pode ser negativo.")

    def test_salvar_produto_valido(self):
        """Garante que produtos corretos continuam sendo salvos."""
        id_p = self.dao.salvar("Produto Correto", 10, 50.0)
        self.assertIsNotNone(id_p)

if __name__ == '__main__':
    unittest.main()
