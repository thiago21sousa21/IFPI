# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre: 
# a) O maior elemento da lista e em que posição esse elemento se encontra; 
# b) O menor elemento da lista e em que posição esse elemento se encontra. 
import os
from random import randint
from functools import reduce
limpar_terminal = lambda: os.system("cls" if os.name=="nt" else "clear")
printar_com_msg = lambda msg, elemento: print(f"\n{msg} {elemento}")
gerar_lista = lambda qnt: [randint(0,100) for _ in range(qnt)]
encontrar_maior = lambda lista: meu_reduce(lambda a, e: e if e > a else a, lista, 0)
encontrar_menor = lambda lista: meu_reduce(lambda a, e: e if e < a else a, lista, lista[0])

def soma(a, b):
    return a + b

def meu_reduce(funcao, lista, valor_inicial):
    acumulador = valor_inicial
    for elemento in lista:
        acumulador =  funcao(acumulador, elemento)
    return acumulador

def meu_index(lista, elemeto):
    for idx, e in enumerate(lista):
        if e == elemeto:return idx


if __name__ == "__main__":
    limpar_terminal()
    #criando lista
    lista = gerar_lista(15)
    printar_com_msg("A lista criada é essa:\n", lista)
    #encontrando o mmaior
    maior = encontrar_maior(lista)
    printar_com_msg("O maior numero dessa lista é:",maior)
    printar_com_msg("O indice desse numero é:", meu_index(lista,maior))
    #encontrando o menor
    menor = encontrar_menor(lista)
    printar_com_msg("O menor numero dessa lista é:", menor)
    printar_com_msg("O indice desse numero é:", meu_index(lista, menor))



