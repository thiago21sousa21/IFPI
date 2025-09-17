class Professor:
    def __init__(self,*, nome, sobrenome, matricula, data_nascimento, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.email = email

    def return_dados(self):
        return [self.nome, self.sobrenome, self.data_nascimento, self.matricula, self.email]
