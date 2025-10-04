# 3. Escreva uma função chamada "contar_caracteres" que receba uma string como 
# parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string 
# e os valores são a quantidade de ocorrências de cada caractere.  

def contar_caracteres(text: str):
    dic = dict()
    for char in text:
        if dic.get(char):
            dic[char] +=1
        else: 
            dic[char] = 1
    return dic

if __name__ == "__main__":
    txt = input("Digite um texto as ser contado os seus caracteres: ")

    dicionario =  contar_caracteres(txt)

    print(dicionario)


