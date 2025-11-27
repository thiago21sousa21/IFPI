
from decimal import Decimal
from datetime import date
from conexao import Conexao
from daos.pedido_dao import PedidoDAO
from models.pedido import Pedido


def teste_criar_pedido():
    print("\n=== TESTE: Criar Pedido ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    novo_pedido = Pedido(
        id_cliente=1,
        data_pedido=date.today(),
        total=Decimal('500.00')
    )
    
    id_pedido = pedido_dao.criar(novo_pedido)
    
    if id_pedido:
        print(f"Pedido criado com ID: {id_pedido}")
    else:
        print("Falha ao criar pedido")
    
    conexao.desconectar()


def teste_buscar_pedido_por_id():
    print("\n=== TESTE: Buscar Pedido por ID ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    pedido = pedido_dao.buscar_por_id(1)
    
    if pedido:
        print(f"Pedido encontrado: {pedido}")
    else:
        print("Pedido não encontrado")
    
    conexao.desconectar()


def teste_buscar_todos_pedidos():
    print("\n=== TESTE: Buscar Todos os Pedidos ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    pedidos = pedido_dao.buscar_todos()
    
    print(f"Total de pedidos encontrados: {len(pedidos)}")
    for pedido in pedidos:
        print(f"  - {pedido}")
    
    conexao.desconectar()


def teste_atualizar_pedido():
    print("\n=== TESTE: Atualizar Pedido ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    pedido = pedido_dao.buscar_por_id(1)
    
    if pedido:
        pedido.total = Decimal('3600.00')
        sucesso = pedido_dao.atualizar(pedido)
        
        if sucesso:
            print(f"Pedido atualizado: {pedido}")
        else:
            print("Falha ao atualizar pedido")
    else:
        print("Pedido não encontrado para atualização")
    
    conexao.desconectar()


def teste_buscar_pedidos_por_cliente():
    print("\n=== TESTE: Buscar Pedidos do Cliente ID 2 ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    pedidos = pedido_dao.buscar_por_cliente(2)
    
    print(f"Total de pedidos encontrados: {len(pedidos)}")
    for pedido in pedidos:
        print(f"  - {pedido}")
    
    conexao.desconectar()


def teste_calcular_total_pedido():
    print("\n=== TESTE: Calcular Total do Pedido ID 2 ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    total = pedido_dao.calcular_total_pedido(2)
    
    if total is not None:
        print(f"Total calculado: R$ {total}")
    else:
        print("Erro ao calcular total")
    
    conexao.desconectar()


def teste_atualizar_total_pedido():
    print("\n=== TESTE: Atualizar Total do Pedido ID 1 ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    sucesso = pedido_dao.atualizar_total(1)
    
    if sucesso:
        pedido = pedido_dao.buscar_por_id(1)
        print(f"Total atualizado: {pedido}")
    else:
        print("Erro ao atualizar total")
    
    conexao.desconectar()


def teste_deletar_pedido():
    print("\n=== TESTE: Deletar Pedido ===")
    
    conexao = Conexao()
    pedido_dao = PedidoDAO(conexao)
    
    novo_pedido = Pedido(
        id_cliente=1,
        data_pedido=date.today(),
        total=Decimal('0.00')
    )
    
    id_pedido = pedido_dao.criar(novo_pedido)
    
    if id_pedido:
        sucesso = pedido_dao.deletar(id_pedido)
        
        if sucesso:
            print(f"Pedido ID {id_pedido} deletado com sucesso")
        else:
            print("Falha ao deletar pedido")
    
    conexao.desconectar()


if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DO PEDIDO DAO")
    print("=" * 50)
    
    teste_criar_pedido()
    teste_buscar_pedido_por_id()
    teste_buscar_todos_pedidos()
    teste_atualizar_pedido()
    teste_buscar_pedidos_por_cliente()
    teste_calcular_total_pedido()
    teste_atualizar_total_pedido()
    teste_deletar_pedido()
    
    print("\n" + "=" * 50)
    print("TESTES CONCLUÍDOS")
    print("=" * 50)
