import sqlite3

def refatoracao_mestre():
    conn = sqlite3.connect("sistema_escolar.db")
    cursor = conn.cursor()

    # Habilitar chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Inserindo um Aluno
    cursor.execute("INSERT INTO Aluno (nome_aluno, data_nascimento) VALUES (?, ?)", 
                   ("Lucas Silva", "2000-05-15"))
    aluno_id = cursor.lastrowid

    # Inserindo os Certificados (Antigo campo multivalorado agora são linhas)
    certificados = ["Python Básico", "Gestão de Projetos", "Inglês Avançado"]
    
    for cert in certificados:
        cursor.execute("INSERT INTO Certificado_Anterior (nome_certificado, fk_aluno) VALUES (?, ?)", 
                       (cert, aluno_id))

    conn.commit()
    print(f"Aluno {aluno_id} e seus {len(certificados)} certificados cadastrados com sucesso!")
    conn.close()

refatoracao_mestre()