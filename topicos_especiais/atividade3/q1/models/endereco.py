from models.matricula import Matricula
from models.aluno import Aluno

class Endereco:
    def __init__(self,*,rua=None, numero=None, bairro=None,cidade, estado, cep, aluno: Aluno):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.bairro = bairro
        self.aluno = aluno

    def __str__(self):
        return f"Endereco(rua={self.rua}, numero={self.numero}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}, cep={self.cep})"

    def to_tuple(self):
        return (self.rua, self.numero, self.bairro, self.cidade, self.estado, self.cep)