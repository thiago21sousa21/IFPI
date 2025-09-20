from models.matricula import Matricula
from dababase.simulacao_db import matriculas
from utils.abstracoes import Abstracao

class MatriculaDao:

    @staticmethod
    def listar_todas():
        return Abstracao.selectAllObjects(matriculas)
    
    @staticmethod
    def listar_uma(matricula: Matricula):
        for m in matriculas:
            if m.id == matricula.id:
                return [vars(m)]
        return []
    
    @staticmethod
    def inserir_uma(matricula:Matricula):
        if not matricula.id:
            matricula.id = len(matriculas) + 1
        matriculas.append(matricula)

    @staticmethod
    def deletar_uma(matricula: Matricula):
        for idx, m in enumerate(matriculas):
            if m.id == matricula.id:
                del matriculas[idx]
                break
