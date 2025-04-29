
from datetime import time

class ArCondicionado:
  VELOCIDADE_VENTILADOR = ["baixa", "media", "alta"]
  MODO_OPERACAO = ["resfriar","automatico", "ventilar"]

  def __init__(self, modelo="split", marca = "consul", potencia = 9000 ):
    self.modelo = modelo
    self.marca = marca
    self.potencia = potencia
    self.estado = False
    self.temperatura_atual = 24
    self.modo_atual = "resfriar"
    self.velocidade_atual = "media"
    self.timer = None

  def __str__(self):
    return f"""Modelo: {self.modelo}
Marca: {self.marca}
Potencia: {self.potencia}
Estado: {"Ligado" if self.estado else "Desligado"}
Temperatura atual: {self.temperatura_atual}
Modo atual: {self.modo_atual}
Velocidade atual: {self.velocidade_atual}"""

  def ligar(self):
    if not self.estado:
      self.estado = True

  def desligar(self):
    if self.estado:
      self.estado = False

  def toggle(self):
    if self.estado:
      self.desligar()
    else:
      self.ligar()

  def alterar_temperatura(self, nova_temperatura):
    if self.isPowerOff(): return
    if not (17 <= nova_temperatura <= 26):
      print("A temperatura precisa estar entre 17 e 26 °C")
      return
    self.temperatura_atual = nova_temperatura

  def alterar_modo(self, novo_modo):
    if self.isPowerOff(): return
    if novo_modo not in self.MODO_OPERACAO:
      print("Modo inválido")
      return
    self.modo_atual = novo_modo

  def isPowerOff(self):
    if not self.estado:
      print('O arcondicionado está desligado!')
      return True
    return False

  def isAutomaticMode(self):
    if self.modo_atual == "automatico":
      print("O ventilador está no modo autoḿatico, a velocidade não pode ser alterada")
      return True
    return False

  def alterar_velocidade_ventilador(self, nova_velocidade):
    if self.isPowerOff(): return
    if self.isAutomaticMode(): return
    if nova_velocidade not in self.VELOCIDADE_VENTILADOR:
      print("Velocidade inválida")
      return
    self.velocidade_atual = nova_velocidade

  def resetar_configuracoes(self):
    self.ligar()
    self.alterar_temperatura(24)
    self.alterar_velocidade_ventilador("media")
    self.alterar_modo("resfriar")

  def desligar_timer(self):
    self.timer= None

  def programar_timer(self, horario):
    try:
      self.timer = time.fromisoformat(horario)
      print(f"Timer ajustado para desligar às {self.timer}")
    except ValueError:
      print("Formato de horário inválido. Use hh:mm")
