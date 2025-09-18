# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o 
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V 
# aparece. 
from random import randint
import os

criar_lista = lambda qnt: [randint(1,3) for _ in range(qnt)]
limpar_terminal = lambda : os.system("cls" if os.name == "nt" else "clear")
imprimir = lambda msg: print(f"\n{msg}")
buscar_valor = lambda: input("Digite um valor a ser buscado na lista")

def meu_enumarate_func(lista):
    nova_lista = []
    indice = 0
    for valor in lista:
        nova_lista.append((indice, valor))
        indice+=1
    return nova_lista


filtrar = lambda lista, valor: list(filter(lambda e: e[1] == valor, lista))

def tentar_converter(valor):
    try:
        valor = int(valor)
        return valor
    except:
        return valor

if __name__ == "__main__":
    limpar_terminal()
    lista = criar_lista(10)
    imprimir(f"A lista é  :\n{lista}")
    enum = meu_enumarate_func(lista)
    imprimir(f"meu enumerate deu:\n {enum}")
    valor = tentar_converter(input("Digite um valor a ser procurado na lista"))
    filtrados = filtrar(enum, valor)
    print(f"ou seja, o valor a ser procurado na lista é: {valor}")
    ocorrencias = len(filtrados)
    if ocorrencias == 0:
        print("não foi encontrado esse valor na lista")
    else:
        imprimir(f"A lista dos filtrados deu:\n {filtrados}")
        print("Ou seja")
        print(f"foram achadas {ocorrencias} ocorrencias nas posições ", end="")
        for v in filtrados:
            print(f"{v[0]}", end= " ")


