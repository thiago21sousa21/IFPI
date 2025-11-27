"""
Exemplo completo de uso do sistema CRUD da Loja
"""
from decimal import Decimal
from datetime import date

from conexao import Conexao
from models.cliente import Cliente
from models.produto import Produto
from models.pedido import Pedido
from models.pedido_produto import PedidoProduto
from daos.cliente_dao import ClienteDAO
from daos.produto_dao import ProdutoDAO
from daos.pedido_dao import PedidoDAO
from daos.pedido_produto_dao import PedidoProdutoDAO


def exemplo_completo():
    """Demonstração completa do sistema"""
    
    print("=" * 60)
    print("SISTEMA DE GERENCIAMENTO DE LOJA - EXEMPLO DE USO")
    print("=" * 60)
    
    # Criar conexão
    conexao = Conexao(
        host='localhost',
        database='loja',
        user='root',
        password='123456'  # Ajuste conforme sua configuração
    )
    
    # Criar DAOs
    cliente_dao = ClienteDAO(conexao)
    produto_dao = ProdutoDAO(conexao)
    pedido_dao = PedidoDAO(conexao)
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    # ========== CLIENTES ==========
    print("\n" + "=" * 60)
    print("GERENCIAMENTO DE CLIENTES")
    print("=" * 60)
    
    # Listar todos os clientes
    print("\n--- Listando todos os clientes ---")
    clientes = cliente_dao.buscar_todos()
    for cliente in clientes:
        print(f"  {cliente}")
    
    # Buscar cliente específico
    print("\n--- Buscando cliente ID 1 ---")
    cliente = cliente_dao.buscar_por_id(1)
    if cliente:
        print(f"  {cliente}")
    
    # Buscar por email
    print("\n--- Buscando cliente por email ---")
    cliente = cliente_dao.buscar_por_email("maria.santos@email.com")
    if cliente:
        print(f"  {cliente}")
    
    # ========== PRODUTOS ==========
    print("\n" + "=" * 60)
    print("GERENCIAMENTO DE PRODUTOS")
    print("=" * 60)
    
    # Listar todos os produtos
    print("\n--- Listando todos os produtos ---")
    produtos = produto_dao.buscar_todos()
    for produto in produtos:
        print(f"  {produto}")
    
    # Buscar produtos com preço > 10.0
    print("\n--- Produtos com preço superior a R$ 10,00 ---")
    produtos_caros = produto_dao.buscar_por_preco_maior_que(Decimal('10.0'))
    for produto in produtos_caros:
        print(f"  {produto}")
    
    # ========== PEDIDOS ==========
    print("\n" + "=" * 60)
    print("GERENCIAMENTO DE PEDIDOS")
    print("=" * 60)
    
    # Listar todos os pedidos
    print("\n--- Listando todos os pedidos ---")
    pedidos = pedido_dao.buscar_todos()
    for pedido in pedidos:
        print(f"  {pedido}")
    
    # Buscar pedidos de um cliente específico
    print("\n--- Pedidos do cliente ID 2 ---")
    pedidos_cliente = pedido_dao.buscar_por_cliente(2)
    for pedido in pedidos_cliente:
        print(f"  {pedido}")
    
    # ========== PRODUTOS DO PEDIDO ==========
    print("\n" + "=" * 60)
    print("PRODUTOS DOS PEDIDOS")
    print("=" * 60)
    
    # Listar produtos do pedido 1 (detalhado)
    print("\n--- Produtos do Pedido ID 1 (com detalhes) ---")
    produtos_pedido = pedido_produto_dao.buscar_produtos_detalhados_por_pedido(1)
    total_pedido = Decimal('0.00')
    
    for item in produtos_pedido:
        print(f"  Produto: {item['nome']}")
        print(f"    Quantidade: {item['quantidade']}")
        print(f"    Preço Unit.: R$ {item['preco_unitario']:.2f}")
        print(f"    Subtotal: R$ {item['subtotal']:.2f}")
        total_pedido += Decimal(str(item['subtotal']))
    
    print(f"\n  TOTAL DO PEDIDO: R$ {total_pedido:.2f}")
    
    # ========== CRIAR NOVO PEDIDO COMPLETO ==========
    print("\n" + "=" * 60)
    print("CRIANDO NOVO PEDIDO COMPLETO")
    print("=" * 60)
    
    # Criar novo pedido
    novo_pedido = Pedido(
        id_cliente=1,
        data_pedido=date.today(),
        total=Decimal('0.00')
    )
    
    id_novo_pedido = pedido_dao.criar(novo_pedido)
    
    if id_novo_pedido:
        print(f"\n✓ Pedido criado com ID: {id_novo_pedido}")
        
        # Adicionar produtos ao pedido
        print("\n--- Adicionando produtos ao pedido ---")
        
        # Produto 1: Notebook Dell
        item1 = PedidoProduto(
            id_pedido=id_novo_pedido,
            id_produto=1,
            quantidade=1,
            preco_unitario=Decimal('3500.00')
        )
        pedido_produto_dao.criar(item1)
        
        # Produto 2: Mouse Logitech
        item2 = PedidoProduto(
            id_pedido=id_novo_pedido,
            id_produto=2,
            quantidade=2,
            preco_unitario=Decimal('8.50')
        )
        pedido_produto_dao.criar(item2)
        
        # Atualizar total do pedido
        print("\n--- Atualizando total do pedido ---")
        pedido_dao.atualizar_total(id_novo_pedido)
        
        # Buscar pedido atualizado
        pedido_atualizado = pedido_dao.buscar_por_id(id_novo_pedido)
        print(f"\n✓ Pedido finalizado: {pedido_atualizado}")
        
        # Listar produtos do novo pedido
        print("\n--- Produtos do novo pedido ---")
        produtos_novo = pedido_produto_dao.buscar_produtos_detalhados_por_pedido(id_novo_pedido)
        for item in produtos_novo:
            print(f"  - {item['nome']}: {item['quantidade']} x R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}")
    
    # ========== CONSULTAS ESPECIAIS ==========
    print("\n" + "=" * 60)
    print("CONSULTAS ESPECIAIS (Baseadas no PDF)")
    print("=" * 60)
    
    # 1. Produtos com preço > 10.0
    print("\n1. Produtos com preço superior a R$ 10,00:")
    produtos = produto_dao.buscar_por_preco_maior_que(Decimal('10.0'))
    for p in produtos:
        print(f"   - {p.nome}: R$ {p.preco:.2f}")
    
    # 2. Pedidos do cliente ID 2
    print("\n2. Pedidos do cliente ID 2:")
    pedidos = pedido_dao.buscar_por_cliente(2)
    for p in pedidos:
        print(f"   - Pedido {p.id_pedido}: {p.data_pedido} - Total: R$ {p.total:.2f}")
    
    # 3. Quantidade de pedidos do cliente ID 3
    print("\n3. Quantidade de pedidos do cliente ID 3:")
    pedidos = pedido_dao.buscar_por_cliente(3)
    print(f"   - Total: {len(pedidos)} pedido(s)")
    
    # 4. Produtos do pedido ID 1
    print("\n4. Produtos do pedido ID 1:")
    produtos = pedido_produto_dao.buscar_produtos_detalhados_por_pedido(1)
    for p in produtos:
        print(f"   - {p['nome']}: {p['quantidade']} x R$ {p['preco_unitario']:.2f}")
    
    # 5. Pedidos do cliente 'Beltrano'
    print("\n5. Pedidos do cliente 'Beltrano':")
    cliente = cliente_dao.buscar_por_email("beltrano@email.com")
    if cliente:
        pedidos = pedido_dao.buscar_por_cliente(cliente.id_cliente)
        print(f"   - Total: {len(pedidos)} pedido(s)")
    
    # 6. Total do pedido ID 2
    print("\n6. Total do pedido ID 2:")
    total = pedido_dao.calcular_total_pedido(2)
    if total:
        print(f"   - Total: R$ {total:.2f}")
    
    # 7. Total de todos os pedidos do cliente ID 1
    print("\n7. Total de todos os pedidos do cliente ID 1:")
    pedidos = pedido_dao.buscar_por_cliente(1)
    total_geral = sum(p.total for p in pedidos)
    print(f"   - Total: R$ {total_geral:.2f}")
    
    # Fechar conexão
    print("\n" + "=" * 60)
    conexao.desconectar()
    print("=" * 60)


if __name__ == "__main__":
    exemplo_completo()
