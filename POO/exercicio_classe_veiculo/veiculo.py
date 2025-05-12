import re
from datetime import date

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

def validar_placa(placa):
    padrao = r'^[A-Z]{3}-?[0-9]{4}$|^[A-Z]{3}-?\d[A-Z]\d{2}$'
    return re.match(padrao, placa.upper().strip()) is not None
    
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
        return valor_minimo
      else:
        return valor_depreciado


  def atualizar_quilometragem(self, nova_quilometragem):
    if nova_quilometragem > self.quilometragem:
      self.quilometragem = nova_quilometragem
    else:
      return 'a nova quilometragem precisa ser maior que a quilometragem atual'   

  def atualizar_proprietario(self, novo_proprietario):
    self.proprietario = novo_proprietario
    return f'novo proprietário: {novo_proprietario}'
  
  def vender(self, valor_venda, novo_proprietario ):
    """* Recebe o valor de venda e o nome do novo proprietário.
    * Calcula o valor depreciado do veículo e compara com o valor de venda.
    * Atualiza o nome do proprietário com o novo proprietário.
    * Retorna se o veículo foi vendido abaixo ou acima do valor de mercado."""
    valor_depreciado = self.calcular_depreciacao()
    self.atualizar_proprietario(novo_proprietario)
    return "vendido acima do mercado" if valor_venda > valor_depreciado else "vendido abaixo do mercado"



v = veiculo(1, 1, 1, 2024, 1, valor=100)
v.atualizar_proprietario("thiago de sousa santos")
v.vender(100, "thiago")