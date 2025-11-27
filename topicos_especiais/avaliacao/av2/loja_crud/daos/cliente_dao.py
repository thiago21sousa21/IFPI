from typing import List, Optional
from mysql.connector import Error
from models.cliente import Cliente
from conexao import Conexao


class ClienteDAO:
    
    def __init__(self, conexao: Conexao):
        self.conexao = conexao
    
    def criar(self, cliente: Cliente) -> Optional[int]:
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO clientes (nome, email, telefone)
                VALUES (%s, %s, %s)
            """
            valores = (cliente.nome, cliente.email, cliente.telefone)
            
            cursor.execute(query, valores)
            conn.commit()
            
            cliente_id = cursor.lastrowid
            cursor.close()
            
            print(f"Cliente '{cliente.nome}' criado com sucesso! ID: {cliente_id}")
            return cliente_id
            
        except Error as e:
            print(f"Erro ao criar cliente: {e}")
            return None
    
    def buscar_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """
        Busca um cliente por ID
        
        Args:
            id_cliente: ID do cliente a ser buscado
            
        Returns:
            Objeto Cliente ou None se não encontrado
        """
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM clientes WHERE id_cliente = %s"
            cursor.execute(query, (id_cliente,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Cliente(
                    id_cliente=resultado['id_cliente'],
                    nome=resultado['nome'],
                    email=resultado['email'],
                    telefone=resultado['telefone'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar cliente: {e}")
            return None
    
    def buscar_todos(self) -> List[Cliente]:
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM clientes ORDER BY nome"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            cursor.close()
            
            clientes = []
            for resultado in resultados:
                cliente = Cliente(
                    id_cliente=resultado['id_cliente'],
                    nome=resultado['nome'],
                    email=resultado['email'],
                    telefone=resultado['telefone'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
                clientes.append(cliente)
            
            return clientes
            
        except Error as e:
            print(f"Erro ao buscar clientes: {e}")
            return []
    
    def atualizar(self, cliente: Cliente) -> bool:
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = """
                UPDATE clientes 
                SET nome = %s, email = %s, telefone = %s
                WHERE id_cliente = %s
            """
            valores = (cliente.nome, cliente.email, cliente.telefone, cliente.id_cliente)
            
            cursor.execute(query, valores)
            conn.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()

            if linhas_afetadas > 0:
                print(f"Cliente ID {cliente.id_cliente} atualizado com sucesso!")
                return True
            else:
                print(f"Cliente ID {cliente.id_cliente} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao atualizar cliente: {e}")
            return False
    
    def deletar(self, id_cliente: int) -> bool:
        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(query, (id_cliente,))
            conn.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            if linhas_afetadas > 0:
                print(f"Cliente ID {id_cliente} deletado com sucesso!")
                return True
            else:
                print(f"Cliente ID {id_cliente} não encontrado.")
                return False
                
        except Error as e:
            print(f"Erro ao deletar cliente: {e}")
            return False
    
    def buscar_por_email(self, email: str) -> Optional[Cliente]:

        try:
            conn = self.conexao.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT * FROM clientes WHERE email = %s"
            cursor.execute(query, (email,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Cliente(
                    id_cliente=resultado['id_cliente'],
                    nome=resultado['nome'],
                    email=resultado['email'],
                    telefone=resultado['telefone'],
                    created_at=resultado['created_at'],
                    updated_at=resultado['updated_at']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar cliente por email: {e}")
            return None
