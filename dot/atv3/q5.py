# 5. Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro 
# como parâmetro e retorne True se o ano for bissexto, e False caso contrário. Um ano é 
# bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400. 


import os

limpar_termial = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def pegar_inteiro():
    while True:
        try:
            n = input("Digie um número inteiro: ")
            return int(n)
        except ValueError:
            print(f"Você precisa digitar um número inteiro '{n}' não é um inteiro!")

def verificar_ano_bissexto(ano: int):
    if ano % 4 == 0 and ( ano % 100 != 0 or ano % 400 == 0):
        return True
    return False

if __name__ == '__main__':
    limpar_termial()
    ano = pegar_inteiro()
    isBissexto = verificar_ano_bissexto(ano)

    print(("Sim " if isBissexto else "Não" )+ ", ano " + f"{ano}" + (" é " if isBissexto else " não é ") + "bissexto")