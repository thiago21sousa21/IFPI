# 8. Crie uma função chamada "remover_vogais" que receba uma string como parâmetro e 
# retorne uma nova string sem as vogais.  

def remover_vogais(texto:str)->str:
    vogais = 'aeiou'
    for letra in texto:
        if letra.lower() in vogais:
            texto = texto.replace(letra, '')
    return texto

if __name__ == "__main__":
    txt = 'aurelio'
    print(remover_vogais(txt))