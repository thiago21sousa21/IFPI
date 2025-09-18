# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A 
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. 
# Para isso são dados:  o cartão gabarito;  o número de alunos da turma;  o cartão de respostas para cada aluno, 
# contendo o seu número e suas respostas. 


#primeiro vamos gerar uma letra aleatoria e depois vamos fazer uma lista com 30 dessas letras
from random import randint
import os

limpar_terminal = lambda: os.system("cls" if os.name=="nt" else "clear")
gerar_letra = lambda: 'ABCDE'[randint(0, 4)]
gerar_gabarito = lambda: [gerar_letra() for _ in range(30)]
gerar_alunos = lambda qnt: [(f"aluno{n+1}", gerar_gabarito()) for n in range(qnt)]

def conferir_resltado(gabarito_oficial, alunos):
    alunos_com_acerto = []
    for aluno in alunos:
        acertos = 0
        for idx, alt_aluno in enumerate(aluno[1]):
            if alt_aluno == gabarito_oficial[idx]:
                acertos+=1
        alunos_com_acerto.append((aluno[0], acertos))
    return alunos_com_acerto


if __name__ == "__main__":
    limpar_terminal()
    gabarito_correto = gerar_gabarito()
    alunos = gerar_alunos(5)
    print(alunos)
    alunos_com_acerto = conferir_resltado(gabarito_correto,alunos)
    print(alunos_com_acerto)
