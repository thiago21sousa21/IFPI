"""Testes para a classe Restaurante."""
import pytest
from sistema.servicos.restaurante import Restaurante
from sistema.servicos.mesa import Mesa
from sistema.modelos.prato import Prato
from sistema.modelos.cliente import Cliente

@pytest.fixture
def setup_restaurante():
    """Fixture que cria um restaurante com mesas e cardápio."""
    restaurante = Restaurante("IFPI Cantina")
    mesa5 = Mesa(5)
    mesa7 = Mesa(7)
    
    # Adiciona itens ao cardápio
    restaurante.adicionar_item_cardapio("Filé Mignon", Prato("Filé Mignon", 55.00, 30))
    
    return {
        "restaurante": restaurante,
        "mesa5": mesa5,
        "mesa7": mesa7
    }

def test_adicionar_mesa_ao_restaurante(setup_restaurante, capsys):
    """
    Testa a adição de uma nova mesa ao restaurante
    """
    restaurante = setup_restaurante["restaurante"]
    mesa10 = Mesa(10)
    restaurante.adicionar_mesa(mesa10)
    
    assert mesa10 in restaurante.mesas
    assert "Cadastrando mesa 10" in capsys.readouterr().out

def test_get_item_cardapio_excecao(setup_restaurante):
    """
    Testa se uma exceção é levantada ao buscar um item que não está no cardápio
    """
    restaurante = setup_restaurante["restaurante"]
    with pytest.raises(ValueError, match="Item fora do cardápio."):
        restaurante.get_item_cardapio("Item que não existe")

def test_listar_mesas_ocupadas(setup_restaurante, capsys):
    """
    Testa a listagem de mesas que estão ocupadas
    """
    restaurante = setup_restaurante["restaurante"]
    mesa5 = setup_restaurante["mesa5"]
    mesa7 = setup_restaurante["mesa7"]
    
    restaurante.adicionar_mesa(mesa5)
    restaurante.adicionar_mesa(mesa7)
    
    # Antes de qualquer pedido
    restaurante.listar_mesas_ocupadas()
    output1 = capsys.readouterr().out
    assert "Nenhuma mesa ocupada no momento." in output1
    
    # Adiciona um pedido à mesa 7
    cliente_pedro = Cliente("Pedro")
    item = restaurante.get_item_cardapio("Filé Mignon")
    mesa7.registrar_pedido(cliente_pedro, [item])
    
    # Depois de um pedido
    restaurante.listar_mesas_ocupadas()
    output2 = capsys.readouterr().out
    assert "Mesas ocupadas:" in output2
    print(output2)
    assert "- Mesa 7" in output2
    assert "- Mesa 5" not in output2