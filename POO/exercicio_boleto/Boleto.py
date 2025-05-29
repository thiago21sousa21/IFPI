class Boleto:
    numero_boleto = 0
    def __init__(self):
        Boleto.numero_boleto += 1
        self.__numero = Boleto.numero_boleto
        self.__nome_do_pagador = ""
        self.__data_emissao = ""
        self.__data_vencimento = ""
        self.__data_pagamento = ""
        #Status do boleto: "em aberto", "pago", "vencido", “cancelado” // Inicialmente: “em aberto”
        self.__status_do_boleto = "em aberto"
        self.__valor_final = 0

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome_do_pagador(self):
        return self.__nome_do_pagador
    
    @property
    def data_emissao(self):
        return self.data_emissao
    
    @property
    def



        