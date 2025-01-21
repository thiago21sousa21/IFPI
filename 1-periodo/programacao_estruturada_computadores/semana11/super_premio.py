from random import *

# Exibir as 3 portas e as instruções do jogo
print('''
Show de Prêmios!
================

Há um prêmio atrás de uma das 3 portas!
Adivinhe a porta correta para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

pontuacao = 0

# Permitir ao jogador 3 tentativas
for tentativa in range(3):

    print("\nEscolha uma porta (1, 2 ou 3):")

    # Obter a porta escolhida e armazenar como um número inteiro
    porta_escolhida = input()
    porta_escolhida = int(porta_escolhida)

    # Escolher aleatoriamente o número da porta vencedora (entre 1 e 3)
    porta_vencedora = randint(1, 3)

    # Mostrar ao jogador os números da porta escolhida e da porta vencedora
    print("A porta escolhida é", porta_escolhida)
    print("A porta vencedora é", porta_vencedora)

    # O jogador vence se a porta escolhida for igual à porta vencedora
    if porta_escolhida == porta_vencedora:
        print("Parabéns!")
        pontuacao += 1
    else:
        print("Que pena!")

print("\nSua pontuação final é", pontuacao)
