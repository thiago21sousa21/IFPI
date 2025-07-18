"""Testes para a classe Cliente."""
from sistema.modelos.cliente import Cliente

def test_inicializacao_cliente():
    """
    Testa a criação de um cliente, garantindo que o nome é armazenado corretamente
    """
    cliente = Cliente(nome="Rogério")
    assert cliente.nome == "Rogério"
    assert str(cliente) == "Rogério"