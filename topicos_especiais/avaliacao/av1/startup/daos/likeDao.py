from database.connection import DatabaseConnection
from models import Like, Post


class LikeDao:

    @staticmethod
    def listar_todos_os_likes():
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM likes")

    @staticmethod
    def buscar_like(like: Like):
        with DatabaseConnection() as conn:
            return conn.fetch_one("SELECT * FROM likes WHERE id = %s", [like.id])
        
    @staticmethod
    def inserir_like(like: Like):
        params = [
            like.usuario.id,
            like.post.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO likes (usuario_id, post_id) VALUES (%s, %s)", params)

    @staticmethod
    def delete_like(like: Like):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM likes WHERE id= %s", [like.id])

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