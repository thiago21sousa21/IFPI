# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.

import os
from random import randint

limpar_terminal = lambda : os.system("cls" if os.name == "nt" else "clear")
gerar_lisa_numerada = lambda qnt: [randint(0,15) for _ in range(qnt)]
imprimir_com_msg = lambda msg, elemento: print(f"\n{msg} {elemento}")

def meu_in(*,lista:list, valor:int):
    for numero in lista:
        if valor == numero:
            return True
    return False

if __name__ == "__main__":
    limpar_terminal()
    lista = gerar_lisa_numerada(10)
    valor = randint(0, 15)
    isElementInLista = meu_in(lista=lista, valor= valor)
    imprimir_com_msg(f"O valor {valor} se encontra na lista abaixo?\n {lista}\n {"SIM" if isElementInLista else "NAO"}", "")
    