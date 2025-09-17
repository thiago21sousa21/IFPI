# ) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e: 
# a) Mostre a quantidade de números pares; 
# b) Grave uma lista somente com os números pares e mostre a lista; 
# c) Mostre a quantidade de números ímpares;
from random import randint
def ficar_lendo_inteiro(msg = "Digite por favor um número inteiro: "):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Você precisa digitar um número inteiro!")

def ficar_enchendo_lista():
    #como a questão pede 100 numeros
    #qnt_numeros = ficar_lendo_inteiro()
    qnt_numeros = 100
    lista = []
    while len(lista) < qnt_numeros:
        try:
            #pra ficar mais rápido
            #lista.append(int(input(f"Digite o {len(lista)+1}° numero: ")))
            lista.append(randint(0,100))
        except ValueError as err:
            print("Você precisa digitar um número inteiro")
        except KeyboardInterrupt :
            raise("Pograma encerado pelo usuário")
    return lista

def separar_par_impar(lista:list)->dict:
    lista_pares = []
    lista_impares = []
    for elemento in lista:
        lista_pares.append(elemento) if elemento % 2 == 0 else lista_impares.append(elemento)
    return{"pares": lista_pares, "impares": lista_impares}

if __name__ == "__main__":
    lista = ficar_enchendo_lista()
    listas = separar_par_impar(lista)
    print("Mostrando os pares:")
    print(listas["pares"])
    print(f"quantidade: {len(listas["pares"])}")
    print("Mostrando os impares:")
    print(listas["impares"])
    print(f"quantidade: {len(listas["impares"])}")