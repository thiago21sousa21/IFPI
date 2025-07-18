# Importando classes dos sub-pacotes modelos e servicos
from sistema.modelos.prato import Prato
from sistema.modelos.bebida import Bebida
from sistema.modelos.cliente import Cliente
from sistema.servicos.restaurante import Restaurante
from sistema.servicos.mesa import Mesa


if __name__ == "__main__":
    print("=====================================================")
    print("🚀 INICIANDO SIMULAÇÃO DO SISTEMA DO RESTAURANTE 🚀")
    print("=====================================================\n")

    # --- 1. Configurando o Restaurante e Cardápio ---
    print("--- 1. Configurando o Restaurante e Cardápio ---")
    restaurante = Restaurante("Restaurante Exemplo")
    print(f"Bem-vindo ao '{restaurante.nome}'!\n")

    print("Adicionando itens ao cardápio...")
    # Criando e adicionando pratos e bebidas ao cardápio
    restaurante.adicionar_item_cardapio("Hambúrguer", Prato("Hambúrguer", 25.00, 15))
    restaurante.adicionar_item_cardapio("Salada Caesar", Prato("Salada Caesar", 22.00, 10))
    restaurante.adicionar_item_cardapio("Filé Mignon", Prato("Filé Mignon", 55.00, 30))
    restaurante.adicionar_item_cardapio("Refrigerante", Bebida("Refrigerante", 4.00, 'G')) # Preço base 4.00, final 8.00
    restaurante.adicionar_item_cardapio("Suco Natural", Bebida("Suco Natural", 8.00, 'M')) # Preço base 8.00, final 10.00
    restaurante.adicionar_item_cardapio("Vinho Tinto", Bebida("Vinho Tinto", 36.00, 'G')) # Preço base 36.00, final 40.00
    print("Cardápio configurado com sucesso!\n")

    # --- 2. Adicionando Mesas ao Restaurante ---
    print("--- 2. Adicionando Mesas ao Restaurante ---")
    mesa5 = Mesa(5)
    mesa7 = Mesa(7)
    restaurante.adicionar_mesa(mesa5)
    restaurante.adicionar_mesa(mesa7)
    print("") # Linha em branco para espaçamento

    # --- 3. Registrando Pedidos dos Clientes ---
    print("--- 3. Registrando Pedidos dos Clientes ---")
    # Criando os clientes
    cliente_joao = Cliente("João")
    cliente_maria = Cliente("Maria")
    cliente_pedro = Cliente("Pedro")

    # Pedidos para a Mesa 5
    try:
        print("\nCliente João está fazendo um pedido na Mesa 5...")
        itens_joao = [
            restaurante.get_item_cardapio("Hambúrguer"),
            restaurante.get_item_cardapio("Refrigerante")
        ]
        mesa5.registrar_pedido(cliente_joao, itens_joao)

        print("\nCliente Maria está fazendo um pedido na Mesa 5...")
        itens_maria = [
            restaurante.get_item_cardapio("Salada Caesar"),
            restaurante.get_item_cardapio("Suco Natural")
        ]
        mesa5.registrar_pedido(cliente_maria, itens_maria)

    except (ValueError, TypeError) as e:
        print(f"‼️ Ocorreu um erro inesperado: {e}")

    # Pedido para a Mesa 7
    try:
        print("\nCliente Pedro está fazendo um pedido na Mesa 7...")
        itens_pedro = [
            restaurante.get_item_cardapio("Filé Mignon"),
            restaurante.get_item_cardapio("Vinho Tinto")
        ]
        mesa7.registrar_pedido(cliente_pedro, itens_pedro)
    except (ValueError, TypeError) as e:
        print(f"‼️ Ocorreu um erro inesperado: {e}")

    # --- 4. Exemplo de Tratamento de Erro ---
    print("\n--- 4. Exemplo de Tratamento de Erro ---")
    print("Tentando pedir um item que não existe no cardápio (Batata Frita)...")
    try:
        item_inexistente = restaurante.get_item_cardapio("Batata Frita")
        mesa5.registrar_pedido(cliente_joao, [item_inexistente])
    except ValueError as e:
        print(f"SUCESSO NA CAPTURA: O sistema tratou o erro corretamente -> {e}\n")

    # --- 5. Finalizando Contas e Exibindo Resumos ---
    print("--- 5. Finalizando Contas e Exibindo Resumos ---")
    mesa5.imprimir_conta_detalhada()
    mesa7.imprimir_conta_detalhada()

    # --- 6. Listando Mesas Ocupadas ---
    print("\n--- 6. Listando Mesas Ocupadas no Final do Atendimento ---")
    restaurante.listar_mesas_ocupadas()

    print("\n=====================================================")
    print("✅ SIMULAÇÃO CONCLUÍDA ✅")
    print("=====================================================")