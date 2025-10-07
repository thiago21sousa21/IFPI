from database.connection import DatabaseConnection
from models import Amizade, Usuario


class AmizadeDao:

    @staticmethod
    def listar_todos_os_amizades():
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM amizades")

    @staticmethod
    def buscar_amizade(amizade: Amizade):
        params = [
            amizade.usuario1.id,
            amizade.usuario2.id
        ]
        with DatabaseConnection() as conn:
            return (conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
                    and conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_2 = %s AND usuario_id_1=%s", params))
        
    @staticmethod
    def inserir_amizade(amizade: Amizade):
        params = [
            amizade.usuario1.id,
            amizade.usuario2.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO amizades (usuario_id_1, usuario_id_2) VALUES (%s, %s)", params)

    @staticmethod
    def delete_amizade(amizade: Amizade):
        params = [
            amizade.usuario1.id,
            amizade.usuario2.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
   
    @staticmethod
    def atualizar_amizade(amizade_antes: Amizade, amizade_depois: Amizade):
        params = [
            amizade_depois.usuario1.id,
            amizade_depois.usuario2.id,
            amizade_depois.data_hora,
            amizade_antes.usuario1.id,
            amizade_antes.usuario2.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE amizades SET usuario_id_1=%s, usuario_id_2=%s data_hora=%s WHERE usuario_id_1=%s AND usuario_id_2=%s", params)