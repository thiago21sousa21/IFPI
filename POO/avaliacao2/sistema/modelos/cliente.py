class Cliente:
    """
    Representa um cliente com seus dados encapsulados.
    """
    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    def __str__(self) -> str:
        return self._nome