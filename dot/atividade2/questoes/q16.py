# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os 
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os 
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

import os
from random import randint

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir = lambda msg: print(f"\n{msg}")
gerar_lista = lambda qnt: [randint(0,100) for _ in range(qnt)]
nova_lista = lambda lista: list(map(lambda e: e/2 if e %2 == 0 else e *3, lista))




# def meu_map(func, lista):
#     nova_lista = []
#     for elemento in lista:
#         nova_lista.append(func(elemento))
#     return nova_lista
meu_map = lambda lista: [( lambda e: e / 2 if e %2 == 0 else e * 3)(elemento) for elemento in lista]

if __name__ == "__main__":
    limpar_terminal()
    X = gerar_lista(10)
    Y = nova_lista(X)
    Z = meu_map(X)
    imprimir(f"A lista origina é:\n {X}")
    imprimir(f"A nova lista lista é:\n {Z}")


