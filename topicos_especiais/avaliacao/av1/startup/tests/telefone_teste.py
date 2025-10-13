
from models.telefone import Telefone
from daos.telefoneDao import TelefoneDao
from faker import Faker
from tests.usuario_test import Testar_usuario
from models.usuario import Usuario

fake = Faker()

class Testar_telefones:
    def __init__(self):
        pass

    def testar_tudo(self):
        #primeiro vou criar um usuario pra poder criar o post do usuario
        teste = Testar_usuario()
        usuarioId = next(teste.criar_usuario())
        usuario = teste.busca_um_usuario(usuarioId)

        print("Vou criar um telefone")
        telefoneId = next(self.criar_telefone(10,usuario))
        print(f"id do ultimo telefone: {telefoneId}")
        print(f"Vou buscar  o telefone de id: {telefoneId}")
        telefone = self.busca_um_telefone(telefoneId)
        print(telefone)
        print("Vou deletar o telefone agora...")
        print(self.deletar_telefone(telefoneId))
        print("Vou conferir se deletou...")
        print(self.buscar_todos_os_telefones())


    def criar_telefone(self, qnt:int = 1, usuario: Usuario = None):
        if not usuario:
            teste_usuario = Testar_usuario()
            usuarioId = next(teste_usuario.criar_usuario())
            usuario = teste_usuario.busca_um_usuario(usuarioId)

        for _ in range(qnt):
            telefone = Telefone(fake.phone_number(), usuario)
            yield TelefoneDao.inserir_telefone(telefone)

    def busca_um_telefone(self, id: int):
        return TelefoneDao.buscar_telefone(id)

    def buscar_todos_os_telefones(self):
        return TelefoneDao.listar_todos_telefones()
    
    def deletar_telefone(self, id:int):
        return TelefoneDao.delete_telefone(id)



