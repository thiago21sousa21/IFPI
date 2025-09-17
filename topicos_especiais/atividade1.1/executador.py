from professor import Professor
from professorDAO import ProfessorDao
# vou agora testar a criação de um professor
prof = Professor(
    nome="Flavio", 
    sobrenome="Davi", 
    data_nascimento="2000-01-01" , 
    matricula="24", 
    email="flavio@gmail.com"
)
ProfessorDao.create_professor(prof)
