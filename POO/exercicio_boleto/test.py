class Boleto:
    def __init__(self):
        self.database = {}
        self.id =  1

    def cadastro(self, nome: str, valor: int):
        dados = []
        for key, value in self.database.items():
            if key == self.id:
                self.id += 1
            else: continue

        dados.append(nome)
        dados.append(valor)
        self.database[self.id] = dados

        return ">>> Dados adicionados com êxito."


    def view(self):
        print("CHAVE\t\t\tVALOR")
        for key, value in self.database.items():
            print(f"{key:<20}{value}")


if __name__ =='__main__':
    a = Boleto()
    a.cadastro("Thiago", 100)
    a.cadastro("Flavio", 500)
    a.cadastro("Viviane", 200)
    a.view()
