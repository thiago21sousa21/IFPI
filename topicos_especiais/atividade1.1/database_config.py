from dotenv import DotEnv

env = DotEnv().data

class Config_db:

    def __init__(self):
        self.__DB_HOST = env["DB_HOST"]
        self.__DB_USER = env["DB_USER"]
        self.__DB_PORT = env["DB_PORT"]
        self.__DB_PASSWORD = env["DB_PASSWORD"]
        self.__DB_DATABASE = env["DB_DATABASE"]
        self.args = self.retorna_argumentos()
    
    def retorna_argumentos(self):
        return {
            "host":self.__DB_HOST, 
            "user":self.__DB_USER, 
            "port": self.__DB_PORT, 
            "password":self.__DB_PASSWORD,
            "database":self.__DB_DATABASE
        }
    