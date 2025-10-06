from database.connection import DatabaseConnection
from models import Amizade, Usuario


class AmizadeDao:

    @staticmethod
    def listar_todos_os_amizades():
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM amizades")

    @staticmethod
    def buscar_amizade(usuario1: Usuario, usuario2:Usuario):
        params = [
            usuario1.id,
            usuario2.id
        ]
        with DatabaseConnection() as conn:
            return (conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
                    and conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_2 = %s AND usuario_id_1=%s", params))
        
    @staticmethod
    def inserir_amizade(usuario1: Usuario, usuario2:Usuario):
        params = [
            usuario1.id,
            usuario2.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO amizades (usuario_id_1, usuario_id_2) VALUES (%s, %s)", params)

    @staticmethod
    def delete_amizade(usuario1: Usuario, usuario2:Usuario):
        params = [
            usuario1.id,
            usuario2.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
    # provavelmente não sera implementado
    # @staticmethod
    # def atualizar_amizade(amizade: Amizade):
    # provavelmente não sera implementado
    #     params = [
    #         amizade.post.id,
    #         amizade.usuario.id,
    #         amizade.conteudo,
    #         amizade.id
    #     ]
    #     with DatabaseConnection() as conn:
    #         conn.execute_query("UPDATE amizades SET post_id=%s, usuario_id=%s, conteudo=%s WHERE id = %s", params)