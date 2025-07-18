"""Testes para a classe Mesa."""
import pytest
from sistema.servicos.mesa import Mesa
from sistema.modelos.cliente import Cliente
from sistema.modelos.prato import Prato
from sistema.modelos.bebida import Bebida

@pytest.fixture
def dados_mesa():
    """Fixture para popular a mesa com dados dos exemplos do documento."""
    return {
        "mesa": Mesa(5),
        "joao": Cliente("João"),
        "maria": Cliente("Maria"),
        "hamburguer": Prato("Hambúrguer", 25.00, 15),
        "refrigerante": Bebida("Refrigerante", 4.00, "G"),
        "salada": Prato("Salada Caesar", 22.00, 10),
        "suco": Bebida("Suco Natural", 8.00, "M"),
    }

def test_registrar_multiplos_pedidos(dados_mesa, capsys):
    """
    Testa o registro de múltiplos pedidos de diferentes clientes em uma mesa
    """
    mesa = dados_mesa["mesa"]
    
    # Pedido do João
    mesa.registrar_pedido(dados_mesa["joao"], [dados_mesa["hamburguer"], dados_mesa["refrigerante"]])
    # Pedido da Maria
    mesa.registrar_pedido(dados_mesa["maria"], [dados_mesa["salada"], dados_mesa["suco"]])
    
    captured = capsys.readouterr().out
    assert "Cliente João fez um pedido na mesa 5" in captured 
    assert "Cliente Maria fez um pedido na mesa 5" in captured 
    assert len(mesa.pedidos) == 2

def test_calcular_total_mesa(dados_mesa):
    """
    Testa o cálculo do valor total da conta da mesa
    """
    mesa = dados_mesa["mesa"]
    
    # Testa com a mesa vazia
    assert mesa.calcular_total() == 0
    
    # Adiciona pedidos
    mesa.registrar_pedido(dados_mesa["joao"], [dados_mesa["hamburguer"], dados_mesa["refrigerante"]]) # 25 + 8 = 33
    mesa.registrar_pedido(dados_mesa["maria"], [dados_mesa["salada"], dados_mesa["suco"]]) # 22 + 10 = 32
    
    # Total esperado 33 + 32 = 65
    assert mesa.calcular_total() == 65.00

def test_imprimir_conta_detalhada_polimorfico(dados_mesa, capsys):
    """
    Testa o método polimórfico que imprime os detalhes da conta, conforme exemplo
    """
    mesa = dados_mesa["mesa"]
    mesa.registrar_pedido(dados_mesa["joao"], [dados_mesa["hamburguer"], dados_mesa["refrigerante"]])
    mesa.registrar_pedido(dados_mesa["maria"], [dados_mesa["salada"], dados_mesa["suco"]])
    
    mesa.imprimir_conta_detalhada()
    output = capsys.readouterr().out

    assert "Resumo da mesa 5:" in output 
    assert "João: Hambúrguer (R$ 25.00), Refrigerante G (R$ 8.00)" in output 
    assert "Maria: Salada Caesar (R$ 22.00), Suco Natural M (R$ 10.00)" in output 
    assert "Total: R$ 65.00" in output 