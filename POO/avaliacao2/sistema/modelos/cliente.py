class Cliente:
    """
    Representa um cliente do restaurante.
    """
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
