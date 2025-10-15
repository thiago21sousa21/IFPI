
from models.amizade import Amizade
from models.usuario import Usuario
from daos.amizadeDao import AmizadeDao
from daos.usuarioDao import UsuarioDao
from faker import Faker
from tests.usuario_test import Testar_usuario

fake = Faker()

class Testar_amizade:
    def __init__(self):
        pass

    def testar_tudo(self):
        print(self.criar_intencao_amizade())
        print(self.criar_intencao_amizade())
        print(self.listar_todas_as_intencoes_de_amizade())
        print(self.busca_uma_amizade())
        print(self.listar_todas_as_intencoes_de_amizade())


    def criar_intencao_amizade(self, id1:int = None, id2:int = None):
        if (not id1) or (not id2):
            teste_usuario = Testar_usuario()

        if not id1:
            id1 = next(teste_usuario.criar_usuario())
            usuario1 = teste_usuario.busca_um_usuario(id1)

        if not id2:
            id2 = next(teste_usuario.criar_usuario())
            usuario2 = teste_usuario.busca_um_usuario(id2)

        amizade = Amizade(usuario1, usuario2)

        return AmizadeDao.inserir_intencao_de_amizade(amizade)

    def busca_uma_amizade(self, id1:int = None, id2:int = None):
        if (not id1) or (not id2):
            teste_usuario = Testar_usuario()

        if not id1:
            id1 = next(teste_usuario.criar_usuario())
            u1 = UsuarioDao.buscar_usuario(id1)

        if not id2:
            id2 = next(teste_usuario.criar_usuario())
            u2 = UsuarioDao.buscar_usuario(id2)

        AmizadeDao.inserir_intencao_de_amizade(Amizade(u1, u2))
        AmizadeDao.inserir_intencao_de_amizade(Amizade(u2, u1))

        return AmizadeDao.buscar_amizade(id1, id2)

    def listar_todas_as_intencoes_de_amizade(self):
        return AmizadeDao.listar_todas_as_intencoes_de_amizade()
    
    def deletar_amizade_ou_intencao(self, id:int):
        return AmizadeDao.delete_amizade(id)
    



