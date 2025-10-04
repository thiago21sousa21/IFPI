# 1. Crie uma função chamada "encontrar_primos_gemeos" que receba um número inteiro 
# n como parâmetro e retorne uma lista contendo todos os pares de números primos 
# gêmeos  menores  que  n.  Os  números  primos  gêmeos  são  dois  números  primos 
# consecutivos que diferem em 2.

import os

os.system("clear")

def receber_inteiro():
    try:
        n = int(input("Digite um  numero inteiro: "))
        return n
    except ValueError as e:
        raise ValueError("você não digitou um numero inteiro!")


def continuar_pedindo():
    while True:
        try:
            num = receber_inteiro()
            return num
        except ValueError as e:
            print("Você precisa digitar um numero intiero! Tente de novo")


def verificar_se_e_primo(num:int):
    lista = []
    for n in range(num):
        if num % (n+1) == 0:
            lista.append(n+1)
    return len(lista) == 2


def pegar_todos_os_primos(num):
    lista = []
    for n in range(num):
        result = verificar_se_e_primo(n)
        if result:
            lista.append(n)
    return lista

def verifica_se_e_gemeo(lista:list):
    duplas = []
    for idx, n in enumerate(lista):
        if idx < 2:
            continue
        else:
            if lista[idx] - lista[idx-1] == 2:
                duplas.append((lista[idx] , lista[idx-1]))
    return duplas

print(verifica_se_e_gemeo(pegar_todos_os_primos(20)))