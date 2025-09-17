from pydantic import BaseModel

class CidadeBase(BaseModel):
    nome: str
    uf: str

class NovaCidade(CidadeBase):
    pass

class Cidade(CidadeBase):
    id:int = None