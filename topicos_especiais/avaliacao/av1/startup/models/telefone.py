from models.usuario import Usuario
class Telefone:
    def __init__(self, numero , usuario: Usuario, id = None):
        self.id = id
        self.numero = numero
        self.usuario = usuario
