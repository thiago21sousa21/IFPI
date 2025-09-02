from datetime import datetime

class Professor:
    def __init__(self, nome: str, sobrenome: str, matricula: str, data_nascimento: str, email: str):
        self.__nome: str = self.isString(nome)
        self.__sobrenome: str = self.isString(sobrenome)
        self.__matricula: str = self.isString(matricula)
        self.__data_nascimento = self.isDate(data_nascimento)
        self.__email: str = self.isEmail(email)

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def email(self):
        return self.__email

    def isString(self, string):
        if not isinstance(string, str) or string.strip() == "":
            raise TypeError("O valor deve ser uma string não vazia.")
        return string

    def isDate(self, data):
        self.isString(data)
        for formato in ["%Y-%m-%d", "%d/%m/%Y"]:
            try:
                return datetime.strptime(data, formato).date()
            except ValueError:
                pass
        raise ValueError("Data inválida. Use o formato YYYY-MM-DD ou DD/MM/YYYY.")

    def isEmail(self, email):
        self.isString(email)
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email inválido.")
        return email

    def __str__(self):
        return (f"Nome: {self.__nome} {self.__sobrenome}, "
                f"Matrícula: {self.__matricula}, "
                f"Data de Nascimento: {self.__data_nascimento}, "
                f"Email: {self.__email}")
