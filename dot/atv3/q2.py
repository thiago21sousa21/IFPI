# 2.  Crie  uma  função  chamada  "verificar_anagrama"  que  receba  duas  strings  como 
# parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as 
# mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário. 

import os

limpar_terminal = lambda : os.system("cls" if os.name == "nt" else  "clear")

def receber_string():
    st = input("Digite uma palavra a ser verificasa se é anagrama: ")
    return st

def transformar_em_dict(texto):
    dic = dict()
    for char in texto:
        if char in dic.keys():
            dic[char]+=1
        else:
            dic[char] = 1
    return dic

def verificar_anagrama(string1, string2):

    d1 = transformar_em_dict(p1)
    d2 = transformar_em_dict(p2)

    return d1 == d2

    

if __name__ == "__main__":
    p1 = receber_string()
    p2 = receber_string()

    isAnagrama = verificar_anagrama(p1, p2)

    print(f"{"Sim" if isAnagrama else "Não"} {p1} {"é" if isAnagrama else "não é"} anagrama de {p2}")