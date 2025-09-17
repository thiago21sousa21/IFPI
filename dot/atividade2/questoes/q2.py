# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade 
# de números negativos e a soma dos números positivos dessa lista.
from random import random, randint
from functools import reduce

gerar_lista = lambda qnt: [round(randint(-100,100)*random(), 2) for _ in range(qnt)]
pegar_negativos = lambda lista : list(filter(lambda elemento: elemento < 0, lista ))
pegar_positivos = lambda lista : list(filter(lambda elemento: elemento > 0, lista ))
somar_lista = lambda lista: reduce(lambda a, e: a + e, lista, 0)
printar_com_msg = lambda msg, elemento: print(f"\n\n{msg}{elemento}")


if __name__ == "__main__":
    lista = gerar_lista(10)
    negativos = pegar_negativos(lista)
    positivos = pegar_positivos(lista)
    printar_com_msg("Primeiro vou mostar a lista:\n", lista)
    printar_com_msg("Agora vamos ver os negativos:\n",negativos)
    printar_com_msg("A quantiade de negativos: ", len(negativos))
    printar_com_msg("Vamos ver agora os numeros positivos:\n", positivos)
    printar_com_msg("A soma dos positivos é: ", somar_lista(positivos))

