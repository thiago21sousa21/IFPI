import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
 
class DbConfig:
    HOST = os.getenv("DB_HOST")
    USUARIO = os.getenv("DB_USER")
    SENHA = os.getenv("DB_PASSWORD")
    BANCO = os.getenv("DB_NAME")

class Connection:
    def __init__(self, config=DbConfig):
        self.host = config.HOST
        self.usuario = config.USUARIO
        self.senha = config.SENHA
        self.banco = config.BANCO
        self.conexao = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            self.cursor = self.conexao.cursor()
            return self
        except Error as e:
            print(f"Erro ao conectar no banco: {e}")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

    def executar(self, query, valores=None):
        try:
            self.cursor.execute(query, valores or ())
            self.conexao.commit()
            # IMPORTANTE: Retorna o ID do último item inserido
            return self.cursor.lastrowid
        except Error as e:
            print(f"Erro ao executar a query: {e}")
            self.conexao.rollback()
            return None

    def buscar(self, query, valores=None):
        try:
            self.cursor.execute(query, valores or ())
            return self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return []
