from models.professor import Professor
from utils.abstracoes import Abstracao
from dababase.simulacao_db import professores

class ProfessorDao:

    @staticmethod
    def getAll():
        return Abstracao.selectAllObjects(professores)

    @staticmethod
    def getOne(professor:Professor):
        for p in professores:
            if p.id_professor == professor.id_professor:
                return [vars(p)]

    @staticmethod
    def deleteOne(professor:Professor):
        for idx, p in enumerate(professores):
            if p.id_professor == professor.id_professor:
                del professores[idx]

    @staticmethod
    def insertOne(professor:Professor):
        professores.append(professor)