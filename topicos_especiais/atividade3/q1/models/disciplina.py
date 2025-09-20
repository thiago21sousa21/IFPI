# Cada disciplina possui um código único, nome, carga horária e ementa.
from models.professor import Professor
class Disciplina:
    def __init__(self,*, codigo, nome, carga_horaria, ementa, professor:Professor=None):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.ementa = ementa
        self.professor = professor

    def atribuir_professor(self, professor:Professor):
        self.professor = professor
  
    def __str__(self):
        return f"Disciplina(Código: {self.codigo}, Nome: {self.nome}, Carga Horária: {self.carga_horaria}, Ementa: {self.ementa})"