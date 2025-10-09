class Usuario:
    def __init__(self, nome_completo, email, data_nascimento, idade=None, id = None):
        self.nome_completo = nome_completo
        self.email = email
        self.data_nascimento = data_nascimento
        self.idade = idade
        self.id = id
        self.numeros = []
    