# Continuar o código para a classe Pessoa definida no link abaixo...
# - Criar os decoradores necessários
# - Implementar os métodos sugeridos
# - Implementar os objetos sugeridos e testar todas as situações dos métodos implementados

class Pessoa:
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",mãe=None):
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mãe = mãe
    self.__pai = None
    self.__mãe_adotiva = None
    self.__pai_adotivo = None
    self.__conjuge = None


  @property
  def nome(self):
    return self.__nome
  @property
  def conjuge(self):
    return self.__conjuge
  @property
  def est_civil(self):
    return self.__est_civil  
  @property
  def estado(self):
    return self.__estado  
  @property
  def mãe(self):
    return self.__mãe  
  @property
  def pai(self):
    return self.__pai  
  @property
  def mãe_adotiva(self):
    return self.__mãe_adotiva  
  @property
  def pai_adotivo(self):
    return self.__pai_adotivo
  @property
  def idade(self):
    return self.__idade
  @property
  def peso(self):
    return self.__peso
  @property
  def altura(self):
    return self.__altura
  @property
  def sexo(self):
    return self.__sexo

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  def casar(self,conjuge):
    if not isinstance(conjuge, Pessoa):
      raise TypeError("O conjuge deve ser uma instância da classe Pessoa.")
    if self.__est_civil == "casado" or conjuge.est_civil == "casado":
      raise ValueError("Ambas as pessoas devem ser solteiras para casar.")
    if self.__conjuge is not None or conjuge.conjuge is not None:
      raise ValueError("Uma das pessoas já está casada.")
    self.__conjuge = conjuge
    conjuge.__conjuge = self
    self.__est_civil = "casado"
    conjuge.__est_civil = "casado"

  def morrer(self):
    if self.__estado == "morto":
      raise ValueError("A pessoa já está morta.")
    self.__estado = "morto"
    if self.__conjuge is not None:
      self.__conjuge.__conjuge = None
      self.__conjuge.__est_civil = "viúvo" if self.__conjuge.est_civil == "casado" else self.__conjuge.est_civil
      self.__conjuge = None
    self.__est_civil = "morto"

  def divorciar(self):
    if self.__est_civil != "casado":
      raise ValueError("A pessoa não está casada.")
    if self.__conjuge is None:
      raise ValueError("Não há cônjuge para divorciar.")
    self.__conjuge.__conjuge = None
    self.__conjuge.__est_civil = "solteiro"
    self.__conjuge = None
    self.__est_civil = "solteiro"


  def adoção(self,mãe): #condição: Pessoa ser órfã e mãe tem que ser de maior
    if self.__mãe is not None and self.__pai is not None:
      raise ValueError("A pessoa não é órfã.")
    if mãe.idade < 18:
      raise ValueError("A mãe adotiva deve ser maior de idade.")
    self.__mãe_adotiva = mãe
    mãe.__filho_adotivo = self
    self.__pai_adotivo = None
    self.__estado = "adotado"

  def __str__(self):
    return f"""
    Nome: {self.__nome}
    Idade: {self.__idade}
    Peso: {self.__peso}
    Altura: {self.__altura}
    Sexo: {self.__sexo}
    Estado: {self.__estado}
    Estado Civil: {self.__est_civil}
    Mãe: {self.__mãe.nome if self.__mãe else 'Não informado'}
    Pai: {self.__pai.nome if self.__pai else 'Não informado'}
    Mãe Adotiva: {self.__mãe_adotiva.nome if self.__mãe_adotiva else 'Não informado'}
    Pai Adotivo: {self.__pai_adotivo.nome if self.__pai_adotivo else 'Não informado'}
    Conjuge: {self.__conjuge.nome if self.__conjuge else 'Não informado'}
    """


####### execução ########

maria = Pessoa("Maria", 30, 65, 1.7, 'F', mãe=Pessoa("Francisca",65,60,1.6,'F')) # maria -> solteira
print(maria)
# joão -> solteiro
joao = Pessoa("João", 32, 70, 1.8, 'M', mãe=Pessoa("Ana", 60, 55, 1.65, 'F')) # joão -> solteiro
print(joao)
# maria.casar(joao) # joão e maria -> casado
maria.casar(joao) # maria e joão -> casados
print(maria)
print(joao)
# ana = Pessoa(...)
ana = Pessoa("Ana", 28, 50, 1.65, 'F', mãe=Pessoa("Clara", 55, 50, 1.6, 'F')) # ana -> solteira
print(ana)
# joao.casar(ana) # não é possivel pois  já é casado com maria
#joao.casar(ana) # não é possivel pois já é casado com maria
# maria.morrer() # maria para para o estado de morto.
maria.morrer() # maria para o estado de morto
print(maria)
print(joao)
# joao.casar(ana) # joao e ana -> casado
joao.casar(ana) # joão e ana -> casados
print(joao)
print(ana)


#simular processo de adoção
# joão -> solteiro
joao = Pessoa("João", 32, 70, 1.8, 'M', mãe=Pessoa("Ana", 60, 55, 1.65, 'F')) # joão -> solteiro
# maria -> solteira
maria = Pessoa("Maria", 30, 65, 1.7, 'F') # maria -> solteira
print(maria)
# joão adota maria
joao.adoção(maria) # joão adota maria
print(joao)
print(maria)