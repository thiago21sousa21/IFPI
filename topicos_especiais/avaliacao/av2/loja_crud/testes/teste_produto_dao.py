
from decimal import Decimal
from conexao import Conexao
from daos.produto_dao import ProdutoDAO
from models.produto import Produto


def teste_criar_produto():
    print("\n=== TESTE: Criar Produto ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    novo_produto = Produto(
        nome="SSD 500GB",
        preco=Decimal('350.00'),
        estoque=40
    )
    
    id_produto = produto_dao.criar(novo_produto)
    
    if id_produto:
        print(f"Produto criado com ID: {id_produto}")
    else:
        print(" Falha ao criar produto")
    
    conexao.desconectar()


def teste_buscar_produto_por_id():
    print("\n=== TESTE: Buscar Produto por ID ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    produto = produto_dao.buscar_por_id(1)
    
    if produto:
        print(f" Produto encontrado: {produto}")
    else:
        print("Produto não encontrado")
    
    conexao.desconectar()


def teste_buscar_todos_produtos():
    print("\n=== TESTE: Buscar Todos os Produtos ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    produtos = produto_dao.buscar_todos()
    
    print(f"Total de produtos encontrados: {len(produtos)}")
    for produto in produtos:
        print(f"  - {produto}")
    
    conexao.desconectar()


def teste_atualizar_produto():
    print("\n=== TESTE: Atualizar Produto ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    produto = produto_dao.buscar_por_id(2)
    
    if produto:
        produto.preco = Decimal('9.50')
        produto.estoque = 45
        sucesso = produto_dao.atualizar(produto)
        
        if sucesso:
            print(f"Produto atualizado: {produto}")
        else:
            print(" Falha ao atualizar produto")
    else:
        print(" Produto não encontrado para atualização")
    
    conexao.desconectar()


def teste_buscar_produtos_por_preco():
    print("\n=== TESTE: Buscar Produtos com Preço > 10.0 ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    produtos = produto_dao.buscar_por_preco_maior_que(Decimal('10.0'))
    
    print(f" Total de produtos encontrados: {len(produtos)}")
    for produto in produtos:
        print(f"  - {produto}")
    
    conexao.desconectar()


def teste_atualizar_estoque():
    """Testa a atualização de estoque de um produto"""
    print("\n=== TESTE: Atualizar Estoque ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    sucesso = produto_dao.atualizar_estoque(1, 15)
    
    if sucesso:
        print(" Estoque atualizado com sucesso")
    else:
        print(" Falha ao atualizar estoque")
    
    conexao.desconectar()


def teste_deletar_produto():
    print("\n=== TESTE: Deletar Produto ===")
    
    conexao = Conexao()
    produto_dao = ProdutoDAO(conexao)
    
    novo_produto = Produto(
        nome="Produto Temporário",
        preco=Decimal('1.00'),
        estoque=1
    )
    
    id_produto = produto_dao.criar(novo_produto)
    
    if id_produto:
        sucesso = produto_dao.deletar(id_produto)
        
        if sucesso:
            print(f" Produto ID {id_produto} deletado com sucesso")
        else:
            print(" Falha ao deletar produto")
    
    conexao.desconectar()


if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DO PRODUTO DAO")
    print("=" * 50)
    
    teste_criar_produto()
    teste_buscar_produto_por_id()
    teste_buscar_todos_produtos()
    teste_atualizar_produto()
    teste_buscar_produtos_por_preco()
    teste_atualizar_estoque()
    teste_deletar_produto()
    
    print("\n" + "=" * 50)
    print("TESTES CONCLUÍDOS")
    print("=" * 50)
