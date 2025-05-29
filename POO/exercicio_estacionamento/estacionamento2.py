# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de estacionamento de shopping. Identifique atributos mutáveis e imutáveis,
# implemente um construtor da classe e métodos para manipulação dos atributos mutáveis.
# Faça todas as validações possíveis. Utilize encapsulamento nos atributos necessários
# implementando em seguida os decoradores de leitura e/ou escrita. Crie objetos para testar os
# métodos implementados.

# Especificações:
from datetime import datetime
import re
import time

class CartaoStatus:
    __aberto = "aberto"
    __finalizado = "finalizado"

    @property
    def aberto(self):
        return self.__aberto
    
    @property
    def finalizado(self):
        return self.__finalizado
    


class CartaoEstacionamento:
    __numero_atual = 0

    def __init__(self, placa):
        CartaoEstacionamento.__numero_atual += 1
        self.__numero_cartao = CartaoEstacionamento.__numero_atual
        self.__momento_entrada = datetime.now()
        self.__status = CartaoStatus().aberto
        self.__momento_saida = None
        self.__valor_total = 0
        self.__placa = self.__validar_placa(placa)

    def __validar_placa(self, placa):
        padrao = '^[A-Z]{3}-[0-9]{4}$|^[A-Z]{3}-[0-9][A-Z][0-9]{2}$'
        correspondencia = re.match(padrao, placa.upper())
        if(correspondencia):
            return correspondencia.group()
        raise Exception("O padrão da placa não está correspondendo ao formato AAA-9999 OU AAA-9A99")
    
    def __converter_para_time(self, string_time):
        try:
            str_time = time.strptime(string_time,"%H:%M")
            print(str_time)
            return str_time
        except Exception as err:
            return str(err)

    def pagar(self, valor_recebido, momento_pagar = None):
        if momento_pagar:
            momento_pagar = self.__converter_para_time(momento_pagar)
            print(momento_pagar)
        valor_a_pagar = self.__calcular_valor()
        pass

    def consultar_valor_atual(self, momento:datetime = None):
        if not momento:
            momento = datetime.now()
        # essa função vai chamar outra que vai calcular o valor
        return f'O valor atual é: {self.__calcular_valor()}'

    def __calcular_valor(self, momento: datetime = None):
        #essa função vai pegar a diferença de tempo de entrada e de saida
        if not momento:
            momento = datetime.now()
        tempo_segundos = self.__retornar_diferença_tempo(self.__momento_entrada, momento)
        tempo_minutos = tempo_segundos / 60
        valor  = 8
        if tempo_minutos <= 120:
            return valor
        quizenas  = -(-tempo_minutos // 15)
        valor += quizenas * 0.5
        return valor
    
    def __retornar_diferença_tempo(self, entrada: datetime, atual: datetime):
        diferenca = atual - entrada
        return diferenca.total_seconds()
    
t = CartaoEstacionamento("nii-8044")
t.pagar(100, '12:30')


# 1. Atributos:
# - Número do cartão (gerado automaticamente)

# - Data e hora de entrada (registrada automaticamente no momento da criação do cartão)
# - Status do cartão ("aberto" ou "finalizado")
# - Data e hora de saída (registrada quando o cartão é finalizado)
# - Valor total

# 2. Métodos sugeridos
# - Um método para registrar o pagamento, que define a data e hora de saída, altera o
# status para "pago" e calcula o valor total a ser pago.

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