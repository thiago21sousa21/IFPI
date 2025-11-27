
from typing import List, Optional, Tuple
from decimal import Decimal
from mysql.connector import Error
from models.pedido_produto import PedidoProduto
from conexao import Conexao


class PedidoProdutoDAO:

    def __init__(self, conexao: Conexao):

        self.conexao = conexao
    
    def criar(self, pedido_produto: PedidoProduto) -> bool:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO pedidos_produtos (id_pedido, id_produto, quantidade, preco_unitario)
                VALUES (%s, %s, %s, %s)
            """
            valores = (
                pedido_produto.id_pedido,
                pedido_produto.id_produto,
                pedido_produto.quantidade,
                pedido_produto.preco_unitario
            )
            
            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            
            print(f"Produto ID {pedido_produto.id_produto} adicionado ao pedido ID {pedido_produto.id_pedido}!")
            return True
            
        except Error as e:
            print(f"Erro ao adicionar produto ao pedido: {e}")
            return False
    
    def buscar_por_pedido(self, id_pedido: int) -> List[PedidoProduto]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos_produtos WHERE id_pedido = %s"
            cursor.execute(query, (id_pedido,))
            
            resultados = cursor.fetchall()
            cursor.close()
            
            pedidos_produtos = []
            for resultado in resultados:
                pedido_produto = PedidoProduto(
                    id_pedido=resultado['id_pedido'],
                    id_produto=resultado['id_produto'],
                    quantidade=resultado['quantidade'],
                    preco_unitario=Decimal(str(resultado['preco_unitario'])),
                    created_at=resultado['created_at']
                )
                pedidos_produtos.append(pedido_produto)
            
            return pedidos_produtos
            
        except Error as e:
            print(f"Erro ao buscar produtos do pedido: {e}")
            return []
    
    def buscar_por_produto(self, id_produto: int) -> List[PedidoProduto]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos_produtos WHERE id_produto = %s"
            cursor.execute(query, (id_produto,))
            
            resultados = cursor.fetchall()
            cursor.close()
            
            pedidos_produtos = []
            for resultado in resultados:
                pedido_produto = PedidoProduto(
                    id_pedido=resultado['id_pedido'],
                    id_produto=resultado['id_produto'],
                    quantidade=resultado['quantidade'],
                    preco_unitario=Decimal(str(resultado['preco_unitario'])),
                    created_at=resultado['created_at']
                )
                pedidos_produtos.append(pedido_produto)
            
            return pedidos_produtos
            
        except Error as e:
            print(f"Erro ao buscar pedidos do produto: {e}")
            return []
    
    def buscar_por_id(self, id_pedido: int, id_produto: int) -> Optional[PedidoProduto]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM pedidos_produtos WHERE id_pedido = %s AND id_produto = %s"
            cursor.execute(query, (id_pedido, id_produto))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return PedidoProduto(
                    id_pedido=resultado['id_pedido'],
                    id_produto=resultado['id_produto'],
                    quantidade=resultado['quantidade'],
                    preco_unitario=Decimal(str(resultado['preco_unitario'])),
                    created_at=resultado['created_at']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar pedido-produto: {e}")
            return None
    
    def atualizar(self, pedido_produto: PedidoProduto) -> bool:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                UPDATE pedidos_produtos 
                SET quantidade = %s, preco_unitario = %s
                WHERE id_pedido = %s AND id_produto = %s
            """
            valores = (
                pedido_produto.quantidade,
                pedido_produto.preco_unitario,
                pedido_produto.id_pedido,
                pedido_produto.id_produto
            )
            
            cursor.execute(query, valores)
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Produto ID {pedido_produto.id_produto} do pedido ID {pedido_produto.id_pedido} atualizado!")
                return True
            else:
                print(f"Relacionamento não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao atualizar pedido-produto: {e}")
            return False
    
    def deletar(self, id_pedido: int, id_produto: int) -> bool:
    
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM pedidos_produtos WHERE id_pedido = %s AND id_produto = %s"
            cursor.execute(query, (id_pedido, id_produto))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Produto ID {id_produto} removido do pedido ID {id_pedido}!")
                return True
            else:
                print(f"Relacionamento não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao deletar pedido-produto: {e}")
            return False
    
    def deletar_por_pedido(self, id_pedido: int) -> bool:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM pedidos_produtos WHERE id_pedido = %s"
            cursor.execute(query, (id_pedido,))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            print(f"{linhas_afetadas} produto(s) removido(s) do pedido ID {id_pedido}!")
            return True
                
        except Error as e:
            print(f"Erro ao deletar produtos do pedido: {e}")
            return False
    
    def buscar_produtos_detalhados_por_pedido(self, id_pedido: int) -> List[dict]:
   
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT 
                    pp.id_pedido,
                    pp.id_produto,
                    p.nome,
                    pp.quantidade,
                    pp.preco_unitario,
                    (pp.quantidade * pp.preco_unitario) as subtotal
                FROM pedidos_produtos pp
                INNER JOIN produtos p ON pp.id_produto = p.id_produto
                WHERE pp.id_pedido = %s
                ORDER BY p.nome
            """
            cursor.execute(query, (id_pedido,))
            
            resultados = cursor.fetchall()
            cursor.close()
            
            return resultados
            
        except Error as e:
            print(f"Erro ao buscar produtos detalhados: {e}")
            return []
