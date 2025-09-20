from models.aluno import Aluno
from models.endereco import Endereco
from models.matricula import Matricula
from models.professor import Professor
from models.disciplina import Disciplina
from dababase.simulacao_db import matriculas
from daos.matriculaDao import MatriculaDao
from daos.alunoDao import AlunoDao
from daos.enderecoDao import EnderecoDao
from daos.professorDao import ProfessorDao
from daos.disciplinaDao import DisciplinaDao

import os
import time

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
dois = lambda: time.sleep(2)

limpar_terminal()
#pra eu criar um aluno primeiro cria a matricula
m1 = Matricula(semestre_ano=2025.1, id=len(matriculas))
    #agora cria um aluno com essa matricula
al1 = Aluno(matricula=m1, nome="thiago", cpf="12341234123", data_nascimento="01/01/2000", idade=20)
    #Tem que ter o endereço dele
end1 = Endereco(bairro="gurupi", cep="64090155", cidade="teresina", estado="PI", numero=22, aluno=al1 )
print("Primeiro sobre matriculas")
print("\nprimeiro quero listar todas, pra ver que esta vazia:")
print(MatriculaDao.listar_todas())
dois()
print("\nAgora eu quero inserir uma")
print(MatriculaDao.inserir_uma(m1))
dois()
print("\nagora vou buscar unicamente a que inseri pra ver se funcina")
print(MatriculaDao.listar_uma(m1))
dois()
print("\nagora vou deletar uma")
print(MatriculaDao.deletar_uma(m1))
print(MatriculaDao.listar_todas())
dois()
############
limpar_terminal()
print("Agora sobre alunos")
print("\nprimeiro quero listar todas, pra ver que esta vazia:")
print(AlunoDao.listar_todas())
dois()
print("\nAgora eu quero inserir uma")
print(AlunoDao.inserir_uma(al1))
dois()
print("\nListar de novo pra ver se inseriu")
print(AlunoDao.listar_todas())
dois()
print("\nagora vou buscar unicamente uma especifica")
print(AlunoDao.listar_uma(al1))
dois()
print("\nagora vou deletar uma")
print(AlunoDao.deletar_uma(al1))
print(AlunoDao.listar_todas())
dois()
limpar_terminal()
##########
print("agora sobre endereço:")
print("\nprimeiro quero listar todas, pra ver que esta vazia:")
print(EnderecoDao.getAll())
dois()
print("\nAgora eu quero inserir uma")
print(EnderecoDao.insertOne(end1))
dois()
print("\nagora vou buscar unicamente uma especifica pra ver se inseriu")
print(EnderecoDao.getOne(end1))
dois()
print("\nagora vou deletar uma")
print(EnderecoDao.deleteOne(end1))
print(EnderecoDao.getAll())
dois()
limpar_terminal()

print("Agora sobre professor")
prof1 = Professor(email="prof@gmail.com", id_professor=1, nome_completo="jose farias", titulacao="doutor")

print("\nprimeiro quero listar todas, pra ver que esta vazia:")
print(ProfessorDao.getAll())
dois()
print("\nAgora eu quero inserir uma")
print(ProfessorDao.insertOne(prof1))
dois()
print("\nagora vou buscar unicamente uma especifica pra ver se inseriu")
print(ProfessorDao.getOne(prof1))
dois()
print("\nagora vou deletar uma")
print(ProfessorDao.deleteOne(prof1))
print(ProfessorDao.getAll())
dois()
limpar_terminal()

print("\nagora sobre disciplinas")
dois()
dis1 = Disciplina(codigo=1, nome="matemadica", carga_horaria=90, ementa="n sei")

print("\nprimeiro quero listar todas, pra ver que esta vazia:")
print(DisciplinaDao.getAll())
dois()
print("\nAgora eu quero inserir uma")
print(DisciplinaDao.insertOne(dis1))
dois()
print("\nagora vou buscar unicamente uma especifica pra ver se inseriu")
print(DisciplinaDao.getOne(dis1))
dois()
print("\nagora vou deletar uma")
print(DisciplinaDao.deleteOne(dis1))
print(DisciplinaDao.getAll())
dois()