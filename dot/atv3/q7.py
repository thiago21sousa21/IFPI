# 7. Escreva uma função chamada "encontrar_elemento_faltante" que receba uma lista de 
# números de 1 a n (sendo n um número inteiro) em ordem aleatória, com um elemento 
# faltando, e retorne o elemento que está faltando. Ex: [4,3,1,5] = 2 


def trocar(n1, n2):
    if n1 > n2:
        return (n2, n1)
    return (n1, n2)


def ordenar(lista:list):
    copia_lista = lista.copy()
    for i in range(len(copia_lista)-1):
        for index in range(len(lista)-1-i):
            e1= copia_lista[index]
            e2 = copia_lista[index+1]
            copia_lista[index], copia_lista[index+1] = trocar(e1, e2)
    return copia_lista

def descobrir_faltantes(lista_ordenada:list) ->list:
    copia_lista = lista_ordenada.copy()
    primeiro = copia_lista[0]
    ultimo = copia_lista[-1]
    faltantes = list()
    referencial = range(primeiro, ultimo+1)
    for e in referencial:
        if e not in copia_lista:
            faltantes.append(e)
    return faltantes

if __name__ == "__main__":
    lista = [10,1]
    ordanada = ordenar(lista)
    print(lista)
    print(descobrir_faltantes(ordanada))