from models import Usuario, Telefone
from daos import UsuarioDao, TelefoneDao


# from tests.telefone_teste import testar_telefone

# testar_telefone()

# print(vars(busca_um_usuario()))
# print(buscar_usuarios())

######################
### TESTE TELEFONE ###
######################



def testar_telefone():

    u1 = Usuario("Thiago", "Thiago@Mail", "2000-01-01")
    u1.id = UsuarioDao.inserir_usuario(u1)
    
    t1: Telefone = Telefone("4567", u1)
    t1.id = 1

    print(TelefoneDao.listar_todos_telefones())
    print(TelefoneDao.inserir_telefone(t1))
    print(TelefoneDao.listar_todos_telefones())
    print('####')
    print(TelefoneDao.buscar_telefone(t1))
    TelefoneDao.delete_telefone(t1)
    print(TelefoneDao.listar_todos_telefones())
    t1.id = 2
    t1.numero = "3333333333"
    TelefoneDao.atualizar_telefone(t1)
    print(TelefoneDao.listar_todos_telefones())

