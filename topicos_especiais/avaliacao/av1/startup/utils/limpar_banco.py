from database.connection import DatabaseConnection

def limpar_banco():
    with DatabaseConnection() as cnn:
        cnn.execute_query("DELETE FROM amizades")
        cnn.execute_query("DELETE FROM comentarios")
        cnn.execute_query("DELETE FROM likes")
        cnn.execute_query("DELETE FROM posts")
        cnn.execute_query("DELETE FROM telefones")
        cnn.execute_query("DELETE FROM usuarios")

