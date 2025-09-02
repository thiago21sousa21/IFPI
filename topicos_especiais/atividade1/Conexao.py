import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host = self.host,
                user = self.usuario,
                password = self.senha,
                database = self.banco
            )

            self.cursor = self.conexao.cursor()
            print(f"Conexão realizada com sucesso")
        except Error as e:
            print(f"Erro ao conectar: {e}")

    def executar(self, query, valores=None):
        try:
            self.cursor.execute(query, valores or ())
            if not query.strip().lower().startswith("select"):
                self.conexao.commit()
            print("query executada com sucesso")
        except Error as e:
            print(f"Erro ao executar a query: {e}")

    def buscar(self):
        """retorna os resultadados da ultima query select"""
        return self.cursor.fetchall()
    
    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
        print(f"Conexão encerrada")

