from sistema.modelos.cliente import Cliente
from sistema.modelos.bebida import Bebida
from sistema.servicos.pedido import Pedido

class Mesa:
    """
    Representa uma mesa do restaurante com seus dados e coleções encapsulados.
    
    A classe gerencia os pedidos associados a ela, calcula o total da conta
    e fornece um resumo detalhado dos consumo por cliente.
    """
    def __init__(self, numero: int):
        """
        Inicializa a mesa com um número e uma lista vazia de pedidos.
        """
        self._numero = numero # Atributo protegido
        self._pedidos = []   # Atributo protegido

    @property
    def numero(self) -> int:
        """Propriedade para acesso seguro (apenas leitura) ao número da mesa."""
        return self._numero

    @property
    def pedidos(self) -> list:
        """Propriedade que retorna uma cópia da lista de pedidos para proteger a original."""
        return self._pedidos.copy()

    def registrar_pedido(self, cliente: Cliente, itens: list):
        """
        Método público para registrar um novo pedido na mesa. 
        Cria um objeto Pedido e o associa a esta mesa.
        """
        try:
            pedido = Pedido(cliente)
            for item in itens:
                pedido.adicionar_item(item)
            self._pedidos.append(pedido)
            print(f"Cliente {cliente.nome} fez um pedido na mesa {self._numero}:")
            pedido.exibir_itens()
        except (TypeError, ValueError) as e:
            # Tratamento de exceção para casos como itens inválidos
            print(f"Erro ao registrar pedido: {e}")

    def calcular_total(self) -> float:
        """
        Calcula o valor total da conta da mesa somando o preço de todos os itens
        em todos os pedidos. 
        """
        total = 0.0
        # Itera sobre a lista interna de pedidos
        for pedido in self._pedidos:
            # Acessa a propriedade 'itens' do pedido, que já retorna uma lista
            for item in pedido.itens:
                # Usa o método polimórfico 'calcular_preco' de cada item
                total += item.calcular_preco()
        return total

    def imprimir_conta_detalhada(self):
        """
        Método polimórfico que imprime um resumo detalhado da conta,
        agrupando os itens por cliente e mostrando o total a pagar.
        """
        print(f"\nResumo da mesa {self._numero}:")
        if not self._pedidos:
            print("Nenhum pedido registrado nesta mesa.")
            return

        detalhes_por_cliente = {}
        # Agrupa todos os itens por nome do cliente
        for pedido in self._pedidos:
            nome_cliente = pedido.cliente.nome
            if nome_cliente not in detalhes_por_cliente:
                detalhes_por_cliente[nome_cliente] = []

            for item in pedido.itens:
                preco = item.calcular_preco()
                # Formatação especial se o item for uma Bebida, para incluir o tamanho
                if isinstance(item, Bebida):
                     detalhes_por_cliente[nome_cliente].append(f"{item.nome} {item.tamanho} (R$ {preco:.2f})")
                else:
                     detalhes_por_cliente[nome_cliente].append(f"{item.nome} (R$ {preco:.2f})")

        # Formata a string de saída final
        resumo_str_list = []
        for cliente, itens_str in detalhes_por_cliente.items():
            resumo_str_list.append(f"- {cliente}: {', '.join(itens_str)}")
        
        print(' '.join(resumo_str_list))
        print(f"Total: R$ {self.calcular_total():.2f}")