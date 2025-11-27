
from typing import Optional
from datetime import datetime
from decimal import Decimal


class PedidoProduto:
   
    
    def __init__(self, 
                 id_pedido: int = 0,
                 id_produto: int = 0,
                 quantidade: int = 0,
                 preco_unitario: Decimal = Decimal('0.00'),
                 created_at: Optional[datetime] = None):

        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario if isinstance(preco_unitario, Decimal) else Decimal(str(preco_unitario))
        self.created_at = created_at

    
    def to_dict(self) -> dict:
        return {
            'id_pedido': self.id_pedido,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade,
            'preco_unitario': float(self.preco_unitario),
            'created_at': self.created_at
        }
    
    def calcular_subtotal(self) -> Decimal:

        return self.preco_unitario * self.quantidade
