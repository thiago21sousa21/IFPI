# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos 
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos 
# de S. Escrever a lista 

from random import randint
import os
from pprint import pprint

criar_lista = lambda qnt: [randint(-10, 10) for _ in range(qnt)]
limpar_terminal = lambda : os.system("cls" if os.name == "nt" else "clear")

# da pra usar concat - metodo
def usando_concat(l1:list, l2: list):
    l1.extend(l2)
    return l1

def usando_desempacotamento(l1:list, l2: list):
    return [*l1, *l2]

def minha_soma_de_lista(l1:list, l2:list):
    nova_lista = []
    for v in l1:
        nova_lista.append(v)
    for v in l2:
        nova_lista.append(v)
    return nova_lista

if __name__ == "__main__":
    limpar_terminal()
    lista1 = criar_lista(5)
    lista2 = criar_lista(10)
    lista_concatenada = minha_soma_de_lista(lista1, lista2)
    pprint(f"A lista 1 é:\n {lista1}\n A lista 2 é:\n {lista2}\n A lista concatenada é:\n{lista_concatenada}")
