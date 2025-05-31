from datetime import datetime, timedelta

class Estilizar:
    __escape_fim = "\033[m"
    def __init__(self, texto:str ,cor_letra=30, cor_fundo=40, estilo=0):
        self.__escape_inicio = f'\033[{estilo};{cor_letra};{cor_fundo}m'
        self.__texto = texto
    
    def __str__(self):
        return f'{self.__escape_inicio}{self.__texto}{Estilizar.__escape_fim}'
    
    def printar(self):
        print(f'{self.__escape_inicio}{self.__texto}{Estilizar.__escape_fim}')

class ReservaHotel:
    __contagem_reservas = 0
    
    def __init__(self, nome_hospede, tipo_quarto, data_checkin, data_checkout):
        
        if tipo_quarto not in ['simples', 'duplo', 'luxo']:
            raise ValueError("Tipo de quarto inválido. Escolha: 'simples', 'duplo' ou 'luxo'.")
        
        ReservaHotel.__contagem_reservas += 1
        self.__numero_reserva = ReservaHotel.__contagem_reservas
        self.data_atual = datetime.now().date()
        self.__nome_hospede = nome_hospede
        self.__tipo_quarto = tipo_quarto
        self.__data_checkin = self.__validar_data_checkin(datetime.strptime(data_checkin, "%d-%m-%Y").date())
        self.__data_checkout = self.__validar_data_checkout(datetime.strptime(data_checkout, "%d-%m-%Y").date())
        self.__quantidade_diarias = (self.__data_checkout - self.__data_checkin).days
        self.__status_reserva = "ativa"
        self.__valor_total = self.__calcular_valor_total()
        
    @property
    def numero_reserva(self):
        return self.__numero_reserva
    
    @property
    def nome_hospede(self):
        return self.__nome_hospede
    
    @property
    def tipo_quarto(self):
        return self.__tipo_quarto
    
    @property
    def data_checkin(self):
        return self.__data_checkin

    @property
    def data_checkout(self):
        return self.__data_checkout

    @property
    def quantidade_diarias(self):
        return self.__quantidade_diarias

    @property
    def valor_total(self):
        return self.__valor_total
    
    @property
    def status_reserva(self):
        return self.__status_reserva

    def __validar_data_checkin(self, data_checkin):
        """verificar se a data de checkin é maior que a data atual"""
        if data_checkin < self.data_atual:
            raise Exception(" A data de checkin não pode ser anterior a data atual")
        return data_checkin
        
    def __validar_data_checkout(self, data_checkout):      
        if data_checkout <= self.__data_checkin:
            raise Exception(" A data de checkout tem que ser maior que a de checkin")
        return data_checkout
        
    def __calcular_valor_total(self):
        precos = {
            'simples': 150,
            'duplo': 250,
            'luxo': 400
        }

        preco_diaria = precos[self.__tipo_quarto]

        # Verificar se há alta temporada (dezembro, janeiro, julho)
        if self.__data_checkin.month in [12, 1, 7]:
            preco_diaria *= 1.20  # acréscimo de 20%

        total = preco_diaria * self.__quantidade_diarias
        return total
    
    def concluir_reserva(self):
        if datetime.now().date() < self.__data_checkout:
            raise Exception("Não é possível concluir antes da data de check-out.")
        if self.__status_reserva == "cancelada":
            raise Exception("Reserva já está cancelada.")        
        if self.__status_reserva == "concluída":
            raise Exception("Reserva já está concluída.")      
        self.__status_reserva = "concluída"

    def cancelar_reserva(self, data_cancelamento):
        data_cancelamento = datetime.strptime(data_cancelamento, "%d-%m-%Y").date()
        if self.__status_reserva == "concluída":
            raise Exception("Não é possível cancelar uma reserva concluída.")

        dias_antecedencia = (self.__data_checkin - data_cancelamento).days

        if dias_antecedencia >= 5:
            multa = 0
        else:
            multa = 0.5 * self.__valor_total

        self.__status_reserva = "cancelada"
        print(f"Reserva {self.__numero_reserva} cancelada. Multa: R${multa:.2f}")
        
    def alterar_reserva(self, nova_data_checkin, nova_data_checkout, data_alteracao):
        nova_data_checkin = datetime.strptime(nova_data_checkin, "%d-%m-%Y").date()
        nova_data_checkout = datetime.strptime(nova_data_checkout, "%d-%m-%Y").date()
        data_alteracao = datetime.strptime(data_alteracao, "%d-%m-%Y").date()
        
        if self.__status_reserva == "cancelada":
            raise Exception("Reserva já está cancelada.")        
        if self.__status_reserva == "concluída":
            raise Exception("Reserva já está concluída.")   

        dias_antecedencia = (self.__data_checkin - data_alteracao).days

        if dias_antecedencia < 5:
            raise Exception("Alterações só podem ser feitas até 5 dias antes do check-in.")

        self.__validar_data_checkin(nova_data_checkin)

        if nova_data_checkout <= nova_data_checkin:
            raise Exception("Data de check-out deve ser após check-in.")
        
        

        self.__data_checkin = nova_data_checkin
        self.__data_checkout = nova_data_checkout

        self.__quantidade_diarias = (self.__data_checkout - self.__data_checkin).days
        self.__valor_total = self.__calcular_valor_total()
        print(f"Reserva {self.__numero_reserva} alterada com sucesso!")
        
    def __str__(self):
        texto = f"""
        
        numero da reserva: {self.numero_reserva}
        nome do hospede: {self.nome_hospede}
        tipo de quarto: {self.tipo_quarto}
        data do checkin: {self.data_checkin}
        data do checkout: {self.data_checkout}
        status da reserva: {self.status_reserva}
        quantidade de diarias: {self.quantidade_diarias}
        """
        return str(Estilizar(texto, 30, 44, 1))
    
    def consultar_reserva(self):
        print(self.__str__())
    
