import re

class veiculo:
  def __init__(self, chassi, marca, modelo, ano, cor, placa=None, proprietario=None, quilometragem=None, valor = None):
    self.chassi = chassi
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.placa = placa
    self.proprietario = proprietario
    self.quilometragem = quilometragem
    self.valor = valor 

  def validar_placa(self, placa):
    padrao = r'^[A-Z]{3}-[A-Z][A-Z0-9][0-9]{2}$'
    return re.match(padrao, placa.upper().strip()) is not None
  

def validar_placa(placa):
    padrao = r'^[A-Z]{3}-?[0-9]{4}$|^[A-Z]-?\d[A-Z]\d{2}$'
    return re.match(padrao, placa.upper().strip()) is not 
    
def calcular_depreciacao(self):
  # o Calcula a depreciação do veículo com base no ano de fabricação e no valor de
  # mercado.
  ano_atual = date.today().year
  depreciacao = 5/100
  ano_carro = self.ano
  valor_depreciado = self.valor * (1 - depreciacao)**((ano_atual-ano_carro) +1)
  valor_minimo = self.valor * (10/100)
  if (ano_carro > ano_atual) :
    print(f"Tu é viajante do tempo? Ajeita o ano desse carro aí, estamos em {ano_atual}")
  else:
    if valor_depreciado < valor_minimo:
      print(valor_minimo)
      return valor_minimo
    else:
      print(valor_depreciado)
      return valor_depreciado

v = validar_placa('nia8020')
print(v)