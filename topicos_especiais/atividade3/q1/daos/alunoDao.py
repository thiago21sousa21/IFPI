from models.aluno import Aluno
from dababase.simulacao_db import alunos
from utils.abstracoes import Abstracao

class AlunoDao:

    @staticmethod
    def listar_todas():
        return Abstracao.selectAllObjects(alunos)
    
    @staticmethod
    def listar_uma(aluno: Aluno):
        for a in alunos:
            if a.matricula.id == aluno.matricula.id:
                return [vars(a)]
        return []
    
    @staticmethod
    def inserir_uma(aluno:Aluno):
        alunos.append(aluno)

    @staticmethod
    def deletar_uma(aluno: Aluno):
        for idx, a in enumerate(alunos):
            if a.matricula.id == aluno.matricula.id:
                del alunos[idx]
                break