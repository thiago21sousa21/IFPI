from sistema.modelos.item_menu import ItemMenu
from sistema.modelos.cliente import Cliente

class Pedido:
    """
    Representa um pedido com cliente e itens encapsulados. 
    """
    def __init__(self, cliente: Cliente):
        self._cliente = cliente
        self._itens = []

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def itens(self) -> list:
        """Retorna uma cópia da lista para proteger a lista original."""
        return self._itens.copy()

    def adicionar_item(self, item: ItemMenu):
        """Método público para manipular a lista interna de itens."""
        if not isinstance(item, ItemMenu):
            raise TypeError("O item adicionado deve ser um Prato ou uma Bebida.")
        self._itens.append(item)

    def exibir_itens(self): 
        """Exibe os itens do pedido."""
        for item in self._itens:
            print(f"- {item}")