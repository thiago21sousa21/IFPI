from database.connection import DatabaseConnection
from models import Like, Post


class LikeDao:

    @staticmethod
    def listar_todos_os_likes():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM likes")
            return [Like(**result) for result in results]

    @staticmethod
    def buscar_like(id:int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM likes WHERE id = %s", [id])
            if result:
                return Like(**result)
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