
from models.comentario import Comentario
from models.usuario import Usuario
from daos.comentarioDao import ComentarioDao
from faker import Faker
from tests.usuario_test import Testar_usuario
from tests.posts_tests import Testar_posts
from models.post import Post


fake = Faker()

class Testar_comentarios:
    def __init__(self):
        pass

    def testar_tudo(self):

        print("Vou criar um comentario")
        ultimo_comentario_id = next(self.criar_comentario(10))
        print(f"id do ultimo comentario: {ultimo_comentario_id}")
        print("Agora vou buscar o ultimo comentario feito")
        ultimo_comentario = self.busca_um_comentario(ultimo_comentario_id)
        print(ultimo_comentario)
        print("Agora vou deletar")
        self.deletar_comentarios(ultimo_comentario_id)
        print("Agora vou buscar todos pra conferir se deletou")
        self.buscar_todos_os_comentarios()


    def criar_comentario(self, qnt:int = 1, post:Post = None, usuario:Usuario = None):
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

        for _ in range(qnt):
            comentario = Comentario(fake.text(100), post, usuario)
            yield ComentarioDao.inserir_comentario(comentario)

    def busca_um_comentario(self, id: int):
        return ComentarioDao.buscar_comentario(id)

    def buscar_todos_os_comentarios(self):
        return ComentarioDao.listar_todos_os_comentarios()
    
    def deletar_comentarios(self, id:int):
        return ComentarioDao.delete_comentario(id)



