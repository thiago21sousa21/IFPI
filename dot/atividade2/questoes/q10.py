# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

import os
from random import randint

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir = lambda msg: print(f"\n{msg}")
gerar_lista = lambda qnt: [randint(0,100) for _ in range(qnt)]

def meu_max(lista:list):
    maior = 0
    for idx, valor in enumerate(lista):
        if valor > lista[maior]:
            maior = idx
    return {"valor": lista[maior], "indece": maior}

def meu_min(lista:list):
    menor = 0
    for idx, valor in enumerate(lista):
        if valor < lista[menor]:
            menor = idx
    return {"valor": lista[menor], "indece": menor}


if __name__ == "__main__":
    limpar_terminal()
    lista = gerar_lista(15)
    print(f"\nA lista é:\n {lista}")
    maior = meu_max(lista)
    menor = meu_min(lista)
    print(f"\no maior valor com sua posição é: \n {maior}")
    print(f"\no menor valor com sua posição é: \n {menor}")


