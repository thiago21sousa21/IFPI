
from typing import List, Optional
from decimal import Decimal
from mysql.connector import Error
from models.produto import Produto
from conexao import Conexao


class ProdutoDAO:
    
    
    def __init__(self, conexao: Conexao):
    
        self.conexao = conexao
    
    def criar(self, produto: Produto) -> Optional[int]:
      
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO produtos (nome, preco, estoque)
                VALUES (%s, %s, %s)
            """
            valores = (produto.nome, produto.preco, produto.estoque)
            
            cursor.execute(query, valores)
            conn.commit()
            
            produto_id = cursor.lastrowid
            cursor.close()
            
            print(f"Produto '{produto.nome}' criado com sucesso! ID: {produto_id}")
            return produto_id
            
        except Error as e:
            print(f"Erro ao criar produto: {e}")
            return None
    
    def buscar_por_id(self, id_produto: int) -> Optional[Produto]:
      
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM produtos WHERE id_produto = %s"
            cursor.execute(query, (id_produto,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Produto(
                    id_produto=resultado['id_produto'],
                    nome=resultado['nome'],
                    preco=Decimal(str(resultado['preco'])),
                    estoque=resultado['estoque'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar produto: {e}")
            return None
    
    def buscar_todos(self) -> List[Produto]:
        
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM produtos ORDER BY nome"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            cursor.close()
            
            produtos = []
            for resultado in resultados:
                produto = Produto(
                    id_produto=resultado['id_produto'],
                    nome=resultado['nome'],
                    preco=Decimal(str(resultado['preco'])),
                    estoque=resultado['estoque'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
                produtos.append(produto)
            
            return produtos
            
        except Error as e:
            print(f"Erro ao buscar produtos: {e}")
            return []
    
    def atualizar(self, produto: Produto) -> bool:
      
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                UPDATE produtos 
                SET nome = %s, preco = %s, estoque = %s
                WHERE id_produto = %s
            """
            valores = (produto.nome, produto.preco, produto.estoque, produto.id_produto)
            
            cursor.execute(query, valores)
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Produto ID {produto.id_produto} atualizado com sucesso!")
                return True
            else:
                print(f"Produto ID {produto.id_produto} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao atualizar produto: {e}")
            return False
    
    def deletar(self, id_produto: int) -> bool:
       
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM produtos WHERE id_produto = %s"
            cursor.execute(query, (id_produto,))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Produto ID {id_produto} deletado com sucesso!")
                return True
            else:
                print(f"Produto ID {id_produto} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao deletar produto: {e}")
            return False
    
    def buscar_por_preco_maior_que(self, preco_minimo: Decimal) -> List[Produto]:
       
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM produtos WHERE preco > %s ORDER BY preco DESC"
            cursor.execute(query, (preco_minimo,))
            
            resultados = cursor.fetchall()
            cursor.close()
            
            produtos = []
            for resultado in resultados:
                produto = Produto(
                    id_produto=resultado['id_produto'],
                    nome=resultado['nome'],
                    preco=Decimal(str(resultado['preco'])),
                    estoque=resultado['estoque'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
                produtos.append(produto)
            
            return produtos
            
        except Error as e:
            print(f"Erro ao buscar produtos por preço: {e}")
            return []
    
    def atualizar_estoque(self, id_produto: int, quantidade: int) -> bool:
     
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "UPDATE produtos SET estoque = %s WHERE id_produto = %s"
            cursor.execute(query, (quantidade, id_produto))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Estoque do produto ID {id_produto} atualizado para {quantidade}!")
                return True
            else:
                print(f"Produto ID {id_produto} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao atualizar estoque: {e}")
            return False
