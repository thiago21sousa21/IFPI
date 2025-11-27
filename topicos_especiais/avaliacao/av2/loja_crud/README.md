# Sistema CRUD - Loja

Sistema completo de CRUD (Create, Read, Update, Delete) para gerenciamento de uma loja, desenvolvido em Python com MySQL.

## 📋 Estrutura do Projeto

```
loja_crud/
├── conexao.py                 # Módulo de conexão com o banco de dados
├── create_database.sql        # Script SQL de criação do banco de dados
├── models/                    # Classes de entidades
│   ├── cliente.py
│   ├── produto.py
│   ├── pedido.py
│   └── pedido_produto.py
├── daos/                      # Data Access Objects (CRUD)
│   ├── cliente_dao.py
│   ├── produto_dao.py
│   ├── pedido_dao.py
│   └── pedido_produto_dao.py
├── testes/                    # Testes dos DAOs
│   ├── teste_cliente_dao.py
│   ├── teste_produto_dao.py
│   ├── teste_pedido_dao.py
│   └── teste_pedido_produto_dao.py
└── README.md                  # Este arquivo
```

## 🗄️ Modelo de Dados

O sistema possui 4 tabelas principais:

### CLIENTES
- `id_cliente` (INT, PK, AUTO_INCREMENT)
- `nome` (VARCHAR)
- `email` (VARCHAR, UNIQUE)
- `telefone` (VARCHAR)
- `created_at`, `updated_at` (TIMESTAMP)

### PRODUTOS
- `id_produto` (INT, PK, AUTO_INCREMENT)
- `nome` (VARCHAR)
- `preco` (DECIMAL)
- `estoque` (INT)
- `created_at`, `updated_at` (TIMESTAMP)

### PEDIDOS
- `id_pedido` (INT, PK, AUTO_INCREMENT)
- `id_cliente` (INT, FK)
- `data_pedido` (DATE)
- `total` (DECIMAL)
- `created_at`, `updated_at` (TIMESTAMP)

### PEDIDOS_PRODUTOS (Tabela Associativa)
- `id_pedido` (INT, PK, FK)
- `id_produto` (INT, PK, FK)
- `quantidade` (INT)
- `preco_unitario` (DECIMAL)
- `created_at` (TIMESTAMP)

## 🚀 Instalação

### 1. Instalar Dependências

```bash
pip install mysql-connector-python
```

### 2. Configurar o Banco de Dados

Execute o script SQL para criar o banco de dados e as tabelas:

```bash
mysql -u root -p < create_database.sql
```

Ou importe manualmente no MySQL Workbench ou phpMyAdmin.

### 3. Configurar a Conexão

Edite o arquivo `conexao.py` se necessário para ajustar as credenciais:

```python
conexao = Conexao(
    host='localhost',
    database='loja',
    user='root',
    password='sua_senha'
)
```

## 💻 Uso

### Exemplo Básico

```python
from conexao import Conexao
from daos.cliente_dao import ClienteDAO
from models.cliente import Cliente

# Criar conexão
conexao = Conexao()

# Criar DAO
cliente_dao = ClienteDAO(conexao)

# Criar novo cliente
novo_cliente = Cliente(
    nome="João Silva",
    email="joao@email.com",
    telefone="(86) 99999-1111"
)

id_cliente = cliente_dao.criar(novo_cliente)

# Buscar cliente
cliente = cliente_dao.buscar_por_id(id_cliente)
print(cliente)

# Atualizar cliente
cliente.telefone = "(86) 98888-2222"
cliente_dao.atualizar(cliente)

# Listar todos
clientes = cliente_dao.buscar_todos()
for c in clientes:
    print(c)

# Deletar cliente
cliente_dao.deletar(id_cliente)

# Fechar conexão
conexao.desconectar()
```

## 🧪 Executar Testes

### Testar Cliente DAO

```bash
cd testes
python teste_cliente_dao.py
```

### Testar Produto DAO

```bash
cd testes
python teste_produto_dao.py
```

### Testar Pedido DAO

```bash
cd testes
python teste_pedido_dao.py
```

### Testar Pedido-Produto DAO

```bash
cd testes
python teste_pedido_produto_dao.py
```

## 📚 Funcionalidades dos DAOs

### ClienteDAO
- `criar(cliente)` - Cria um novo cliente
- `buscar_por_id(id_cliente)` - Busca cliente por ID
- `buscar_todos()` - Lista todos os clientes
- `atualizar(cliente)` - Atualiza dados do cliente
- `deletar(id_cliente)` - Remove cliente
- `buscar_por_email(email)` - Busca cliente por email

### ProdutoDAO
- `criar(produto)` - Cria um novo produto
- `buscar_por_id(id_produto)` - Busca produto por ID
- `buscar_todos()` - Lista todos os produtos
- `atualizar(produto)` - Atualiza dados do produto
- `deletar(id_produto)` - Remove produto
- `buscar_por_preco_maior_que(preco)` - Busca produtos com preço maior que X
- `atualizar_estoque(id_produto, quantidade)` - Atualiza estoque

### PedidoDAO
- `criar(pedido)` - Cria um novo pedido
- `buscar_por_id(id_pedido)` - Busca pedido por ID
- `buscar_todos()` - Lista todos os pedidos
- `atualizar(pedido)` - Atualiza dados do pedido
- `deletar(id_pedido)` - Remove pedido
- `buscar_por_cliente(id_cliente)` - Busca pedidos de um cliente
- `calcular_total_pedido(id_pedido)` - Calcula total do pedido
- `atualizar_total(id_pedido)` - Atualiza total automaticamente

### PedidoProdutoDAO
- `criar(pedido_produto)` - Adiciona produto ao pedido
- `buscar_por_pedido(id_pedido)` - Lista produtos de um pedido
- `buscar_por_produto(id_produto)` - Lista pedidos com um produto
- `buscar_por_id(id_pedido, id_produto)` - Busca item específico
- `atualizar(pedido_produto)` - Atualiza quantidade/preço
- `deletar(id_pedido, id_produto)` - Remove produto do pedido
- `deletar_por_pedido(id_pedido)` - Remove todos os produtos do pedido
- `buscar_produtos_detalhados_por_pedido(id_pedido)` - Busca com JOIN

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **MySQL 8.0+**
- **mysql-connector-python** - Driver MySQL para Python

## 📝 Observações

- O sistema utiliza **Decimal** para valores monetários (preços e totais)
- As chaves estrangeiras possuem **ON DELETE CASCADE**
- Timestamps são gerenciados automaticamente pelo MySQL
- Os testes incluem dados de exemplo para demonstração

## 👨‍💻 Autor

Sistema desenvolvido para gerenciamento de loja com arquitetura em camadas (Models, DAOs, Conexão).

---

**Versão:** 1.0  
**Data:** Novembro 2025
