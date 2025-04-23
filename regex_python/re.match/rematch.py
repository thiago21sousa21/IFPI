import re

def exer1(padrao):
    """ Verifique se a string começa com a palavra "Olá"."""
    texto = "Olá, mundo!"
    resultado = re.match(rf"{padrao}", texto)
    print("Match encontrado" if resultado else "Sem match")
#exer1("ola")

def exer2(padrao='wrong'):
    """📍Exercício 2 – Começa com letra maiúscula"""
    texto = "Python é incrível"
    resultado = re.match(rf"{padrao}", texto)
    print("Match encontrado" if resultado else "Sem match")
    print(resultado)
#exer2('[A-Z]')

def exer3(padrao = 'wrong'):
    """ Verifique se a string começa com um número inteiro ou decimal."""
    texto = "123 é a resposta"
    resultado = re.match(rf"{padrao}", texto)
    print("Match encontrado" if resultado else "Sem match")
#exer3("^[0-9]+(\.[0-9]+)?")

def exer4(padrao = 'wrong'):
    """Verifique se o CEP digitado é válido no formato XXXXX-XXX (5 números, hífen, 3 números)."""
    cep = '12345-678'
    resultado = re.match(rf'{padrao}',cep)
    print("cep válido " if resultado else "cep inválido")
exer4('\d{5}-\d{3}')

def exer5(padrao = 'wrong'):
    """ Verifique se a string começa com a palavra "Item" seguida de um número qualquer (ex: Item23)."""
    texto = " Item23 disponível no estoque"
    resultado = re.match(rf"{padrao}", texto)
    print("formato correto" if resultado else "formato incorreto")
#exer5('[a-zA-Z0-9]')

def exer6(padrao = "wrong"):
    """A string pode começar com "Sr." ou "Sra.", seguido de um espaço e um nome. Verifique se o padrão é seguido corretamente."""
    texto = "Sra. Silva"
    resultado = re.match(rf"{padrao}", texto)
    print("Nome com titulo válido " if resultado else "padrão inválido")
#exer6("Sra")

