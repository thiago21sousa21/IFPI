from Conexao import Connection
from Disciplina import Disciplina

class DisciplinaDao:

    @staticmethod
    def criar_tabela_disciplinas():
        with Connection() as db:
            if not db:
                return

            try:
                query = """CREATE TABLE IF NOT EXISTS disciplinas(
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nome VARCHAR(100) NOT NULL,
                                carga_horaria INT NOT NULL,
                                professor_id INT,
                                FOREIGN KEY (professor_id) REFERENCES professores(id) ON DELETE CASCADE
                            )"""
                db.executar(query)
                print("Tabela 'disciplinas' verificada/criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela disciplinas: {e}")

    @staticmethod
    def criar_disciplina(disciplina: Disciplina):
        with Connection() as db:
            if not db:
                return

            try:
                # CORREÇÃO 3: Não inserimos o 'id', pois é AUTO_INCREMENT.
                # CORREÇÃO 4: Usamos disciplina.professor_id, que agora é um inteiro.
                query = """INSERT INTO disciplinas
                            (nome, carga_horaria, professor_id)
                            VALUES (%s, %s, %s)"""
                values = (disciplina.nome, disciplina.carga_horaria, disciplina.professor_id)
                
                novo_id = db.executar(query, values)
                if novo_id is not None:
                    disciplina.id = novo_id # Atualiza o objeto com o ID do banco
                    print(f"Disciplina '{disciplina.nome}' inserida com sucesso com o ID: {novo_id}")
                
            except Exception as e:
                print(f"Erro ao inserir disciplina: {e}")
    
    @staticmethod
    def listar_disciplinas():
        with Connection() as db:
            if not db:
                return []
            
            try:
                # Usamos um JOIN para buscar também o nome do professor.
                query = """
                    SELECT d.id, d.nome, d.carga_horaria, d.professor_id, p.nome 
                    FROM disciplinas d
                    LEFT JOIN professores p ON d.professor_id = p.id
                """
                return db.buscar(query)
            except Exception as e:
                print(f"Erro ao listar disciplinas: {e}")
                return []
            