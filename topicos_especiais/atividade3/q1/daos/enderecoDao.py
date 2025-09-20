from models.endereco import Endereco
from dababase.simulacao_db import enderecos
from utils.abstracoes import Abstracao

class EnderecoDao:

    @staticmethod
    def getAll():
        return Abstracao.selectAllObjects(enderecos)

    @staticmethod
    def getOne(endereco:Endereco):
        for e in enderecos:
            if e.aluno.cpf == endereco.aluno.cpf:
                return [vars(e)]

    @staticmethod
    def deleteOne(endereco:Endereco):
        for idx, e in enumerate(enderecos):
            if e.aluno.cpf == endereco.aluno.cpf:
                del enderecos[idx]

    @staticmethod
    def insertOne(endereco:Endereco):
        enderecos.append(endereco)