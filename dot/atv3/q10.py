# 10. Escreva uma função chamada "verificar_quadrado_perfeito" que receba um número
# inteiro como parâmetro e retorne True se o número for um quadrado perfeito, e False
# caso contrário. Um número inteiro é considerado um quadrado perfeito quando ele é o
# resultado da multiplicação de um número inteiro por ele mesmo. Em outras palavras, um
# número inteiro "n" é um quadrado perfeito se existir um número inteiro "m" tal que "n =
# m * m". Por exemplo, os números 4, 9, 16 e 25 são quadrados perfeitos, pois podem ser
# obtidos pela multiplicação de um número inteiro por ele mesmo: 4 = 2 * 2; 9 = 3 * 3; 16 =
# 4 * 4; 25 = 5 * 5.
# Obs: não utilizar a função raiz quadrada isqrt(). """

def verificar_quadrado_perfeito(num : int):
    cont = 0
    while  (quadrado:= (cont**2)) <= num:
        if quadrado == num:
            return cont
        cont += 1
    return None
if __name__ == "__main__":
    n = int(input("Digite um numero: "))
    isQuadrado = verificar_quadrado_perfeito(n)
    print(f"{n} não é um quadrado perfeiro" if not isQuadrado else f"Sim {n} é quadrado perfeito e sua raiz é: {isQuadrado}")