import mysql.connector
from mysql.connector import Error
from database_config import Config_db
from typing import Optional, Any, List, Tuple


class Connection:
    """Gerencia conexão com o banco de dados MySQL usando context manager."""

    def __init__(self, config: Optional[Config_db] = None):
        self.config = config or Config_db()
        self.conexao = None
        self.cursor = None

    def __enter__(self) -> "Connection":
        try:
            self.conexao = mysql.connector.connect(**self.config.args)
            # Aqui já pode escolher dictionary=True se quiser dicionário
            self.cursor = self.conexao.cursor()
            return self
        except Error as err:
            raise RuntimeError(f"Erro ao conectar ao banco: {err}") from err

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.cursor:
                self.cursor.close()  # não precisa checar se está "closed"
            if self.conexao and self.conexao.is_connected():
                self.conexao.close()
        except Error as err:
            raise RuntimeError(f"Erro ao fechar conexão: {err}") from err

    def buscar(self, query: str, valores: Optional[Tuple[Any, ...]] = None) -> List[Tuple]:
        """Executa uma consulta SELECT e retorna os resultados."""
        try:
            self.cursor.execute(query, valores or ())
            return self.cursor.fetchall()
        except Error as e:
            raise RuntimeError(f"Erro ao buscar dados: {e}") from e

    def executar(self, query: str, valores: Optional[Tuple[Any, ...]] = None) -> Optional[int]:
        """Executa uma query de modificação (INSERT/UPDATE/DELETE)."""
        try:
            self.cursor.execute(query, valores or ())
            self.conexao.commit()
            return self.cursor.lastrowid
        except Error as e:
            self.conexao.rollback()
            raise RuntimeError(f"Erro ao executar a query: {e}") from e
