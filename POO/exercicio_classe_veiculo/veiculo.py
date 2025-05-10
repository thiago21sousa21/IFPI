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
    return re.match(padrao, placa.upper().strip()) is not None

v = validar_placa('nia8020')
print(v)