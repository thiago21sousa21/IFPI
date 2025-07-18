"""Testes para a superclasse ItemMenu."""
from sistema.modelos.item_menu import ItemMenu

def test_inicializacao_item_menu():
    """
    Testa a criação de um item genérico do cardápio
    """
    item = ItemMenu(nome="Item Genérico", preco=10.50)
    assert item.nome == "Item Genérico"
    assert item.preco == 10.50

def test_calcular_preco_item_menu():
    """
    Testa o método base de cálculo de preço
    """
    item = ItemMenu(nome="Item Base", preco=99.00)
    assert item.calcular_preco() == 99.00

def test_representacao_str_item_menu():
    """
    Testa a representação em string do item.
    """
    item = ItemMenu(nome="Item", preco=15.00)
    assert str(item) == "Item (R$ 15.00)"