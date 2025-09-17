# 5)  Faça  um  programa  que  leia  duas  listas  de  10  elementos  
# numéricos  cada  um  e  intercale  os 
# elementos deste em uma outra lista de 20 elementos. 
import os
from random import randint

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir_com_msg = lambda msg, elemento: print(f"\n{msg} {elemento}")
criar_lista = lambda qnt : [randint(0,100) for _ in range(qnt)]

def intercalar_listas(l1, l2):
    nova_lista = list()
    for idx, e in enumerate(l1):
        nova_lista.append(e)
        nova_lista.append(l2[idx])
    return nova_lista

if __name__ == "__main__":
    limpar_terminal()
    #criando primeira lista
    lista1 = criar_lista(10)
    imprimir_com_msg("A lista 1 foi criada:\n", lista1)
    #criando segunda lista
    lista2 = criar_lista(10)
    imprimir_com_msg("A lista 2 foi criada:\n", lista2)
    #criando lista intercadada
    listao = intercalar_listas(lista1, lista2)
    imprimir_com_msg("A lista intercalada foi criada:\n", listao)
    imprimir_com_msg("A lista inercalada tem", f"{len(listao)} elemtos")




