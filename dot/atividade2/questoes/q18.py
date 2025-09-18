# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para 
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R. 

from random import randint
import os

criar_lista = lambda qnt: [randint(-10, 10) for _ in range(qnt)]
limpar_terminal = lambda : os.system("cls" if os.name == "nt" else "clear")
imprimir = lambda msg: print(f"\n{msg}")
buscar_valor = lambda: input("Digite um valor a ser buscado na lista")



filtrar_negativos = lambda lista: [ num for num in lista if num < 0]

if __name__ == "__main__":
    limpar_terminal()
    lista = criar_lista(10)
    print(f"A lista foi criada:\n {lista}")
    negativos = filtrar_negativos(lista)
    print(f"os negativos são:\n {negativos}")