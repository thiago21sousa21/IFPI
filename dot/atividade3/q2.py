# 2.  Crie  uma  função  chamada  "verificar_anagrama"  que  receba  duas  strings  como 
# parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as 
# mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário.  


def gerar_dicionario(texto: list):
    dicionario = {}
    for letra in texto:
        if letra in dicionario:
            dicionario[letra] +=1
        else:
            dicionario[letra] = 1
    return dicionario


def verificar_se_sao_iguais(dict1:dict, dict2:dict):
    return dict1 == dict2

def vericar_se_anagrama(text1:str, text2:str):
    dict1 = gerar_dicionario(text1)
    dict2 = gerar_dicionario(text2)
    iguais = verificar_se_sao_iguais(dict1, dict2)
    print("E anagrama" if iguais else "Não é anagrama")

vericar_se_anagrama("abacaxi", "ixacaba")