from ..modelos.item_menu import ItemMenu

class Pedido:
    """
    Representa um pedido feito por um cliente, contendo itens do cardápio.
    """
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item: ItemMenu):
        """Adiciona um item ao pedido."""
        if not isinstance(item, ItemMenu):
            raise TypeError("O item adicionado deve ser um Prato ou uma Bebida.")
        self.itens.append(item)

    def exibir_itens(self):
        """Exibe os itens do pedido."""
        for item in self.itens:
            print(f"- {item}")