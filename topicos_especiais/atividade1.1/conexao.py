import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '123456',
    database = 'escola_topicos_especiais'
)

