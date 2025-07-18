"""Testes para a subclasse Bebida."""
import pytest
from sistema.modelos.bebida import Bebida

def test_inicializacao_bebida():
    """
    Testa se a Bebida é criada com seus atributos, como o tamanho[cite: 23].
    """
    bebida = Bebida(nome="Refrigerante", preco=4.00, tamanho="G")
    assert bebida.nome == "Refrigerante"
    assert bebida.preco == 4.00
    assert bebida.tamanho == "G"

def test_calcular_preco_bebida_sobrescrito_com_variacao():
    """
    Testa o método 'calcular_preco' sobrescrito, considerando as variações de preço
    """
    bebida_p = Bebida("Água", 3.00, "P")
    bebida_m = Bebida("Suco Natural", 8.00, "M")
    bebida_g = Bebida("Vinho Tinto", 36.00, "G")

    assert bebida_p.calcular_preco() == 3.00  # Preço base para P
    assert bebida_m.calcular_preco() == 10.00 # Preço com adicional para M
    assert bebida_g.calcular_preco() == 40.00 # Preço com adicional para G

def test_representacao_str_bebida():
    """
    Testa a formatação da string de saída, conforme exemplo do documento
    """
    bebida = Bebida(nome="Suco Natural", preco=8.00, tamanho="M")
    # A string deve refletir o preço final calculado
    esperado = "Bebida: Suco Natural (Tamanho: M) - R$ 10.00"
    assert str(bebida) == esperado

def test_excecao_tamanho_invalido_bebida():
    """
    Testa o tratamento de exceções para casos de dados inválidos
    """
    with pytest.raises(ValueError, match="Tamanho inválido"):
        Bebida("Bebida Ruim", 1.00, "XPTO")