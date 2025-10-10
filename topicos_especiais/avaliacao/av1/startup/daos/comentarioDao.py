from database.connection import DatabaseConnection
from models.comentario import Comentario

class ComentarioDao:

    @staticmethod
    def listar_todos_os_comentarios():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM comentarios")
            return [ Comentario(**result) for result in results]

    @staticmethod
    def buscar_comentario(id: int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM comentarios WHERE id = %s", [id])
            if result:
                return Comentario(**result)
            return None
        
    @staticmethod
    def inserir_comentario(comentario: Comentario):
        params = [
            comentario.post.id,
            comentario.usuario.id,
            comentario.conteudo
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO comentarios (post_id, usuario_id, conteudo) VALUES (%s, %s, %s)", params)

    @staticmethod
    def delete_comentario(id: int ):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM comentarios WHERE id= %s", [id])

    @staticmethod
    def atualizar_comentario(comentario: Comentario):
        params = [
            comentario.post.id,
            comentario.usuario.id,
            comentario.conteudo,
            comentario.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE comentarios SET post_id=%s, usuario_id=%s, conteudo=%s WHERE id = %s", params)