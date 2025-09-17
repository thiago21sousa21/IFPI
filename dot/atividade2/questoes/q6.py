# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, 
# elabore um 
# programa  que  calcule  e  exiba  o faturamento que  é igual a  quantidade  x preço. 
# Calcule  e exiba 
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos 
# e quantos faturamentos estão abaixo da média. 

import os
from faker import Faker
from random import randint, random
#from functools import reduce

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir_com_msg = lambda msg, elemento: print(f"\n{msg} {elemento}")
gerar_nomes_produtos = lambda qnt: [Faker().name() for _ in range(qnt)]
gerar_quantidades = lambda qnt: [randint(1, 10) for _ in range(qnt)]
gerar_valores_aleatorios = lambda qnt: [round(10 + 90*random(), 2) for _ in range(qnt)]
calcular_faturamento = lambda qnt, preco: [round(qnt[i]*preco[i],2) for i in range(len(qnt))]
soma_total = lambda lista: meu_reduce(lambda a, e: a+e, lista, 0)
media_faturamento = lambda soma_total, qnt_vendida: soma_total/qnt_vendida
produtos_abaixo_media = lambda lista, media: list(filter(lambda e: e < media, lista))


def meu_sum(lista):
    acc = 0
    for v in lista:
        acc+=v
    return acc

def meu_reduce(func, lista, v_init):
    acc = v_init
    for elemento in lista:
        acc = func(acc, elemento)
    return acc




if __name__ == "__main__":
    limpar_terminal()
    quantidade = 5
    #gerar nomes para os produtos
    nomes = gerar_nomes_produtos(quantidade)
    imprimir_com_msg("Aqui estão os nomes dos produtos:\n", nomes)
    #gerar a quantidade de cada produto
    quantidades = gerar_quantidades(quantidade)
    imprimir_com_msg("Aqui esta a quantidade vendida de cada produto:\n", quantidades)
    #gerar valor individual de cada produto
    valores = gerar_valores_aleatorios(quantidade)
    imprimir_com_msg("Aqui esta o valor unitário de cada produto", valores)
    #calcular o faturamento de cada produto
    faturamentos = calcular_faturamento(quantidades, valores)
    imprimir_com_msg("Aqui esta o valor total vendido de cada protudo:\n", faturamentos)
    #calcular total  falturado
    tota_faturado = soma_total(faturamentos)
    imprimir_com_msg("Aqui está o valor total vendido considerando todos os faturamentos: ", tota_faturado)
    #calcular a media de faturamento
    media = media_faturamento(tota_faturado, len(quantidades))
    imprimir_com_msg("A média de faturamento de cada produto é: ", media)
    #calcular produtos abaixo da media
    produtos_abaixo = produtos_abaixo_media(faturamentos, media)
    imprimir_com_msg(f"Os faturamentos que estão abaixo da media {media} são:\n", produtos_abaixo)



