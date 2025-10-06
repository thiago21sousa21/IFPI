from database.connection import DatabaseConnection
from models.telefone import Telefone

class TelefoneDao:

    @staticmethod
    def listar_todos_telefones():
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM telefones")

    @staticmethod
    def buscar_telefone(telefone: Telefone):
        with DatabaseConnection() as conn:
            return conn.fetch_one("SELECT * FROM telefones WHERE id = %s", [telefone.id])
        
    @staticmethod
    def inserir_telefone(telefone: Telefone):
        params = [
            telefone.numero,
            telefone.usuario.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("INSERT INTO telefones (numero, usuario_id) VALUES (%s, %s)", params)

    @staticmethod
    def delete_telefone(telefone: Telefone):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM telefones WHERE id= %s", [telefone.id])

    @staticmethod
    def atualizar_telefone(telefone: Telefone):
        params = [
            telefone.numero,
            telefone.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE telefones SET numero=%s WHERE id = %s", params)