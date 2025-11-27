
from typing import Optional
from datetime import datetime


class Cliente:
    
    def __init__(self, 
                 id_cliente: Optional[int] = None,
                 nome: str = '',
                 email: str = '',
                 telefone: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.created_at = created_at
        self.updated_at = updated_at
    

    def to_dict(self) -> dict:
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
