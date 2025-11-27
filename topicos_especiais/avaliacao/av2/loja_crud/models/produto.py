
from typing import Optional
from datetime import datetime
from decimal import Decimal


class Produto:
    
    def __init__(self, 
                 id_produto: Optional[int] = None,
                 nome: str = '',
                 preco: Decimal = Decimal('0.00'),
                 estoque: int = 0,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):

        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco if isinstance(preco, Decimal) else Decimal(str(preco))
        self.estoque = estoque
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self) -> str:
        return f"Produto(id={self.id_produto}, nome='{self.nome}', preco={self.preco}, estoque={self.estoque})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_dict(self) -> dict:
        return {
            'id_produto': self.id_produto,
            'nome': self.nome,
            'preco': float(self.preco),
            'estoque': self.estoque,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
