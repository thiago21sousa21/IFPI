from datetime import datetime, timedelta

class BoletoStatus:
    __aberto = "aberto"
    __pago = "pago"
    __vencido = "vencido"
    __cancelado = "cancelado"

    @property
    def aberto(self): return self.__aberto
    @property
    def pago(self): return self.__pago  
    @property
    def vencido(self): return self.__vencido
    @property
    def cancelado(self): return self.__cancelado  


class Estilizar:
    __escape_fim = "\033[m"
    def __init__(self, texto:str ,cor_letra=30, cor_fundo=40, estilo=0):
        self.__escape_inicio = f'\033[{estilo};{cor_letra};{cor_fundo}m'
        self.__texto = texto
    
    def __str__(self):
        return f'{self.__escape_inicio}{self.__texto}{Estilizar.__escape_fim}'


class Boleto:
    __contador = 0

    def __init__(self, valor_original: float, data_vencimento: str):
        if valor_original <= 0:
            raise Exception(str(Estilizar("Valor deve ser positivo", 35, 40, 4)))

        Boleto.__contador += 1
        self.__numero = Boleto.__contador
        self.__nome_do_pagador = None
        self.__valor_original = valor_original
        self.__data_emissao = datetime.now()
        self.__data_vencimento = self.__verificar_dia_vencimento(
            datetime.strptime(data_vencimento, "%d-%m-%Y"))
        self.__data_pagamento = None
        self.__status_boleto = BoletoStatus().aberto
        self.__valor_final = 0.00

    def __str__(self):
        texto = f"""Número: {self.numero}
Nome do Pagador: {self.nome_do_pagador}
Valor Original: R$ {self.valor_original:.2f}
Data de Emissão: {self.data_emissao}
Data de Vencimento: {self.data_vencimento}
Data de Pagamento: {self.data_pagamento}
Status: {self.status_boleto}
Valor Final: R$ {self.valor_final:.2f}"""
        return str(Estilizar(texto, 33, 40, 1))

    @property
    def numero(self): return self.__numero
    @property
    def nome_do_pagador(self): return self.__nome_do_pagador
    @nome_do_pagador.setter
    def nome_do_pagador(self, nome): self.__nome_do_pagador = nome
    @property
    def valor_original(self): return self.__valor_original
    @property
    def data_emissao(self): return self.__data_emissao
    @property
    def data_vencimento(self): return self.__data_vencimento
    @property
    def data_pagamento(self): return self.__data_pagamento
    @property
    def status_boleto(self): return self.__status_boleto
    @property
    def valor_final(self): return self.__valor_final

    def __verificar_dia_vencimento(self, data):
        data = data.replace(hour=23, minute=59, second=59)
        if data < self.__data_emissao:
            raise Exception(str(Estilizar("Data de vencimento não pode ser anterior à emissão.", 35, 40, 4)))
        return data

    def __calcular_dias_atrasados(self, vencimento, pagamento):
        return max(0, (pagamento - vencimento).days)

    def __calcular_valor_final(self, pagamento):
        dias_antes = (self.__data_vencimento - pagamento).days
        dias_atraso = self.__calcular_dias_atrasados(self.__data_vencimento, pagamento)

        if dias_antes >= 3:
            desconto = self.__valor_original * 0.05
            return self.__valor_original - desconto
        elif pagamento > self.__data_vencimento:
            multa = self.__valor_original * 0.02
            juros = self.__valor_original * 0.0003 * dias_atraso
            return self.__valor_original + multa + juros
        else:
            return self.__valor_original

    def pagar(self, nome_pagador, valor_pago, data_pagamento=None):
        if self.__status_boleto == BoletoStatus().pago:
            raise Exception(str(Estilizar("Este boleto já foi pago.", 35, 40, 4)))
        if self.__status_boleto == BoletoStatus().cancelado:
            raise Exception(str(Estilizar("Este boleto foi cancelado.", 35, 40, 4)))

        if not data_pagamento:
            data_pagamento = datetime.now()
        else:
            try:
                data_pagamento = datetime.strptime(data_pagamento, "%d-%m-%Y")
            except:
                raise Exception(str(Estilizar("Formato de data inválido. Use DD-MM-AAAA.", 35, 40, 4)))

        if data_pagamento < self.__data_emissao:
            raise Exception(str(Estilizar("Data de pagamento não pode ser anterior à emissão.", 35, 40, 4)))

        valor_calculado = self.__calcular_valor_final(data_pagamento)

        if valor_pago < valor_calculado:
            raise Exception(str(Estilizar("Valor insuficiente para quitar o boleto.", 35, 40, 4)))

        self.__valor_final = valor_calculado
        self.__data_pagamento = data_pagamento
        self.__nome_do_pagador = nome_pagador
        self.__status_boleto = BoletoStatus().pago
        troco = valor_pago - valor_calculado
        return f"Pagamento registrado com sucesso. Troco: R$ {troco:.2f}"

    def cancelar(self):
        if self.__status_boleto == BoletoStatus().pago:
            raise Exception(str(Estilizar("Não é possível cancelar um boleto já pago.", 35, 40, 4)))
        self.__status_boleto = BoletoStatus().cancelado
        return "Boleto cancelado com sucesso."

def menu():
    boletos = []
    while True:
        print(Estilizar("\n=== MENU DE BOLETOS ===", 32, 40, 1))
        print("1. Criar boleto")
        print("2. Ver boletos")
        print("3. Pagar boleto")
        print("4. Cancelar boleto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Valor do boleto: R$ "))
                vencimento = input("Data de vencimento (DD-MM-AAAA): ")
                boleto = Boleto(valor, vencimento)
                boletos.append(boleto)
                print(Estilizar("Boleto criado com sucesso!", 34, 40, 1))
            except Exception as e:
                print(e)

        elif opcao == "2":
            if not boletos:
                print("Nenhum boleto criado.")
            else:
                for b in boletos:
                    print(b)

        elif opcao == "3":
            try:
                num = int(input("Número do boleto: "))
                boleto = next(b for b in boletos if b.numero == num)
                nome = input("Nome do pagador: ")
                valor = float(input("Valor pago: R$ "))
                data = input("Data de pagamento (DD-MM-AAAA) [enter = hoje]: ") or None
                print(boleto.pagar(nome, valor, data))
            except StopIteration:
                print(Estilizar("Boleto não encontrado.", 35, 40, 4))
            except Exception as e:
                print(e)

        elif opcao == "4":
            try:
                num = int(input("Número do boleto: "))
                boleto = next(b for b in boletos if b.numero == num)
                print(boleto.cancelar())
            except StopIteration:
                print(Estilizar("Boleto não encontrado.", 35, 40, 4))
            except Exception as e:
                print(e)

        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print(Estilizar("Opção inválida.", 35, 40, 4))


# Iniciar o menu
if __name__ == "__main__":
    menu()
