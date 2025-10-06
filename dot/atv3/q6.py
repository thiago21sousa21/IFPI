# 6. Crie uma função chamada "contar_substrings" que receba uma string e uma substring 
# como parâmetros e retorne a quantidade de ocorrências da substring na string. 

def contar_substrings(txt, sub):
    cont = 0
    for idx in range(len(txt) - len(sub)):
        if sub == txt[idx:idx+len(sub)]:
            cont += 1
    return cont
    

if __name__ == "__main__":
    texto = "cdaaaacdbbbbbbcdcdc"
    sub = "cd"
    print(texto.count(sub))
    