from database.connection import DatabaseConnection
from models.post import Post
from daos.usuarioDao import UsuarioDao
from models.usuario import Usuario

class PostDao:

    @staticmethod
    def listar_todos_posts():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM posts")
            return [Post(**result) for result in results]

    @staticmethod
    def buscar_post(id: int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM posts WHERE id = %s", [id])
            print(result)
            if result:
                usuario:Usuario = UsuarioDao.buscar_usuario(result["usuario_id"]) 
                return Post(
                    data_hora=result["data_hora"],
                    conteudo= result["conteudo"],
                    id= result["id"],
                    midia= result["midia"],
                    usuario= usuario
                )
            return None
        
    @staticmethod
    def inserir_post(post: Post):
        params = [
            post.data_hora,
            post.conteudo,
            post.midia,
            post.ususario.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO posts (data_hora, conteudo, midia, usuario_id) VALUES (%s, %s, %s, %s)", params)

    @staticmethod
    def delete_post(id:int):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM posts WHERE id= %s", [id])

    @staticmethod
    def atualizar_post(post: Post):
        params = [
            post.data_hora,
            post.conteudo,
            post.midia,
            post.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE posts SET data_hora=%s, conteudo=%s, midia=%s WHERE id = %s", params)