from models.disciplina import Disciplina
from utils.abstracoes import Abstracao
from dababase.simulacao_db import disciplinas
class DisciplinaDao:

    @staticmethod
    def getAll():
        return Abstracao.selectAllObjects(disciplinas)

    @staticmethod
    def getOne(disciplina:Disciplina):
        for d in disciplinas:
            if d.codigo == disciplina.codigo:
                return [vars(d)]

    @staticmethod
    def deleteOne(disciplina:Disciplina):
        for idx, d in enumerate(disciplinas):
            if d.codigo == disciplina.codigo:
                del disciplinas[idx]

    @staticmethod
    def insertOne(disciplina:Disciplina):
        disciplinas.append(disciplina)