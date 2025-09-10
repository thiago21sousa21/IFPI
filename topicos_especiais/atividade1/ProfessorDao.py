from Professor import Professor
from Conexao import Connection

class ProfessorDao:

    @staticmethod
    def createTable():
        # Usa o 'with' para garantir que a conexão será aberta e fechada
        with Connection() as db:
            if db: # Verifica se a conexão foi bem sucedida
                try:
                    query = """
                    CREATE TABLE IF NOT EXISTS professores (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(100),
                        sobrenome VARCHAR(100),
                        matricula VARCHAR(100),
                        data_nascimento DATE,
                        email VARCHAR(100)
                    )
                    """
                    db.executar(query)
                    print("Tabela de professores criada/verificada com sucesso!")
                except Exception as err:
                    print(f"Erro ao criar a tabela: {err}")

    @staticmethod
    def insertProfessor(professor :Professor):
        with Connection() as db:
            if db:
                try:
                    query = """INSERT INTO professores 
                               (nome, sobrenome, matricula, data_nascimento, email) 
                               VALUES (%s, %s, %s, %s, %s)"""
                    values = (professor.nome, professor.sobrenome, professor.matricula, professor.data_nascimento, professor.email)
                    result = db.executar(query, values)
                    print("Professor inserido com sucesso!")
                    return result
                except Exception as e:
                    print(f"Erro ao inserir professor: {e}")

    @staticmethod
    def listarProfessores():
        with Connection() as db:
            if db:
                try:
                    query = "SELECT * FROM professores"
                    # O método 'buscar' agora executa a query e retorna os resultados
                    return db.buscar(query)
                except Exception as e:
                    print(f"Erro ao listar professores: {e}")
        return []

    # ... Adapte os outros métodos (buscarPorId, atualizar, deletar) da mesma forma
    
    @staticmethod
    def buscarProfessorPorId(professor_id: int):
        with Connection() as db:
            if db:
                try:
                    query = "SELECT * FROM professores WHERE id = %s"
                    resultado = db.buscar(query, (professor_id,))
                    return resultado[0] if resultado else None
                except Exception as e:
                    print(f"Erro ao buscar professor: {e}")
        return None

    @staticmethod
    def deletarProfessor(professor_id: int):
            with Connection() as db:
                if db:
                    try:
                        query = "DELETE FROM professores WHERE id=%s"
                        db.executar(query, (professor_id,))
                        print("Professor deletado com sucesso!")
                    except Exception as e:
                        print(f"Erro ao deletar professor: {e}")