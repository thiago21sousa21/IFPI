

from conexao import Conexao
from daos.cliente_dao import ClienteDAO
from models.cliente import Cliente


def teste_criar_cliente():
    print("\n=== TESTE: Criar Cliente ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    novo_cliente = Cliente(
        nome="Pedro Oliveira",
        email="pedro.oliveira@email.com",
        telefone="(86) 98888-5555"
    )
    
    id_cliente = cliente_dao.criar(novo_cliente)
    
    if id_cliente:
        print(f" Cliente criado com ID: {id_cliente}")
    else:
        print("Falha ao criar cliente")
    
    conexao.desconectar()


def teste_buscar_cliente_por_id():
    print("\n=== TESTE: Buscar Cliente por ID ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    cliente = cliente_dao.buscar_por_id(1)
    
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente não encontrado")
    
    conexao.desconectar()


def teste_buscar_todos_clientes():
    print("\n=== TESTE: Buscar Todos os Clientes ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    clientes = cliente_dao.buscar_todos()
    
    print(f" Total de clientes encontrados: {len(clientes)}")
    for cliente in clientes:
        print(f"  - {cliente}")
    
    conexao.desconectar()


def teste_atualizar_cliente():
    print("\n=== TESTE: Atualizar Cliente ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    cliente = cliente_dao.buscar_por_id(1)
    
    if cliente:
        cliente.telefone = "(86) 99999-0000"
        sucesso = cliente_dao.atualizar(cliente)
        
        if sucesso:
            print(f"Cliente atualizado: {cliente}")
        else:
            print("Falha ao atualizar cliente")
    else:
        print("Cliente não encontrado para atualização")
    
    conexao.desconectar()


def teste_buscar_cliente_por_email():
    print("\n=== TESTE: Buscar Cliente por Email ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    cliente = cliente_dao.buscar_por_email("joao.silva@email.com")
    
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente não encontrado")
    
    conexao.desconectar()


def teste_deletar_cliente():
    print("\n=== TESTE: Deletar Cliente ===")
    
    conexao = Conexao()
    cliente_dao = ClienteDAO(conexao)
    
    # Primeiro cria um cliente para deletar
    novo_cliente = Cliente(
        nome="Cliente Temporário",
        email="temp@email.com",
        telefone="(00) 00000-0000"
    )
    
    id_cliente = cliente_dao.criar(novo_cliente)
    
    if id_cliente:
        sucesso = cliente_dao.deletar(id_cliente)
        
        if sucesso:
            print(f"Cliente ID {id_cliente} deletado com sucesso")
        else:
            print("Falha ao deletar cliente")
    
    conexao.desconectar()


if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DO CLIENTE DAO")
    print("=" * 50)
    
    teste_criar_cliente()
    teste_buscar_cliente_por_id()
    teste_buscar_todos_clientes()
    teste_atualizar_cliente()
    teste_buscar_cliente_por_email()
    teste_deletar_cliente()
    
    print("\n" + "=" * 50)
    print("TESTES CONCLUÍDOS")
    print("=" * 50)
