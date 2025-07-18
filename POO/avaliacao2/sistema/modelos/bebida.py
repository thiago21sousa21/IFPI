from sistema.modelos.item_menu import ItemMenu

class Bebida(ItemMenu):
    """
    Subclasse encapsulada para Bebida. 
    """
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        tamanho_upper = tamanho.upper()
        if tamanho_upper not in ['P', 'M', 'G']:
            raise ValueError("Tamanho inválido. Use 'P', 'M' ou 'G'.")
        self._tamanho = tamanho_upper 

    @property
    def tamanho(self) -> str:
        return self._tamanho

    def calcular_preco(self) -> float: 
        """Sobrescreve o método para adicionar custo com base no tamanho."""
        preco_final = self._preco
        if self._tamanho == 'M':
            preco_final += 2.00
        elif self._tamanho == 'G':
            preco_final += 4.00
        return preco_final

    def __str__(self) -> str:
        preco_calculado = self.calcular_preco()
        return f"Bebida: {self._nome} (Tamanho: {self._tamanho}) - R$ {preco_calculado:.2f}"