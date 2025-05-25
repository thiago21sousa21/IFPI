from datetime import datetime, timedelta
import uuid


class CartaoEstacionamento:
    def __init__(self, placa_veiculo: str):
        self.__numero_cartao = str(uuid.uuid4())  # número único
        self.__placa_veiculo = placa_veiculo.strip().upper()
        self.__data_entrada = datetime.now()
        self.__data_saida = None
        self.__status = "aberto"
        self.__valor_total = 0.0
        self.__data_pagamento = None

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def placa_veiculo(self):
        return self.__placa_veiculo

    @property
    def data_entrada(self):
        return self.__data_entrada

    @property
    def status(self):
        return self.__status

    @property
    def data_saida(self):
        return self.__data_saida

    @property
    def valor_total(self):
        return self.__valor_total

    def calcular_valor(self, tempo_personalizado=None):
        fim = tempo_personalizado if tempo_personalizado else datetime.now()
        tempo_total = fim - self.__data_entrada
        minutos = tempo_total.total_seconds() / 60

        if minutos <= 120:
            return 8.0
        else:
            minutos_excedentes = minutos - 120
            fracoes_15_min = -(-minutos_excedentes // 15) 
            return 8.0 + (fracoes_15_min * 0.5)

    def consultar_valor(self):
        if self.__status == "aberto":
            return self.calcular_valor()
        return self.__valor_total

    def registrar_pagamento(self):
        if self.__status != "aberto":
            raise Exception("Pagamento já registrado ou cartão encerrado.")

        self.__data_pagamento = datetime.now()
        self.__valor_total = self.calcular_valor(self.__data_pagamento)
        self.__status = "pago"

    def registrar_saida(self):
        if self.__status != "pago":
            raise Exception("Saída não permitida: o pagamento ainda não foi realizado.")

        agora = datetime.now()
        tempo_pos_pagamento = agora - self.__data_pagamento

        if tempo_pos_pagamento > timedelta(hours=1):
            raise Exception("Saída não permitida: mais de 1 hora após o pagamento.")

        self.__data_saida = agora
        if self.__data_saida < self.__data_entrada:
            raise Exception("Erro: saída anterior à entrada.")

        self.__status = "finalizado"

    def __str__(self):
        return (f"Cartão: {self.__numero_cartao}\n"
                f"Placa: {self.__placa_veiculo}\n"
                f"Entrada: {self.__data_entrada.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Saída: {self.__data_saida.strftime('%d/%m/%Y %H:%M:%S') if self.__data_saida else '---'}\n"
                f"Status: {self.__status}\n"
                f"Valor Total: R$ {self.__valor_total:.2f}\n")

from time import sleep

cartao1 = CartaoEstacionamento("ABC-1234")
sleep(2) 
print("Valor acumulado cartão 1:", cartao1.consultar_valor())
cartao1.registrar_pagamento()
sleep(2)
cartao1.registrar_saida()
print(cartao1)

cartao2 = CartaoEstacionamento("XYZ-9876")
try:
    cartao2.registrar_saida()
except Exception as e:
    print("Erro esperado cartão 2:", e)

cartao3 = CartaoEstacionamento("DEF-4567")
cartao3._CartaoEstacionamento__data_entrada -= timedelta(hours=3)
print("Valor acumulado cartão 3:", cartao3.consultar_valor())  # Deve calcular extra
cartao3.registrar_pagamento()
cartao3.registrar_saida()
print(cartao3)
