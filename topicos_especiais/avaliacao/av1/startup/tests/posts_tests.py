
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
        #primeiro vou criar um usuario pra poder criar o post do usuario
        teste = Testar_usuario()
        usuarioId = next(teste.criar_usuario())
        usuario = teste.busca_um_usuario(usuarioId)

        #agora podemos criar o post
        postId = next(self.criar_post(10))
        post = self.busca_um_post(postId)
        print(vars(post))
        print("Vou usar o buscar  o post... ")
        print(self.busca_um_post(postId))
        print("Vou deletar o post agora...")
        print(self.deletar_post(postId))
        print("Vou conferir se deletou...")
        print(self.buscar_todos_os_posts())


    def criar_post(self, qnt:int = 1, usuario: Usuario = None):
        if not usuario:
            teste_usuario = Testar_usuario()
            usuarioId = next(teste_usuario.criar_usuario())
        usuario = teste_usuario.busca_um_usuario(usuarioId)

        for _ in range(qnt):
            post = Post(fake.date_time(), fake.text(100), usuario)
            yield PostDao.inserir_post(post)

    def busca_um_post(self, id: int):
        return PostDao.buscar_post(id)

    def buscar_todos_os_posts(self):
        return PostDao.listar_todos_posts()
    
    def deletar_post(self, id:int):
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