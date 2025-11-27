
import mysql.connector
from mysql.connector import Error
from typing import Optional


class Conexao:
    def __init__(self, host: str = 'localhost', 
                 database: str = 'loja', 
                 user: str = 'root', 
                 password: str = '123456'):
        
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection: Optional[mysql.connector.MySQLConnection] = None
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.connection.is_connected():
                print(f"Conectado ao banco de dados '{self.database}' com sucesso!")
                return self.connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
    
    def desconectar(self) -> None:
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")
    
    def get_connection(self) -> Optional[mysql.connector.MySQLConnection]:
        if not self.connection or not self.connection.is_connected():
            return self.conectar()
        return self.connection