# reserva = ReservaHotel( nome_hospede = "thiago", tipo_quarto ="luxo", data_checkin = "10-06-2025", data_checkout="11-06-2025")
# reserva.alterar_reserva('06-06-2025','10-06-2025','05-06-2025')
# reserva.consultar_reserva()

        
def menu():
    reservas = []
    while True:
        print(Estilizar("\n=== MENU DE RESERVAS ===", 30, 42, 1))
        print("""
              
              1 - CRIAR RESERVA
              2 - CONSULTAR TODAS RESERVAS
              3 - CONSULTAR UMA RESERVA EM ESPECIFICO
              4 - ALTERAR RESERVA
              5 - CANCELAR RESERVA
              6 - SAIR
              """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                Estilizar("Criando reserva ...", 35, 48, 1).printar()

                
                
                nome_hospede = input("Digite seu nome: ")
                tipo_quarto = input("Escolha o tipo tipo de quarto [simples, duplo, luxo]: ")
                data_checkin = input("Data de data_checkin (DD-MM-AAAA): ")
                data_checkout = input("Data de data_checkin (DD-MM-AAAA): ")
                
                reserva = ReservaHotel(nome_hospede=nome_hospede, tipo_quarto=tipo_quarto, data_checkin= data_checkin, data_checkout=data_checkout)
                
                reservas.append(reserva)
                print(Estilizar("Reserva criado com sucesso!", 34, 40, 1))
            except Exception as e:
                print(e)

        elif opcao == "2":
            Estilizar("Exibindo reservas ...", 35, 48, 1).printar()
            if not reservas:
                print("Nenhuma reserva criada.")
            else:
                for r in reservas:
                    print(r)

        elif opcao == "3":
            Estilizar("Ver uma reserva ...", 35, 48, 1).printar()
            try:
                num = int(input("Número da reserva: "))
                reserva = next(r for r in reservas if r.numero_reserva == num)                      
                print(reserva)
                
            except StopIteration:
                print(Estilizar("Reserva não encontrada", 35, 40, 4))
            except Exception as e:
                print(e)

        elif opcao == "4":
            Estilizar("Alterando uma reserva ...", 35, 48, 1).printar()
            try:
                num = int(input("Número da reserva: "))
                reserva = next(r for r in reservas if r.numero_reserva == num)            
                # reserva.alterar_reserva('06-06-2025','10-06-2025','05-06-2025')
                novo_checkin  = input("Digite nova data de checkin (DD-MM-AAAA): ")
                novo_checkout  = input("Digite nova data de checkout (DD-MM-AAAA): ")
                data_alteracao = input("Digite a data da alteração (DD-MM-AAAA) se for a data de hoje não precisa digitar nada(tecla enter): ")
                if not data_alteracao:
                    data_alteracao = datetime.now().date().strftime("%d-%m-%Y")
                    print(f"DENTRO DO IF VALOR {data_alteracao}")
                reserva.alterar_reserva(novo_checkin, novo_checkout, data_alteracao)
                print(reserva)                    
            except StopIteration:
                print(Estilizar("Boleto não encontrado.", 35, 40, 4))
            except Exception as e:
                print(e)
                
        
        elif opcao == "5":
            Estilizar("Calcelar uma reserva ...", 35, 48, 1).printar()
            try:
                num = int(input("Número da reserva: "))
                reserva = next(r for r in reservas if r.numero_reserva == num)            
                data_cancelamento = input("Digite a data do cancelamento (DD-MM-AAAA) se for a data de hoje não precisa digitar nada(tecla enter): ")
                if not data_cancelamento:
                    data_cancelamento = datetime.now().date().strftime("%d-%m-%Y")
                reserva.cancelar_reserva(data_cancelamento)
                print(reserva)                    
            except StopIteration:
                print(Estilizar("Boleto não encontrado.", 35, 40, 4))
            except Exception as e:
                print(e)

        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print(Estilizar("Opção inválida.", 35, 40, 4))
 
        
if __name__ == "__main__":
    menu()
