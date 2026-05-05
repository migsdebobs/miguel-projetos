import sqlite3

# 1. Estabelecendo a conexão
conexao = sqlite3.connect("banco_filmes.db")
cursor = conexao.cursor()

# (Opcional) Isso apaga a tabela toda vez que você roda o código. 
# Se quiser guardar os filmes para sempre, remova a linha abaixo:
cursor.execute("DROP TABLE IF EXISTS biblioteca_filmes")

print("-- Cadastro de Filme --")
nome_filme = input("Digite o nome do filme que queira adicionar: ")
genero_filme = input("Qual o gênero: ")

# 2. Criação da Tabela (Corrigido REAL para TEXT)
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS biblioteca_filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_filme TEXT NOT NULL,
        genero_filme TEXT NOT NULL
    )
""")

# 3. Execução da query com passagem segura
# (Corrigido o nome da tabela de 'produtos' para 'biblioteca_filmes')
comando_sql = "INSERT INTO biblioteca_filmes (nome_filme, genero_filme) VALUES (?, ?)"

# (Corrigido: passando as variáveis para a tupla)
valores = (nome_filme, genero_filme)

# 4. Inserindo no banco
cursor.execute(comando_sql, valores)

# 5. Confirmação e Encerramento
conexao.commit()
cursor.close()
conexao.close()

print("\nFilme adicionado com sucesso!")
