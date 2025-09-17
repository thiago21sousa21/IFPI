# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

from random import  randint
import os


limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
imprimir_com_msg = lambda msg, eletemto: print(f"\n{msg} {eletemto}")

def gerar_lista_letras(qnt):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    return [alfabeto[randint(0,25)] for _ in range(qnt)]

def converter_para_letra(valor):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if valor not in  alfabeto:
        print(f"Não foi possivel converver {valor} para uma letra")
        raise ValueError

def pegar_letra():
    letra = input("Digie uma letra: ")
    while True:
        try:
            converter_para_letra(letra)
            return letra
        except:
            print(f"Tente de novo")
            letra = input("Digie uma letra: ")

def contar_ocorrencias(*,lista, valor):
    valores = list(filter(lambda e: e == valor, lista))
    return {"valores": valores, "quantidade": len(valores)}

if __name__ == "__main__":
    limpar_terminal()
    letras = gerar_lista_letras(26)
    letra = pegar_letra()
    imprimir_com_msg(f"Vamos contar quantas vezes a {letra} está na lista:\n", letras)
    imprimir_com_msg(contar_ocorrencias(lista=letras,valor=letra ), "")