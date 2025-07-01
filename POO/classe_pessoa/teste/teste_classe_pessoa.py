from POO.classe_pessoa.classe_pessoa import Pessoa
import pytest


def test_casar():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    pessoa2 = Pessoa("Ana", 28, 55, 1.65, "Feminino")
    pessoa1.casar(pessoa2)
    assert pessoa1.conjuge == pessoa2
    assert pessoa2.conjuge == pessoa1
    assert pessoa1.est_civil == "casado"
    assert pessoa2.est_civil == "casado"

def test_morrer():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    pessoa1.morrer()
    assert pessoa1.estado == "morto"
    assert pessoa1.conjuge is None
    assert pessoa1.est_civil == "viúvo"

def test_divorciar():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    pessoa2 = Pessoa("Ana", 28, 55, 1.65, "Feminino")
    pessoa1.casar(pessoa2)
    pessoa1.divorciar()
    assert pessoa1.conjuge is None
    assert pessoa1.est_civil == "divorciado"
    assert pessoa2.est_civil == "divorciado"

def test_adoção():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    pessoa2 = Pessoa("Ana", 28, 55, 1.65, "Feminino", estado="vivo", est_civil="solteiro")
    pessoa1.adoção(pessoa2)
    assert pessoa1.mãe_adotiva == pessoa2
    assert pessoa2.filho_adotivo == pessoa1
    assert pessoa1.mãe is None
    assert pessoa1.pai is None 

def test_verificar_instancia():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    try:
        pessoa1.verificar_instancia("não é uma pessoa")
    except TypeError as e:
        assert str(e) == "Objeto não é uma instância de Pessoa"
    
    try:
        pessoa1.verificar_instancia(123)
    except TypeError as e:
        assert str(e) == "Objeto não é uma instância de Pessoa"
    
    assert isinstance(pessoa1, Pessoa)  # Verifica se pessoa1 é uma instância de Pessoa

def test_str():
    pessoa1 = Pessoa("João", 30, 80, 1.80, "Masculino")
    expected_str = f"""
        Nome: João
        Idade: 30
        Peso: 80
        Altura: 1.8
        Sexo: Masculino
        Estado: vivo
        Estado Civil: solteiro
        Mãe: Não informado
        Pai: Não informado
        Mãe Adotiva: Não informado
        Pai Adotivo: Não informado
        Cônjuge: Não informado
        """
    assert str(pessoa1) == expected_str.strip()
