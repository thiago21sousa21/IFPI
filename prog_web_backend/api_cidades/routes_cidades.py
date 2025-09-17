from schemas import Cidade, NovaCidade
from fastapi import APIRouter, status, HTTPException

router = APIRouter()

cidades : list[Cidade] = [
    Cidade(nome="Teresina", uf="PI", id=1),
    Cidade(nome="Campo Maior", uf="PI", id=2),
]


@router.post("", status_code=status.HTTP_201_CREATED)
def criar_cidade(cidade:Cidade):
    cidade.id = len(cidades) + 1
    cidades.append(cidade)
    return f'criei a cidade: {cidade}'

@router.get("", status_code=status.HTTP_200_OK)
def buscar_cidade():
    return  cidades

@router.put("/{id}", status_code=status.HTTP_200_OK)
def atualizar_cidade(id:int, cidade_atualizada: Cidade):
    cidade_procurada:Cidade = None
    for cid in cidades:
        if cid.id == id:
            cidade_procurada = cid
            break
    if not cidade_procurada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa cidade não esta na lista")
    
    if cidade_atualizada.nome: cidade_procurada.nome = cidade_atualizada.nome
    if cidade_atualizada.uf: cidade_procurada.uf = cidade_atualizada.uf

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_cidade(id:int):
    for idx ,cid in enumerate(cidades):
        if cid.id == id:
            cidades.pop(idx)
            return f'Deu certo, deletei: {cid}'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa cidade não esta na lista")


@router.get("/{id}", status_code=status.HTTP_200_OK)
def buscar_cidades(id:int):
    for cid in cidades:
        if cid.id == id:
            return f'Deu certo, retornando a cidade: {cid}'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa cidade não esta na lista")
