class Disciplina:
    # O ID será definido pelo banco de dados, então não o pedimos no construtor.
    # Armazenamos o professor_id diretamente, pois é o que a tabela do BD precisa.
    def __init__(self, nome: str, carga_horaria: int, professor_id: int):
        self.__id = None  # O ID começa como None
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__professor_id = professor_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def professor_id(self):
        return self.__professor_id
    

