from typing import List
class Abstracao:

    @staticmethod
    def selectAllObjects(lista:List):
        nova_lista = []
        for e in lista:
            nova_lista.append(vars(e))
        return nova_lista
