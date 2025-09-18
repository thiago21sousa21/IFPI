# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem 
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim 
# por diante. Escrever todo a lista D e todo a lista E.

# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

import os
from random import randint

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir = lambda msg: print(f"\n{msg}")
gerar_lista = lambda qnt: [randint(0,100) for _ in range(qnt)]

def meu_reversed(lista:list):
    lista_reversa = []
    for idx, valor in enumerate(lista):
        lista_reversa.append(lista[len(lista)-1-idx])
    return lista_reversa



if __name__ == "__main__":
    limpar_terminal()
    X = gerar_lista(10)
    Y = meu_reversed(X)
    imprimir(f"A lista origina é:\n {X}")
    imprimir(f"A lista reversa é:\n {Y}")


