from conexao import Connection
from professor import Professor

class ProfessorDao:

    @staticmethod
    def create_professor(professor: Professor):
        with Connection() as cnx:
            cnx.executar("""INSERT INTO 
                                    professores
                                    (nome, sobrenome, data_nascimento, matricula, email)
                                VALUES 
                                    (%s, %s, %s, %s, %s)""", professor.return_dados())
    
    