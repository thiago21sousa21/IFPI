class ItemMenu:
    """
    Superclasse que representa um item genérico do cardápio. 
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco(self):
        """
        Retorna o preço base do item.
        Este método será sobrescrito pelas subclasses. 
        """
        return self.preco

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"
