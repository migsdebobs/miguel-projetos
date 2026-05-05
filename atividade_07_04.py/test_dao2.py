import sqlite3
import unittest

# ==========================================
# 1. CLASSE DAO (Com o novo método deletar)
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

    # NOVO MÉTODO ADICIONADO PARA O TESTE FUNCIONAR
    def deletar(self, id_produto):
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

    
# ==========================================
# 2. CLASSE DE TESTES UNITÁRIOS
# ==========================================
class TestProdutoDAO(unittest.TestCase):

    def setUp(self):
        # Prepara o terreno: Cria um banco em memória zerado para os testes
        self.dao = ProdutoDAO()

    def tearDown(self):
        # Limpa a bagunça: Fecha a conexão após cada teste
        self.dao.fechar_conexao()

    # NOVA DEF DE TESTE CONFORME SOLICITADO
    def test_deletar_objeto(self):
        # 1. Salve um registro
        id_produto = self.dao.salvar("Teclado Mecânico", 15)
        
        # (Opcional, mas boa prática) Garantir que realmente salvou antes de deletar
        produto_antes_deletar = self.dao.buscar_por_id(id_produto)
        self.assertIsNotNone(produto_antes_deletar, "O produto deveria existir no banco antes de ser deletado.")

        # 2. Use o DAO para deletar
        self.dao.deletar(id_produto)

        # 3. Faça a busca do ID apagado
        produto_apagado = self.dao.buscar_por_id(id_produto)

        # 4. Utilize o self.assertIsNone para garantir que o retorno foi nulo
        self.assertIsNone(produto_apagado, "O retorno do banco deve ser nulo (None) após a deleção.")


# Executa os testes caso o arquivo seja rodado diretamente
if __name__ == '__main__':
    unittest.main()