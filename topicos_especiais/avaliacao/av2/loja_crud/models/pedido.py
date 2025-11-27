
from typing import Optional
from datetime import datetime, date
from decimal import Decimal


class Pedido:
    
    def __init__(self, 
                 id_pedido: Optional[int] = None,
                 id_cliente: int = 0,
                 data_pedido: Optional[date] = None,
                 total: Decimal = Decimal('0.00'),
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):

        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.data_pedido = data_pedido if data_pedido else date.today()
        self.total = total if isinstance(total, Decimal) else Decimal(str(total))
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self) -> str:
        return f"Pedido(id={self.id_pedido}, cliente_id={self.id_cliente}, data={self.data_pedido}, total={self.total})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_dict(self) -> dict:
        return {
            'id_pedido': self.id_pedido,
            'id_cliente': self.id_cliente,
            'data_pedido': self.data_pedido,
            'total': float(self.total),
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
