# ● Cada professor possui um identificador único, nome completo, e-mail e titulação (ex.:
# Mestre, Doutor). Um professor pode ministrar várias disciplinas, mas cada disciplina é
# ministrada por apenas um professor.

class Professor:
    def __init__(self,*, id_professor, nome_completo, email, titulacao):
        self.id_professor = id_professor
        self.nome_completo = nome_completo
        self.email = email
        self.titulacao = titulacao

    def __str__(self):
        return f"Professor(ID: {self.id_professor}, Nome: {self.nome_completo}, Email: {self.email}, Titulação: {self.titulacao})"