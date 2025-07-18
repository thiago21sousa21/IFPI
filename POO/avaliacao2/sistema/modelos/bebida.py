from .item_menu import ItemMenu

class Bebida(ItemMenu):
    """
    Subclasse que representa uma bebida, com um tamanho específico.
    """
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        # Validação do tamanho da bebida
        if tamanho.upper() not in ['P', 'M', 'G']:
            raise ValueError("Tamanho inválido. Use 'P', 'M' ou 'G'.")
        self.tamanho = tamanho.upper()

    def calcular_preco(self):
        """
        Sobrescreve o método para adicionar um custo extra com base no tamanho. 
        - Tamanho 'M' tem um acréscimo de R$ 2.00
        - Tamanho 'G' tem um acréscimo de R$ 4.00
        """
        preco_final = self.preco
        if self.tamanho == 'M':
            preco_final += 2.00
        elif self.tamanho == 'G':
            preco_final += 4.00 # Exemplo de variação de preço
        return preco_final

    def __str__(self):
        # Gera uma representação em string para a bebida, mostrando o preço calculado.
        preco_calculado = self.calcular_preco()
        return f"Bebida: {self.nome} (Tamanho: {self.tamanho}) - R$ {preco_calculado:.2f}"
