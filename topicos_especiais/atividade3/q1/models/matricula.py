# Cada matrícula guarda o semestre/ano em que foi realizada, o número de faltas do aluno 
# na disciplina e a nota final do aluno naquela disciplina.

class Matricula:
    def __init__(self,*, semestre_ano, num_faltas=0, nota_final=None, id=None):
        self.id = id
        self.semestre_ano = semestre_ano
        self.num_faltas = num_faltas
        self.nota_final = nota_final

    def __str__(self):
        return f"Matrícula(Semestre/Ano: {self.semestre_ano}, Número de Faltas: {self.num_faltas}, Nota Final: {self.nota_final})"