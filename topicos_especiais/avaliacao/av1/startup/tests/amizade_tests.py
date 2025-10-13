
from models.amizade import Amizade
from models.usuario import Usuario
from daos.amizadeDao import AmizadeDao
from faker import Faker
from tests.usuario_test import Testar_usuario

fake = Faker()

class Testar_amizade:
    def __init__(self):
        pass

    def testar_tudo(self):


        
        #print(self.buscar_todos_os_amizade())

        # print("Vou criar uma amizade")
        # amizade_id = next(self.criar_amizade())
        # print(f"id da amizade: {amizade_id}")
        # print("Agora vou buscar a amizade")
        # amizade = self.busca_uma_amizade(amizade_id)
        # print(amizade)
        # print("Agora vou deletar")
        # self.deletar_amizade(amizade_id)
        pass


    def criar_amizade(self, usuario1:Usuario = None, usuario2:Usuario = None):
        if not usuario1:
            teste_usuario = Testar_usuario()
            usuarioId = next(teste_usuario.criar_usuario())
            usuario1 = teste_usuario.busca_um_usuario(usuarioId)

        if not usuario2:
            teste_usuario = Testar_usuario()
            usuarioId = next(teste_usuario.criar_usuario())
            usuario2 = teste_usuario.busca_um_usuario(usuarioId)


        amizade = Amizade(usuario1, usuario2)
        return AmizadeDao.inserir_amizade(amizade)

    def busca_uma_amizade(self, id: int):
        return AmizadeDao.buscar_amizade(id)

    def buscar_todos_os_amizade(self):
        return AmizadeDao.listar_todos_os_amizades()
    
    def deletar_amizade(self, id:int):
        return AmizadeDao.delete_amizade(id)



