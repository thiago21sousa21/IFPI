import os
from random import randint

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
gerar_sequencia = lambda tamanho: [randint(0, 100) for _ in range(tamanho)]
inverter = lambda seq: seq[::-1]
printar_com_msg = lambda msg, elemento: print(f"\n{msg} {elemento}")

if __name__ == "__main__":
    limpar_terminal()
    seq = gerar_sequencia(5)
    printar_com_msg("Sequência original:", seq)
    printar_com_msg("Sequência invertida:", inverter(seq))
