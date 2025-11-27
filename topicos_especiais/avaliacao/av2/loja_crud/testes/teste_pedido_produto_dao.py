

from decimal import Decimal
from conexao import Conexao
from daos.pedido_produto_dao import PedidoProdutoDAO
from models.pedido_produto import PedidoProduto


def teste_criar_pedido_produto():
    print("\n=== TESTE: Adicionar Produto ao Pedido ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    novo_item = PedidoProduto(
        id_pedido=1,
        id_produto=4,
        quantidade=1,
        preco_unitario=Decimal('800.00')
    )
    
    sucesso = pedido_produto_dao.criar(novo_item)
    
    if sucesso:
        print(" Produto adicionado ao pedido com sucesso")
    else:
        print(" Falha ao adicionar produto ao pedido")
    
    conexao.desconectar()


def teste_buscar_produtos_por_pedido():
    """Testa a busca de produtos de um pedido"""
    print("\n=== TESTE: Buscar Produtos do Pedido ID 1 ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    produtos = pedido_produto_dao.buscar_por_pedido(1)
    
    print(f" Total de produtos no pedido: {len(produtos)}")
    for item in produtos:
        print(f"  - {item}")
        print(f"    Subtotal: R$ {item.calcular_subtotal()}")
    
    conexao.desconectar()


def teste_buscar_pedidos_por_produto():
    """Testa a busca de pedidos que contêm um produto"""
    print("\n=== TESTE: Buscar Pedidos com Produto ID 3 ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    pedidos = pedido_produto_dao.buscar_por_produto(3)
    
    print(f" Total de pedidos com este produto: {len(pedidos)}")
    for item in pedidos:
        print(f"  - {item}")
    
    conexao.desconectar()


def teste_buscar_por_id():
    print("\n=== TESTE: Buscar Pedido-Produto Específico ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    item = pedido_produto_dao.buscar_por_id(1, 1)
    
    if item:
        print(f" Item encontrado: {item}")
    else:
        print("Item não encontrado")
    
    conexao.desconectar()


def teste_atualizar_pedido_produto():
    print("\n=== TESTE: Atualizar Item do Pedido ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    item = pedido_produto_dao.buscar_por_id(1, 2)
    
    if item:
        item.quantidade = 3
        item.preco_unitario = Decimal('8.00')
        sucesso = pedido_produto_dao.atualizar(item)
        
        if sucesso:
            print(f"Item atualizado: {item}")
        else:
            print("Falha ao atualizar item")
    else:
        print("Item não encontrado para atualização")
    
    conexao.desconectar()


def teste_buscar_produtos_detalhados():
    """Testa a busca de produtos detalhados de um pedido"""
    print("\n=== TESTE: Buscar Produtos Detalhados do Pedido ID 1 ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    produtos = pedido_produto_dao.buscar_produtos_detalhados_por_pedido(1)
    
    print(f" Total de produtos: {len(produtos)}")
    for produto in produtos:
        print(f"  - Produto: {produto['nome']}")
        print(f"    Quantidade: {produto['quantidade']}")
        print(f"    Preço Unit.: R$ {produto['preco_unitario']}")
        print(f"    Subtotal: R$ {produto['subtotal']}")
    
    conexao.desconectar()


def teste_deletar_pedido_produto():
    """Testa a remoção de um produto de um pedido"""
    print("\n=== TESTE: Remover Produto do Pedido ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    # Primeiro adiciona um item para depois deletar
    novo_item = PedidoProduto(
        id_pedido=2,
        id_produto=2,
        quantidade=1,
        preco_unitario=Decimal('8.50')
    )
    
    pedido_produto_dao.criar(novo_item)
    
    sucesso = pedido_produto_dao.deletar(2, 2)
    
    if sucesso:
        print(" Produto removido do pedido com sucesso")
    else:
        print(" Falha ao remover produto do pedido")
    
    conexao.desconectar()


def teste_deletar_por_pedido():
    """Testa a remoção de todos os produtos de um pedido"""
    print("\n=== TESTE: Remover Todos os Produtos do Pedido ID 3 ===")
    
    conexao = Conexao()
    pedido_produto_dao = PedidoProdutoDAO(conexao)
    
    sucesso = pedido_produto_dao.deletar_por_pedido(3)
    
    if sucesso:
        print(" Todos os produtos removidos do pedido")
    else:
        print(" Falha ao remover produtos do pedido")
    
    conexao.desconectar()


if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DO PEDIDO-PRODUTO DAO")
    print("=" * 50)
    
    teste_criar_pedido_produto()
    teste_buscar_produtos_por_pedido()
    teste_buscar_pedidos_por_produto()
    teste_buscar_por_id()
    teste_atualizar_pedido_produto()
    teste_buscar_produtos_detalhados()
    teste_deletar_pedido_produto()
    teste_deletar_por_pedido()
    
    print("\n" + "=" * 50)
    print("TESTES CONCLUÍDOS")
    print("=" * 50)
