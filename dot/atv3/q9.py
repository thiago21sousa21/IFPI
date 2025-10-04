# 9. Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de
# números como parâmetro e retorne o elemento que se repete mais vezes na lista. 


def contar_repetidos(lista: list):
    dic = dict()
    for e in lista:
        if dic.get(e):
            dic[e] +=1
        else: 
            dic[e] = 1
    return dic

def encontar_moda(dic: dict):
    most = list(dic.keys())[0]
    for c, v in dic.items():
        if v > dic[most]:
            most = c
    return most

if __name__ == "__main__":
    lista = [1,1,1,2,3,4]
    dicionario =  contar_repetidos(lista)
    chave = encontar_moda(dicionario)
    print(dicionario)

    print(f"O valor que mais se repete é: {chave} com {dicionario[chave]} ocorrencias")

