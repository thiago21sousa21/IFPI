"""Testes para a classe Pedido."""
import pytest
from sistema.modelos.cliente import Cliente
from sistema.modelos.prato import Prato
from sistema.modelos.bebida import Bebida

# Criando um cliente e itens como fixtures para serem usados nos testes
@pytest.fixture
def dados_pedido():
    cliente = Cliente("Maria")
    prato = Prato("Salada Caesar", 22.00, 10)
    bebida = Bebida("Suco Natural", 8.00, "M")
    return {"cliente": cliente, "prato": prato, "bebida": bebida}

def test_inicializacao_pedido(dados_pedido):
    """
    Testa se um pedido é associado a um cliente no momento da criação
    """
    from sistema.servicos.pedido import Pedido
    cliente = dados_pedido["cliente"]
    pedido = Pedido(cliente)
    assert pedido.cliente == cliente
    assert len(pedido.itens) == 0

def test_adicionar_item_ao_pedido(dados_pedido):
    """
    Testa a adição de múltiplos itens a um pedido.
    """
    from sistema.servicos.pedido import Pedido
    pedido = Pedido(dados_pedido["cliente"])
    pedido.adicionar_item(dados_pedido["prato"])
    pedido.adicionar_item(dados_pedido["bebida"])
    
    assert len(pedido.itens) == 2
    assert pedido.itens[0].nome == "Salada Caesar"
    assert pedido.itens[1].nome == "Suco Natural"

def test_excecao_adicionar_item_invalido(dados_pedido):
    """
    Testa se o sistema levanta uma exceção ao tentar adicionar um objeto inválido como item
    """
    from sistema.servicos.pedido import Pedido
    pedido = Pedido(dados_pedido["cliente"])
    item_invalido = "não sou um item de menu"
    
    with pytest.raises(TypeError):
        pedido.adicionar_item(item_invalido)

def test_exibir_itens_pedido(dados_pedido, capsys):
    """
    Testa o método para exibir os itens do pedido
    """
    from sistema.servicos.pedido import Pedido
    pedido = Pedido(dados_pedido["cliente"])
    pedido.adicionar_item(dados_pedido["prato"])
    pedido.adicionar_item(dados_pedido["bebida"])
    
    pedido.exibir_itens()
    captured = capsys.readouterr()
    
    assert "Prato: Salada Caesar" in captured.out
    assert "Bebida: Suco Natural" in captured.out