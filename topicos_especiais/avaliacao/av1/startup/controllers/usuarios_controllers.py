from daos import UsuarioDao
from models import Usuario

class UsuariosControllers:

    @staticmethod
    def criar_usuario(usuario: Usuario):
        return UsuarioDao.inserir_usuario(usuario)