# Exercício de Revisão – Boleto Bancário

# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# boleto bancário. Identifique atributos mutáveis e imutáveis, implemente um construtor da
# classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
# necessárias. Utilize encapsulamento e decoradores de leitura/escrita. Crie objetos para testar
# os métodos implementados.

from datetime import datetime, timedelta

class BoletoStatus:
    __aberto = "aberto"
    __pago = "pago"
    __vencido = "vencido"
    __cancelado = "cancelado"

    @property
    def aberto(self):
        return self.__aberto
    
    @property
    def pago(self):
        return self.__pago  

    @property
    def vencido(self):
        return self.__vencido

    @property
    def cancelado(self):
        return self.__cancelado  


class Boleto:
    __numero = 0
    def __init__ (self, valor_original:float, data_pagamento:str):
        self.__numero = Boleto.__numero
        self.__nome_do_pagador = None
        self.__valor_original = float(valor_original)
        self.__data_emissao = datetime.now()
        self.__data_vencimento =  self.__verificar_dia_vencimento(datetime.strptime(data_pagamento, "%d-%m-%Y"))
        self.__data_pagamento = None
        self.__status_boleto = BoletoStatus().aberto
        self.__valor_final  = None

    def __str__(self):
        return f"""\033[1;33;48mnumero: {self.numero}
nome do pagador: {self.nome_do_pagador}
valor original: {self.valor_original}
data emissão: {self.data_emissao}
data vencimento: {self.data_vencimento}
data pagamento: {self.data_pagamento}
status do boleto: {self.status_boleto}
valor final: {self.valor_final}\033[0m"""
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome_do_pagador(self):
        return self.__nome_do_pagador
    @nome_do_pagador.setter
    def nome_do_pagador(self, nome_pagador):
        self.__nome_do_pagador = nome_pagador
    
    @property
    def valor_original(self):
        return self.__valor_original

    @property
    def data_emissao(self):
        return self.__data_emissao

    @property
    def data_vencimento(self):
        return self.__data_vencimento
    
    @property
    def data_pagamento(self):
        return self.__data_pagamento
    
    @property
    def status_boleto(self):
        return self.__status_boleto

    @property
    def valor_final(self):
        return self.__valor_final
    
    @status_boleto.setter
    def status_boleto(self, status: str):
        self.__status_boleto = status
    
    def __verificar_dia_vencimento(self, data_vencimento: datetime ):
        data_vencimento = data_vencimento.replace(hour=23, minute=59, second=59, microsecond=999999)
        # if data_vencimento < self.data_emissao:
        #     raise "A data de vencimento não pode ser maior que a dada de emissão!"
        return data_vencimento
    
    def pagar(self, nome_pagador:str , valor:float , momento_pagamento:str = None):
        status = BoletoStatus()

        self.__definir_status()

        if self.status_boleto == status.cancelado:
            raise f'boleto encontra-se com status: {self.status_boleto}'
        
        if self.status_boleto == status.pago:
             raise f'boleto encontra-se com status: {self.status_boleto}'
        
        if self.status_boleto == status.vencido:
            # calcucar a quantos dias está vencido
            if not momento_pagamento:
                momento_pagamento = datetime.now()

            dias_de_atraso = momento_pagamento - self.data_vencimento
            print(dias_de_atraso)
        
        self.nome_do_pagador = nome_pagador

    
    def __definir_status(self, cancelar:bool = False):
        momento_atual = datetime.now()
        status = BoletoStatus()

        if self.status_boleto == status.cancelado:
            return self.status_boleto
        
        if self.data_pagamento:
            self.status_boleto = status.pago
            return self.status_boleto
        
        if cancelar:
            self.status_boleto = status.cancelado
            return self.status_boleto

        if momento_atual <= self.data_vencimento:
            self.status_boleto = status.aberto
            return self.status_boleto
        
        if momento_atual > self.data_vencimento:
            self.status_boleto = status.vencido
            return self.status_boleto

        momento_atual = datetime.now()

        
    

    
    

teste = Boleto(100, "27-05-2025")
print(teste)
teste.pagar(nome_pagador="thiago", valor=100)
print(teste)


# Especificações:
# 1. Atributos:
# • Número do boleto (gerado automaticamente e único)
# • Nome do pagador
# • Valor original
# • Data de emissão (registrada automaticamente na criação do boleto) //Não pode ser
# uma data menor que a data atual
# • Data de vencimento (definida no momento da criação)
# • Data de pagamento (registrada quando pago) // Inicialmente: None
# • Status do boleto: "em aberto", "pago", "vencido", “cancelado” // Inicialmente: “em
# aberto”
# • Valor final com juros e/ou desconto // inicialmente: 0,00

# 2. Métodos sugeridos:
# • Um método para registrar o pagamento:
    # o Define a data de pagamento
    # o Calcula o valor final (com desconto ou juros)
    # o Altera o status para "pago" ou "vencido" conforme a data

# • Um método para consultar o valor atualizado:
# o Considera:
# ▪ Desconto de 5% se pago até 3 dias antes do vencimento
# ▪ Multa de 2% + juros de 0,03% ao dia se pago após o vencimento
# • Um método para cancelar o boleto, que altera o status do boleto para “cancelado”.
# Não pode cancelar se o boleto já foi pago.

# Regras de Validação:
# • O número do boleto deve ser único
# • O valor original deve ser positivo
# • A data de vencimento deve ser posterior à emissão
# • A data de pagamento não pode ser anterior à emissão
# • O status só pode ser "pago" se o pagamento for registrado
# • O status deve mudar para "vencido" se a data atual ultrapassar o vencimento e o
# boleto ainda não tiver sido pago
# • Boleto com o status “pago” não pode ser pago novamente.

# Teste:
# • Crie pelo menos três objetos da classe, com diferentes datas de vencimento e simule
# pagamentos antecipados, pontuais e atrasados.
# • Mostre