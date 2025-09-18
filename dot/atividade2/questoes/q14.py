# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. 
# Escrever a lista C modificada.

from random import randint
import os

def criar_lista(qnt):
    return [randint(-10, 10) for _ in range(qnt)]

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def trocar_por_zero(lista):
    nova_lista = []
    for v in lista:
        if v < 0:
            nova_lista.append(0)
        else:
            nova_lista.append(v)
    return nova_lista

if __name__ == "__main__":
    limpar_terminal()
    lista = criar_lista(20)
    print("A primeira lista e:\n")
    print(lista)
    nova = trocar_por_zero(lista)
    print("\nA segunda lista  é:\n")
    print(nova)

