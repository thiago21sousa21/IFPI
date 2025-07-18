from sistema.modelos.item_menu import ItemMenu

class Prato(ItemMenu):
    """
    Subclasse encapsulada para Prato.
    """
    def __init__(self, nome: str, preco: float, tempo_preparo: int):
        super().__init__(nome, preco)
        self._tempo_preparo = tempo_preparo 

    @property
    def tempo_preparo(self) -> int:
        return self._tempo_preparo

    def __str__(self) -> str:
        return f"Prato: {self._nome} (Tempo de preparo: {self._tempo_preparo} min) - R$ {self._preco:.2f}"
