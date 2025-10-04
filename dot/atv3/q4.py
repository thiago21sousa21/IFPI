# 4. Crie uma função chamada "contar_divisores" que receba um número inteiro como 
# parâmetro e retorne a quantidade de divisores desse número.

def receber_inteiro():
    while True:
        try:
            n = input("Digite um número inteiro: ")
            n = int(n)
            return n
        except ValueError:
            print(f"Você precisa digitar um número inteiro! '{n}' não é numero inteiro!")

def contar_divisores(n: int):
    for e in range(1,n+1):
        if n % e == 0:
            yield e

def mostra(iterador):
    for e in iterador:
        print(e)

if __name__ == "__main__":
    n = receber_inteiro()
    divisores = contar_divisores(n)
    mostra(divisores)