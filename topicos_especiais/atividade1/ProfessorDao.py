from Professor import Professor
from Conexao import Connection

db = Connection(banco="professor_atividade", host="localhost", senha="123456", usuario="root")

class ProfessorDao:

    @staticmethod
    def createTable():
        try:
            db.conectar()
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
            db.fechar()
            print("Tabela criada com sucesso!")
        except Exception as err:
            print(f"Erro ao criar a tabela: {err}")

    @staticmethod
    def insertProfessor(professor: Professor):
        try:
            db.conectar()
            query = """INSERT INTO professores 
                       (nome, sobrenome, matricula, data_nascimento, email) 
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (professor.nome, professor.sobrenome, professor.matricula, professor.data_nascimento, professor.email)
            db.executar(query, values)
            db.fechar()
            print("Professor inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir professor: {e}")

    @staticmethod
    def listarProfessores():
        try:
            db.conectar()
            query = "SELECT * FROM professores"
            db.executar(query)
            resultados = db.buscar()
            db.fechar()
            return resultados
        except Exception as e:
            print(f"Erro ao listar professores: {e}")
            return []

    @staticmethod
    def buscarProfessorPorId(professor_id: int):
        try:
            db.conectar()
            query = "SELECT * FROM professores WHERE id = %s"
            db.executar(query, (professor_id,))
            resultado = db.buscar()
            db.fechar()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Erro ao buscar professor: {e}")
            return None

    @staticmethod
    def atualizarProfessor(professor_id: int, professor: Professor):
        try:
            db.conectar()
            query = """UPDATE professores 
                       SET nome=%s, sobrenome=%s, matricula=%s, data_nascimento=%s, email=%s 
                       WHERE id=%s"""
            values = (professor.nome, professor.sobrenome, professor.matricula, professor.data_nascimento, professor.email, professor_id)
            db.executar(query, values)
            db.fechar()
            print("Professor atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar professor: {e}")

    @staticmethod
    def deletarProfessor(professor_id: int):
        try:
            db.conectar()
            query = "DELETE FROM professores WHERE id=%s"
            db.executar(query, (professor_id,))
            db.fechar()
            print("Professor deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar professor: {e}")


if __name__ == "__main__":
    ProfessorDao.createTable()

    # Criar professor
    prof = Professor("Thiago", "Sousa", "123456", "21/10/1999", "thiago21sousa21@gmail.com")
    ProfessorDao.insertProfessor(prof)

    # Listar todos
    print("Lista de professores:", ProfessorDao.listarProfessores())

    # Buscar por ID
    print("Professor com ID 1:", ProfessorDao.buscarProfessorPorId(1))

    # Atualizar professor com ID 1
    prof_atualizado = Professor("Thiago", "Santos", "654321", "1999-10-21", "thiago.santos@ifpi.edu.br")
    ProfessorDao.atualizarProfessor(2, prof_atualizado)

    # Deletar professor
    ProfessorDao.deletarProfessor(1)

    print("Lista de professores:", ProfessorDao.listarProfessores())
