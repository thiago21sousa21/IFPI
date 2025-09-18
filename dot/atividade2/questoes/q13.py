# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o 
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de 
# cada face.

from random import randint
import os

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")

criar_lista = lambda qnt: [randint(1,6) for _ in range(qnt)]

def contar_jogads(lista:list):
    faces = [0] * 6
    for lado in lista:
        faces[lado-1] +=1
    return faces

def explicar_mais_bonito(lista):
    for idx, valor in enumerate(lista):
        print(f'o lado {idx+1} apareceu {valor} vezes')

if __name__ == "__main__":
    limpar_terminal()
    lista = criar_lista(1000)
    print(lista)
    lados = contar_jogads(lista)
    print(lados)
    explicar_mais_bonito(lados)