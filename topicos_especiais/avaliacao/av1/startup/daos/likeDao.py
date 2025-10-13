from database.connection import DatabaseConnection
from models.like import Like
from models.post import Post
from daos.usuarioDao import UsuarioDao
from daos.postDao import PostDao


class LikeDao:

    @staticmethod
    def listar_todos_os_likes():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM likes")
            for result in results:
                post = PostDao.buscar_post(result["post_id"])
                usuario = UsuarioDao.buscar_usuario(result["usuario_id"])
                yield Like(
                    id=result["id"],
                    data_hora=result["data_hora"],
                    post=post,
                    usuario=usuario
                )

    @staticmethod
    def buscar_like(id:int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM likes WHERE id = %s", [id])
            if result:
                post = PostDao.buscar_post(result["post_id"])
                usuario = UsuarioDao.buscar_usuario(result["usuario_id"])
                return Like(
                    id=result["id"],
                    data_hora=result["data_hora"],
                    post=post,
                    usuario=usuario
                )
            return None
        
    @staticmethod
    def inserir_like(like: Like):
        params = [
            like.usuario.id,
            like.post.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO likes (usuario_id, post_id) VALUES (%s, %s)", params)

    @staticmethod
    def delete_like(id: int):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM likes WHERE id= %s", [id])

    @staticmethod
    def atualizar_like(like: Like):
        params = [
            like.usuario.id,
            like.post.id,
            like.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE likes SET usuario_id=%s, post_id=%s WHERE id = %s", params)
        
    @staticmethod
    def buscar_likes_de_um_post(post:Post):
        params = [post.id]
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM likes WHERE post_id = %s", params)