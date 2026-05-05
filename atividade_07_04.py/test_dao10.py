import sqlite3
import unittest

# ==========================================
# 1. O CÓDIGO DA SUA APLICAÇÃO (ENTIDADE COMPLETA)
# ==========================================
class ClienteDAO:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def salvar(self, nome, cpf, idade):
        # REGRA DE NEGÓCIO: Bloqueia dados inválidos
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        
        self.cursor.execute(
            "INSERT INTO clientes (nome, cpf, idade) VALUES (?, ?, ?)", 
            (nome, cpf, idade)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def buscar_por_id(self, id_cliente):
        self.cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
        return self.cursor.fetchone()

    def atualizar(self, id_cliente, novo_nome, novo_cpf, nova_idade):
        self.cursor.execute(
            "UPDATE clientes SET nome = ?, cpf = ?, idade = ? WHERE id = ?",
            (novo_nome, novo_cpf, nova_idade, id_cliente)
        )
        self.conn.commit()

    def deletar(self, id_cliente):
        self.cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


# ==========================================
# 2. A SUÍTE DE TESTES PARA O AVALIADOR
# ==========================================
class TestClienteDAO(unittest.TestCase):

    def setUp(self):
        # Prepara um banco zerado na RAM para cada teste
        self.dao = ClienteDAO()

    def tearDown(self):
        # Fecha a conexão após o teste
        self.dao.fechar_conexao()

    def test_salvar_e_buscar_cliente(self):
        # 1. Create e Read
        id_cli = self.dao.salvar("Ana Silva", "111.222.333-44", 25)
        cliente = self.dao.buscar_por_id(id_cli)
        
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente[1], "Ana Silva") # Índice 1 é o nome



if __name__ == '__main__':
    unittest.main()
