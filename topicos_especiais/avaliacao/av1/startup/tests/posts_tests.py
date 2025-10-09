
from models.post import Post
from daos.postDao import PostDao
from faker import Faker
from tests.usuario_test import Testar_usuario
from models.usuario import Usuario

fake = Faker()

class Testar_posts:
    def __init__(self):
        pass

    def testar_tudo(self):
        idUsuariCriado = next(self.criar_usuario(10))
        print(next(idUsuariCriado))
        usuario_buscado = self.busca_um_usuario(idUsuariCriado)
        print(vars(usuario_buscado))
        print("Vou usar o buscar tudo... ")
        print(self.buscar_usuarios())
        print("Vou deletar o usuario agora...")
        print(self.deletar_usuario(idUsuariCriado))
        print("Vou conferir se deletou...")
        print(self.buscar_usuarios())


    def criar_post(self, qnt:int = 1, usuario: Usuario = None):
        if not usuario:
            usuario = next(Testar_usuario.criar_usuario(1))

        for _ in range(qnt):
            post = Post(fake.date_time(), fake.text(100), usuario)
            yield PostDao.inserir_post()

    def busca_um_post(self, id: int):
        return PostDao.buscar_post(id)

    def buscar_todos_os_posts(self):
        return PostDao.listar_todos_posts()
    
    def deletar_usuario(self, id:int):
        return PostDao.delete_post(id)




###################
### TESTE POSTS ###
###################

# post1:Post = Post(datetime.now(), "Bom dia!", u1, midia="meu link 1")
# print(PostDao.listar_todos_posts())
# u1.id = 2
# post1.id = 2
# PostDao.inserir_post(post1)

#print(PostDao.buscar_post(post1))
#PostDao.delete_post(post1)

#ATUALIZAR  POST
# post1.conteudo = "Boa tarde"
# post1.midia = "Meu link 2"
# PostDao.atualizar_post(post1)
# print(PostDao.listar_todos_posts())
#PostDao.atualizar_post()