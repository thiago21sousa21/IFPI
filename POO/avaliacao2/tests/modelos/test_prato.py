"""Testes para a subclasse Prato."""
from sistema.modelos.prato import Prato

def test_inicializacao_prato():
    """
    Testa se o Prato é criado com seus atributos específicos, como o tempo_preparo[cite: 22].
    """
    prato = Prato(nome="Hambúrguer", preco=25.00, tempo_preparo=15)
    assert prato.nome == "Hambúrguer"
    assert prato.preco == 25.00
    assert prato.tempo_preparo == 15

def test_calcular_preco_prato_sobrescrito():
    """
    Testa o método 'calcular_preco' sobrescrito na classe Prato[cite: 40].
    """
    prato = Prato(nome="Salada Caesar", preco=22.00, tempo_preparo=10)
    # No caso do Prato, o preço não tem variação extra.
    assert prato.calcular_preco() == 22.00

def test_representacao_str_prato():
    """
    Testa a formatação da string de saída, conforme exemplo do documento[cite: 52].
    """
    prato = Prato(nome="Filé Mignon", preco=55.00, tempo_preparo=30)
    esperado = "Prato: Filé Mignon (Tempo de preparo: 30 min) - R$ 55.00"
    assert str(prato) == esperado