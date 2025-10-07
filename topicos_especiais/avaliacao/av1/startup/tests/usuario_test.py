from utils.limpar_banco import limpar_banco
from daos import UsuarioDao
from models import Usuario

limpar_banco()

def criar_usuario():
    usuario = Usuario("thiago", "thiago@mail.com", "2000-01-01")
    result = UsuarioDao.inserir_usuario(usuario)