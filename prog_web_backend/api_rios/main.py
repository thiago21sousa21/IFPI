from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelos  ou Schema de API
class Rio(BaseModel):
  id: int
  nome: str
  extensao: float
  permanente: bool


class NovoRio(BaseModel):
  nome: str
  extensao: float | None = 0.0

rios: list[Rio] = [
  Rio(id=1, nome='Parnaíba', extensao=1400, permanente=True),
  Rio(id=2, nome='São Francisco', extensao=2830, permanente=True),
  Rio(id=3, nome='Jaguaribe', extensao=633, permanente=False)
  ]



@app.get('/rios')
def list_rios(ordem:str | None = None,
              tipo:str | None = None):
  if tipo == 'permanente':
    rios_filtrados = []
    for rio in rios:
      if rio.permanente:
        rios_filtrados.append(rio)
    return rios_filtrados

  if ordem:
    rios_ordenados = sorted(rios, key=lambda x:x[ordem])
    return rios_ordenados

  return rios

# Path Param ou Parametro de Rota/Path
@app.get('/rios/{id}', status_code=status.HTTP_200_OK)
def detail_rios(id:int):
  if id % 2 == 0:
    return f'Detalhes do Rio de ID = {id}'
  else:
    # return Response(content='Rio não localizado', 
    #                 status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                  detail='Rio não localizado')


@app.post('/rios', status_code=status.HTTP_201_CREATED)
def create_rio(dados: NovoRio):
  # como criar efetivamente um Rio no BD
  return dados


@app.put('/rios/{id}')
def update_rio(id:int):
  # Fake.. ok?!
  return f'Rio({id}) atualizado com sucesso.'


@app.delete('/rios/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rio(id:int):
  return