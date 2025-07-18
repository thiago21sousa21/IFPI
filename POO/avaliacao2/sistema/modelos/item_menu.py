class ItemMenu:
    """
    Superclasse encapsulada para um item do cardápio.
    """
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco

    def calcular_preco(self) -> float:
        """Retorna o preço base. Será sobrescrito nas subclasses."""
        return self._preco

    def __str__(self) -> str:
        return f"{self._nome} (R$ {self._preco:.2f})"