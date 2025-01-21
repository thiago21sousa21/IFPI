from random import *

# Essa variável deve ser alterada pelo usuário para terminar o jogo
jogando = True

pontuacao = 0

# Imprime as instruções do jogo
print('''
Vinte e Um!
===========
Tente fazer exatamente 21 pontos!
''')

# Repete enquanto a variável 'jogando' for 'True'
while jogando == True:

    # Escolhe um número aleatoriamente entre 1 e 10
    novo_numero = randint(1, 10)

    # Soma o novo número à pontuação
    pontuacao = pontuacao + novo_numero

    # Mostra os dados para o jogador
    print("\nSeu próximo número é", novo_numero)
    print("Sua pontuação agora é", pontuacao)

    # Termina se o usuário digitar 'n'
    # ou se a pontuação for maior que 21
    print("\nGostaria de somar mais um número? (s/n)")
    resposta = input()
    if resposta.lower() == 'n' or pontuacao > 21:
        jogando = False

print("\nSua pontuação final é", pontuacao)

# Se o jogador marcar 21
if pontuacao == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!")
