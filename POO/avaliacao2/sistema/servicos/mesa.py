from ..modelos.cliente import Cliente
from .pedido import Pedido
from ..modelos.bebida import Bebida

class Mesa:
    """
    Representa uma mesa do restaurante, que pode ter múltiplos pedidos.
    """
    def __init__(self, numero):
        self.numero = numero
        self.pedidos = []

    def registrar_pedido(self, cliente: Cliente, itens: list):
        """
        Adiciona um novo pedido para um cliente na mesa.
        """
        try:
            pedido = Pedido(cliente)
            for item in itens:
                pedido.adicionar_item(item)
            self.pedidos.append(pedido)
            print(f"Cliente {cliente.nome} fez um pedido na mesa {self.numero}:")
            pedido.exibir_itens()
        except (TypeError, ValueError) as e:
            print(f"Erro ao registrar pedido: {e}") # Tratamento de exceção


    def calcular_total(self):
        """
        Calcula o valor total da conta da mesa.
        """
        total = 0
        for pedido in self.pedidos:
            for item in pedido.itens:
                total += item.calcular_preco()
        return total

    def imprimir_conta_detalhada(self):
        """
        Método polimórfico para imprimir os detalhes da conta da mesa.
        """
        print(f"\nResumo da mesa {self.numero}:")
        if not self.pedidos:
            print("Nenhum pedido registrado nesta mesa.")
            return

        detalhes_por_cliente = {}
        for pedido in self.pedidos:
            nome_cliente = pedido.cliente.nome
            if nome_cliente not in detalhes_por_cliente:
                detalhes_por_cliente[nome_cliente] = []

            for item in pedido.itens:
                # Polimorfismo: o preço é calculado de forma diferente para Prato e Bebida
                preco = item.calcular_preco()
                if isinstance(item, Bebida):
                     detalhes_por_cliente[nome_cliente].append(f"{item.nome} {item.tamanho} (R$ {preco:.2f})")
                else:
                     detalhes_por_cliente[nome_cliente].append(f"{item.nome} (R$ {preco:.2f})")

        resumo_str = []
        for cliente, itens_str in detalhes_por_cliente.items():
            resumo_str.append(f"- {cliente}: {', '.join(itens_str)}")

        print(' '.join(resumo_str))
        print(f"Total: R$ {self.calcular_total():.2f}")