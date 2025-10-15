from database.connection import DatabaseConnection
from models.amizade import Amizade
from daos.usuarioDao import UsuarioDao


class AmizadeDao:

    @staticmethod
    def listar_todas_as_intencoes_de_amizade():
        with DatabaseConnection() as conn:
            results = conn.fetch_all("SELECT * FROM amizades")
            for result in results:
                id1 = result['usuario_id_1']
                id2 = result['usuario_id_2']

                if id1:
                    usuario1 = UsuarioDao.buscar_usuario(id1)
                if id2:
                    usuario2 = UsuarioDao.buscar_usuario(id2)

                yield Amizade(usuario1, usuario2, result['data_hora'])


    @staticmethod
    def buscar_amizade(id1: int, id2: int):
        params = [id1,id2]
        with DatabaseConnection() as conn:
            amizade12 = conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
            amizade21 = conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_2 = %s AND usuario_id_1=%s", params)
            
            if amizade12 and amizade21:
                return ( amizade12['id'], amizade21['id'])
            return None
        
    def buscar_intencao_de_amizade_por_id(id:int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM amizades WHERE id =%s", id)
            if result:
                id1 = result['usuario_id_1']
                id2 = result['usuario_id_2']

                if id1:
                    usuario1 = UsuarioDao.buscar_usuario(id1)
                if id2:
                    usuario2 = UsuarioDao.buscar_usuario(id2)

                return Amizade(usuario1, usuario2, result['data_hora'])
            
    def buscar_intencao_de_amizade_por_usuariosIds(id1:int, id2:int):
        with DatabaseConnection() as conn:
            result = conn.fetch_one("SELECT * FROM amizades WHERE usuario_id_1=%s AND usuario_id_2=%s", [id1, id2])
            if result:
                usuario1 = UsuarioDao.buscar_usuario(id1)
                usuario2 = UsuarioDao.buscar_usuario(id2)  
                return Amizade(usuario1, usuario2, result['data_hora'])
            
    @staticmethod
    def inserir_intencao_de_amizade(amizade: Amizade):
        params = [
            amizade.usuario1.id,
            amizade.usuario2.id
        ]
        with DatabaseConnection() as conn:
            return conn.execute_query("INSERT INTO amizades (usuario_id_1, usuario_id_2) VALUES (%s, %s)", params)

    @staticmethod
    def delete_amizade(id1:int, id2:int):
        params = [id1,id2]
        with DatabaseConnection() as conn:
            conn.execute_query("DELETE FROM amizades WHERE usuario_id_1 = %s AND usuario_id_2=%s", params)
   
    @staticmethod
    def atualizar_intecao_amizade(amizade_antes: Amizade, amizade_depois: Amizade):
        params = [
            amizade_depois.usuario1.id,
            amizade_depois.usuario2.id,
            amizade_depois.data_hora,
            amizade_antes.usuario1.id,
            amizade_antes.usuario2.id
        ]
        with DatabaseConnection() as conn:
            conn.execute_query("UPDATE amizades SET usuario_id_1=%s, usuario_id_2=%s data_hora=%s WHERE usuario_id_1=%s AND usuario_id_2=%s", params)

    @staticmethod
    def buscar_amizades():
        with DatabaseConnection() as conn:
            return conn.fetch_all("""
                SELECT 
                    a.usuario_id_1 AS usuario_id_a,
                    a.usuario_id_2 AS usuario_id_b,
                    a.data_hora AS data_pedido_a_para_b,
                    b.data_hora AS data_pedido_b_para_a
                FROM amizades a
                JOIN amizades b
                    ON a.usuario_id_1 = b.usuario_id_2
                AND a.usuario_id_2 = b.usuario_id_1
                WHERE a.usuario_id_1 < a.usuario_id_2;
        """)