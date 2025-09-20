# Cada  aluno  possui  um  número  de  matrícula  único,  nome  completo,  CPF,  endereço 
# (composto por rua, número, bairro, cidade e CEP), além de uma data de nascimento e a 
# idade.
from .matricula import Matricula

class Aluno:
    def __init__(self,* ,matricula: Matricula, nome, cpf, data_nascimento, idade):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf # Espera-se que seja um dicionário com rua, número, bairro, cidade e CEP
        self.data_nascimento = data_nascimento
        self.idade = idade

    def __str__(self):
        return f"Aluno(matricula={self.matricula}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco}, data_nascimento={self.data_nascimento}, idade={self.idade})"