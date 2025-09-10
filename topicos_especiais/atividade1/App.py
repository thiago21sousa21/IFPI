# Supondo que ProfessorDao também foi refatorado para usar 'with'
# e que insertProfessor retorna o ID do novo professor.
from ProfessorDao import ProfessorDao
from Professor import Professor
from DisciplinaDao import DisciplinaDao
from Disciplina import Disciplina

# --- CRIAÇÃO DAS TABELAS (Executar uma vez ou deixar no início) ---
print("--- Configurando o Banco de Dados ---")
ProfessorDao.createTable()
DisciplinaDao.criar_tabela_disciplinas()
print("-" * 20)

# --- FLUXO DE CADASTRO ---

# 1. Criar um objeto Professor
prof1 = Professor("Ana", "Silva", "2023002", "1985-07-20", "ana@email.com")

# 2. Inserir o professor no banco de dados
#    (Supondo que seu ProfessorDao.insertProfessor foi ajustado para retornar o ID)
novo_professor_id = ProfessorDao.insertProfessor(prof1)
print(f"ID do novo professor: {novo_professor_id}")
# 3. Se o professor foi inserido com sucesso, cadastrar suas disciplinas
if novo_professor_id:
    print(f"\nProfessor(a) {prof1.nome} cadastrado(a) com ID: {novo_professor_id}")
    
    # Criamos os objetos Disciplina usando o ID do professor que acabamos de obter
    disc1 = Disciplina(nome="Cálculo I", carga_horaria=90, professor_id=novo_professor_id)
    disc2 = Disciplina(nome="Álgebra Linear", carga_horaria=75, professor_id=novo_professor_id)

    # Inserimos as disciplinas no banco
    DisciplinaDao.criar_disciplina(disc1)
    DisciplinaDao.criar_disciplina(disc2)

# --- LISTANDO OS DADOS ---
print("\n--- Professores Cadastrados ---")
professores = ProfessorDao.listarProfessores()
for prof in professores:
    print(prof)

print("\n--- Disciplinas Cadastradas (com nome do professor) ---")
disciplinas = DisciplinaDao.listar_disciplinas()
for disc in disciplinas:
    # disc será uma tupla como: (id, nome_disciplina, carga_h, prof_id, nome_professor)
    print(f"ID: {disc[0]}, Disciplina: {disc[1]}, Carga Horária: {disc[2]}h, Professor: {disc[4]}")
