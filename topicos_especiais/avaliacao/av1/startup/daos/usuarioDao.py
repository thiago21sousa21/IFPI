from database.connection import DatabaseConnection
from models import Usuario

class UsuarioDao:

    @staticmethod
    def listar_todos_os_usuarios():
        with DatabaseConnection() as conn:
            return conn.fetch_all("SELECT * FROM usuarios")

    @staticmethod
    def buscar_usuario(usuario: Usuario):
        with DatabaseConnection() as conn:
            resultado = conn.fetch_one("SELECT * FROM usuarios WHERE id = %s", [usuario.id])
            if resultado:
                return Usuario(**usuario)
            return None
        
    @staticmethod
    def inserir_usuario(usuario: Usuario):
        params = [usuario.nome_completo, usuario.email, usuario.data_nascimento]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO usuarios (nome_completo, email, data_nascimento) VALUES (%s, %s, %s)", params)

    @staticmethod
    def delete_usuario(usuario: Usuario):
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM usuarios WHERE id= %s", [usuario.id])

    @staticmethod
    def atualizar_usuario(usuario: Usuario):
        params = [
            usuario.nome_completo,
            usuario.email,
            usuario.data_nascimento,
            usuario.idade,
            usuario.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE usuarios SET nome_completo=%s, email=%s, data_nascimento=%s, idade=%s WHERE id = %s", params)