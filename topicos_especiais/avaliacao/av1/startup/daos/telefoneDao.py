from database.connection import DatabaseConnection
from models.telefone import Telefone
from daos.usuarioDao import UsuarioDao

class TelefoneDao:

    @staticmethod
    def listar_todos_telefones():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM telefones")
            for result in results:
                usuario = UsuarioDao.buscar_usuario(result["usuario_id"])
                yield Telefone(
                    numero= result["numero"],
                    usuario= usuario,
                    id=result["id"]
                )

    @staticmethod
    def buscar_telefone(id: int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM telefones WHERE id = %s", [id])
            if result:
                usuario = UsuarioDao.buscar_usuario(result["usuario_id"])
                return Telefone(
                    numero= result["numero"],
                    usuario= usuario,
                    id=result["id"]
                )
            return None

        
    @staticmethod
    def inserir_telefone(telefone: Telefone):
        params = [
            telefone.numero,
            telefone.usuario.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("INSERT INTO telefones (numero, usuario_id) VALUES (%s, %s)", params)

    @staticmethod
    def delete_telefone(id: int):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM telefones WHERE id= %s", [id])

    @staticmethod
    def atualizar_telefone(telefone: Telefone):
        params = [
            telefone.numero,
            telefone.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE telefones SET numero=%s WHERE id = %s", params)