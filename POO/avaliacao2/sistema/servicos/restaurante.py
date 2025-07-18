from sistema.servicos.mesa import Mesa
from sistema.modelos.item_menu import ItemMenu

class Restaurante:
    """
    Representa o restaurante com suas coleções encapsuladas. [cite: 9]
    """
    def __init__(self, nome: str):
        self._nome = nome
        self._mesas = []
        self._cardapio = {}

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def mesas(self) -> list:
        return self._mesas.copy()
    
    @property
    def cardapio(self) -> dict:
        return self._cardapio.copy()

    def adicionar_item_cardapio(self, nome_item: str, item: ItemMenu):
        """Método público para adicionar um item ao cardápio interno."""
        self._cardapio[nome_item.lower()] = item

    def get_item_cardapio(self, nome_item: str) -> ItemMenu:
        """Método público para buscar um item do cardápio."""
        item = self._cardapio.get(nome_item.lower())
        if not item:
            raise ValueError("Item fora do cardápio.") 
        return item

    def adicionar_mesa(self, mesa: Mesa): 
        """Método público para adicionar uma mesa à lista interna."""
        self._mesas.append(mesa)
        print(f"Cadastrando mesa {mesa.numero}...")

    def listar_mesas_ocupadas(self): 
        """Lista as mesas com base na coleção interna de pedidos."""
        print("\nMesas ocupadas:")
        mesas_ocupadas = [m for m in self._mesas if m.pedidos]
        if not mesas_ocupadas:
            print("Nenhuma mesa ocupada no momento.")
        for mesa in mesas_ocupadas:
            print(f"- Mesa {mesa.numero}")