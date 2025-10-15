
from models.usuario import Usuario
from daos.usuarioDao import UsuarioDao
from faker import Faker
from time import sleep

fake = Faker()

class Testar_usuario:
    def __init__(self):
        pass

    def testar_tudo(self):
        print("primeiro vou criar um usuario, ou alguns usuarios, estou criando 10...")
        idUsuariCriado = None
        for idUsuariCriado in self.criar_usuario(10):
            print(f"Usuário criado com id: {idUsuariCriado}")
        usuario_buscado = self.busca_um_usuario(idUsuariCriado)
        sleep(2)
        print(vars(usuario_buscado))
        print("Vou usar o buscar tudo... ")
        print(list(self.buscar_usuarios()))
        print(f"Vou deletar o usuario agora de id: {idUsuariCriado}...")
        print(self.deletar_usuario(idUsuariCriado))
        print("Vou conferir se deletou...")
        print(list(self.buscar_usuarios()))
        print("Usuario deletado com sucesso")


    def criar_usuario(self, qnt:int = 1):
        for _ in range(qnt):
            usuario = Usuario(fake.name(), fake.email(), fake.date_of_birth())
            yield UsuarioDao.inserir_usuario(usuario)

    def busca_um_usuario(self, id: int):
        return UsuarioDao.buscar_usuario(id)

    def buscar_usuarios(self):
        return UsuarioDao.listar_todos_os_usuarios()
    
    def deletar_usuario(self, id:int):
        return UsuarioDao.delete_usuario(id)

