from .item_menu import ItemMenu

class Prato(ItemMenu):
    """
    Subclasse que representa um prato, com um tempo de preparo específico.
    """
    def __init__(self, nome, preco, tempo_preparo):
        super().__init__(nome, preco)
        self.tempo_preparo = tempo_preparo

    def __str__(self):
        return f"Prato: {self.nome} (Tempo de preparo: {self.tempo_preparo} min) - R$ {self.preco:.2f}"

