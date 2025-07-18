from ..modelos.item_menu import ItemMenu
from .mesa import Mesa

class Restaurante:
    """
    Representa o restaurante, contendo várias mesas.
    """
    def __init__(self, nome):
        self.nome = nome
        self.mesas = []
        self.cardapio = {} # Para facilitar a busca de itens

    def adicionar_item_cardapio(self, nome, item: ItemMenu):
        """Adiciona um item ao cardápio do restaurante."""
        self.cardapio[nome.lower()] = item

    def get_item_cardapio(self, nome):
        """Busca um item no cardápio."""
        item = self.cardapio.get(nome.lower())
        if not item:
            raise ValueError("Item fora do cardápio.") # Exceção para item inválido [cite: 47]
        return item

    def adicionar_mesa(self, mesa: Mesa):
        """
        Adiciona uma nova mesa ao restaurante.
        """
        self.mesas.append(mesa)
        print(f"Cadastrando mesa {mesa.numero}...")

    def listar_mesas_ocupadas(self):
        """
        Lista todas as mesas que possuem pedidos.
        """
        print("\nMesas ocupadas:")
        mesas_ocupadas = [m for m in self.mesas if m.pedidos]
        if not mesas_ocupadas:
            print("Nenhuma mesa ocupada no momento.")
        for mesa in mesas_ocupadas:
            print(f"- Mesa {mesa.numero}")