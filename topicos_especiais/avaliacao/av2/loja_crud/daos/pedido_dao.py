"""
DAO (Data Access Object) para a entidade Pedido
"""
from typing import List, Optional
from decimal import Decimal
from datetime import date
from mysql.connector import Error
from models.pedido import Pedido
from conexao import Conexao


class PedidoDAO:
    
    def __init__(self, conexao: Conexao):
        self.conexao = conexao
    
    def criar(self, pedido: Pedido) -> Optional[int]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO pedidos (id_cliente, data_pedido, total)
                VALUES (%s, %s, %s)
            """
            valores = (pedido.id_cliente, pedido.data_pedido, pedido.total)
            
            cursor.execute(query, valores)
            conn.commit()
            
            pedido_id = cursor.lastrowid
            cursor.close()
            
            print(f"Pedido criado com sucesso! ID: {pedido_id}")
            return pedido_id
            
        except Error as e:
            print(f"Erro ao criar pedido: {e}")
            return None
    
    def buscar_por_id(self, id_pedido: int) -> Optional[Pedido]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos WHERE id_pedido = %s"
            cursor.execute(query, (id_pedido,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Pedido(
                    id_pedido=resultado['id_pedido'],
                    id_cliente=resultado['id_cliente'],
                    data_pedido=resultado['data_pedido'],
                    total=Decimal(str(resultado['total'])),
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar pedido: {e}")
            return None
    
    def buscar_todos(self) -> List[Pedido]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos ORDER BY data_pedido DESC"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            cursor.close()
            
            pedidos = []
            for resultado in resultados:
                pedido = Pedido(
                    id_pedido=resultado['id_pedido'],
                    id_cliente=resultado['id_cliente'],
                    data_pedido=resultado['data_pedido'],
                    total=Decimal(str(resultado['total'])),
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
                pedidos.append(pedido)
            
            return pedidos
            
        except Error as e:
            print(f"Erro ao buscar pedidos: {e}")
            return []
    
    def atualizar(self, pedido: Pedido) -> bool:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                UPDATE pedidos 
                SET id_cliente = %s, data_pedido = %s, total = %s
                WHERE id_pedido = %s
            """
            valores = (pedido.id_cliente, pedido.data_pedido, pedido.total, pedido.id_pedido)
            
            cursor.execute(query, valores)
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Pedido ID {pedido.id_pedido} atualizado com sucesso!")
                return True
            else:
                print(f"Pedido ID {pedido.id_pedido} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao atualizar pedido: {e}")
            return False
    
    def deletar(self, id_pedido: int) -> bool:
 
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM pedidos WHERE id_pedido = %s"
            cursor.execute(query, (id_pedido,))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Pedido ID {id_pedido} deletado com sucesso!")
                return True
            else:
                print(f"Pedido ID {id_pedido} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao deletar pedido: {e}")
            return False
    
    def buscar_por_cliente(self, id_cliente: int) -> List[Pedido]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos WHERE id_cliente = %s ORDER BY data_pedido DESC"
            cursor.execute(query, (id_cliente,))
            
            resultados = cursor.fetchall()
            cursor.close()
            
            pedidos = []
            for resultado in resultados:
                pedido = Pedido(
                    id_pedido=resultado['id_pedido'],
                    id_cliente=resultado['id_cliente'],
                    data_pedido=resultado['data_pedido'],
                    total=Decimal(str(resultado['total'])),
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
                pedidos.append(pedido)
            
            return pedidos
            
        except Error as e:
            print(f"Erro ao buscar pedidos por cliente: {e}")
            return []
    
    def calcular_total_pedido(self, id_pedido: int) -> Optional[Decimal]:
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT SUM(quantidade * preco_unitario) as total
                FROM pedidos_produtos
                WHERE id_pedido = %s
            """
            cursor.execute(query, (id_pedido,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado and resultado[0] is not None:
                return Decimal(str(resultado[0]))
            return Decimal('0.00')
            
        except Error as e:
            print(f"Erro ao calcular total do pedido: {e}")
            return None
    
    def atualizar_total(self, id_pedido: int) -> bool:
        try:
            total = self.calcular_total_pedido(id_pedido)
            if total is None:
                return False
            
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "UPDATE pedidos SET total = %s WHERE id_pedido = %s"
            cursor.execute(query, (total, id_pedido))
            conn.commit()
            
            cursor.close()
            print(f"Total do pedido ID {id_pedido} atualizado para {total}!")
            return True
            
        except Error as e:
            print(f"Erro ao atualizar total do pedido: {e}")
            return False
