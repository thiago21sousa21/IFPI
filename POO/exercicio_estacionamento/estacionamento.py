# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de estacionamento de shopping. Identifique atributos mutáveis e imutáveis,
# implemente um construtor da classe e métodos para manipulação dos atributos mutáveis.
# Faça todas as validações possíveis. Utilize encapsulamento nos atributos necessários
# implementando em seguida os decoradores de leitura e/ou escrita. Crie objetos para testar os
# métodos implementados.

from datetime import datetime, timedelta

class Estacionamento:

    numero_cartao = 0
    def __init__(self, placa_veiculo: str):
        # 1. Atributos:
        # - Número do cartão (gerado automaticamente)
        self.numero_cartao += 1
        # - Placa do veículo (string)
        self.__placa_veiculo = placa_veiculo
        # - Data e hora de entrada (registrada automaticamente no momento da criação do cartão)
        self.__data_hora_entrada = datetime.now()
        # - Status do cartão ("aberto" ou "finalizado")
        self.__status = "aberto"
        # - Data e hora de saída (registrada quando o cartão é finalizado)
        self.__data_hora_saida = None
        # - Valor total a ser pago (calculado com base no tempo de permanência)
        self.__valor_total = 0.0



    # 2. Métodos:
    def registrar_pagamento(self, data_hora_saida: datetime = datetime.now()):
        # - Um método para registrar o pagamento, que define a data e hora de saída, altera o
        # status para "pago" e calcula o valor total a ser pago.
        if self.__status == "aberto":
            self.__data_hora_saida = data_hora_saida
            self.__status = "pago"
            self.__valor_total = self.calcular_valor_pago()
        else:
            raise ValueError("O cartão já foi finalizado.")


# - Um método para consultar o valor acumulado, permitindo ao cliente verificar o custo do
# estacionamento antes de finalizar.
# - Um método para calcular o valor a ser pago, condiderando:
# - Até 2h de permanência, R$ 8,00
# - Acima de 2h de permanência cobrar R$ 0,50 a cada fração de 15 min

# 4. Requisitos de Validação
# - O número do cartão deve ser único .
# - Placa do veículo

# - Um método para registrar a saída: Verificar se o cartão foi pago e se a hora de
# pagamento for menor ou igual a 1 hora. Mudar o status do cartão para "finalizado"

# - O status só pode ser alterado para "finalizado" se o pagamento for executado.
# - O tempo de permanência deve ser calculado em horas completas e frações, considerando
# uma tarifa fixa por hora.
# - A data e hora de saída não podem ser anteriores à data e hora de entrada.

# 5. Teste:
# - Crie pelo menos três objetos da classe, representando cartões de estacionamento
# diferentes.
# - Demonstre os métodos implementados e suas validações em ação.