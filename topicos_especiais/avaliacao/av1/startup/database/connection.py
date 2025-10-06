import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnection: 
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conexao = mysql.connector.connect(
                user = os.getenv("USER_DB", "root"),
                password = os.getenv("PASSWORD_DB", "123456"),
                host = os.getenv("HOST_BD", "localhost"),
                database = os.getenv("DATABASE", "startup")
            )
            self.cursor = self.conexao.cursor(dictionary=True)
            return self
        except Error as e:
            print(f"Não foi possivel estabelecer uma conexão com o banco de dados!: {e}")
            raise

    def __exit__(self, a, b, c):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexao:
                self.conexao.close()
        except Error as e:
            print(f"Erro ao finalizar conexão: {e}")
            raise

    def execute_query(self, query, params = None):
        try:
            self.cursor.execute(query, params or ())
            self.conexao.commit()
            return self.cursor.lastrowid
        except Error as e:
            self.conexao.rollback()
            print(f"Não foi possivel executar a query:\n {query}:\n {e}")
            raise

    def fetch_one(self, query, params = None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            print(f"Não foi possivel executar a query:\n {query}:\n {e}")
            raise
    
    def fetch_all(self, query, params = None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            print(f"Não foi possivel executar a query:\n {query}:\n {e}")
            raise
