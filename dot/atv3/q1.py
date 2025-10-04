import math

def receber_inteiro():
    while True:        
        try:
            n = int(input("Digite o número inteiro: "))
            return n
        except ValueError:
            print("Você precisa digitar um número inteiro!")

def gerar_primos(num: int):
    for n in range(2, num): 
        cont = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cont += 1
                break 
        if cont == 0:  
            yield n

def encontrar_primos_gemeos(n: int):
    primos = gerar_primos(n)
    ultimo_primo = None
    for primo in primos:
        if ultimo_primo is not None and primo - ultimo_primo == 2:
            yield (ultimo_primo, primo)
        ultimo_primo = primo  

def mostrar(iteravel):
    for e in iteravel:
        print(e)

if __name__ == "__main__":
    n = receber_inteiro() 
    primos_gemeos = encontrar_primos_gemeos(n) 
    mostrar(primos_gemeos)  