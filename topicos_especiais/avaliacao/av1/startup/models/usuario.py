class Usuario:
    def __init__(self, nome_completo, email, data_narcimento, idade=None, id = None):
        self.nome_completo = nome_completo
        self.email = email
        self.data_nascimento = data_narcimento
        self.idade = idade
        self.id = id
        self.numeros = []
    