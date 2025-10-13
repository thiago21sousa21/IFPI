
from models.like import Like
from models.usuario import Usuario
from daos.likeDao import LikeDao
from faker import Faker
from tests.usuario_test import Testar_usuario
from tests.posts_tests import Testar_posts
from models.post import Post


fake = Faker()

class Testar_likes:
    def __init__(self):
        pass

    def testar_tudo(self):

        print("Vou criar um like")
        like_id = next(self.criar_like())
        print(f"id do like: {like_id}")
        print("Agora vou buscar o like")
        like = self.busca_um_like(like_id)
        print(like)
        print("Agora vou deletar")
        self.deletar_likes(like_id)
        print("Agora vou buscar todos pra conferir se deletou")
        self.buscar_todos_os_likes()


    def criar_like(self, post:Post = None, usuario:Usuario = None):
        if not usuario:
            teste_usuario = Testar_usuario()
            usuarioId = next(teste_usuario.criar_usuario())
            usuario = teste_usuario.busca_um_usuario(usuarioId)
            print(usuario)

        if not post:
            print("Agora vou criar um post")
            teste_post = Testar_posts()
            postId = next(teste_post.criar_post())
            post = teste_post.busca_um_post(postId)
            print(post)

        like = Like(post, usuario)
        yield LikeDao.inserir_like(like)

    def busca_um_like(self, id: int):
        return LikeDao.buscar_like(id)

    def buscar_todos_os_likes(self):
        return LikeDao.listar_todos_os_likes()
    
    def deletar_likes(self, id:int):
        return LikeDao.delete_like(id)



