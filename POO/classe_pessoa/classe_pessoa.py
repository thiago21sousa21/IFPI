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

    def verificar_instancia(self, classe):
        if not isinstance(classe, Pessoa):
            raise TypeError(f"Objeto não é uma instância de Pessoa")

    def casar(self,conjuge):
        self.verificar_instancia(conjuge)
        pode_casar = self.__estado == "vivo" and self.__est_civil != "casado" and conjuge.__estado == "vivo" and conjuge.__est_civil != "casado"
        if pode_casar:
            self.__conjuge = conjuge
            conjuge.__conjuge = self
            self.__est_civil = "casado"
            conjuge.__est_civil = "casado"
        else:
            raise ValueError("Não é possível casar: condições não atendidas.")



    def morrer(self):
        if self.__estado == "vivo":
            self.__estado = "morto"
            if self.__conjuge:
                self.__conjuge.__conjuge = None
                self.__conjuge.__est_civil = "viúvo"
            self.__conjuge = None
        else:
            raise ValueError("Pessoa já está morta.")

    def divorciar(self):
        if not self.__conjuge:
            raise ValueError("Não é possível divorciar: não há cônjuge.")
        if self.__estado != "vivo":
            raise ValueError("Não é possível divorciar: pessoa não está viva.")
        if self.__est_civil != "casado":
            raise ValueError("Não é possível divorciar: pessoa não está casada.")

        self.__conjuge.__est_civil = "divorciado"
        self.__est_civil = "divorciado"
        self.__conjuge.__conjuge = None
        self.__conjuge = None


    def adoção(self,mãe): #condição: Pessoa ser órfã e mãe tem que ser de maior
        self.verificar_instancia(mãe)
        if self.__mãe is not None:
            raise ValueError("Pessoa já tem mãe biológica.")
        if self.__pai is not None:
            raise ValueError("Pessoa já tem pai biológico.")
        if self.__estado != "vivo":
            raise ValueError("Não é possível adotar: pessoa não está viva.")
        if not isinstance(mãe, Pessoa):
            raise TypeError("Mãe adotiva deve ser uma instância de Pessoa.")
        if mãe.__estado != "vivo":
            raise ValueError("Mãe adotiva deve estar viva.")
        if mãe.__idade < 18:
            raise ValueError("Mãe adotiva deve ser maior de idade (18 anos ou mais).")
 
        self.__mãe_adotiva = mãe
        mãe.__filho_adotivo = self

    def __str__(self):
        return f"""
        Nome: {self.__nome}
        Idade: {self.__idade}
        Peso: {self.__peso}
        Altura: {self.__altura}
        Sexo: {self.__sexo}
        Estado: {self.__estado}
        Estado Civil: {self.__est_civil}
        Mãe: {self.__mãe.nome if self.__mãe else "Não informado"}
        Pai: {self.__pai.nome if self.__pai else "Não informado"}
        Mãe Adotiva: {self.__mãe_adotiva.nome if self.__mãe_adotiva else "Não informado"}
        Pai Adotivo: {self.__pai_adotivo.nome if self.__pai_adotivo else "Não informado"}
        Cônjuge: {self.__conjuge.nome if self.__conjuge else "Não informado"}
        """


pessoa = Pessoa("Thiago", 20, 70, 1.75, "Masculino")
print(pessoa)
pessoa2 = Pessoa("Maria", 22, 60, 1.65, "Feminino")
print(pessoa2)
pessoa.casar(pessoa2)
print(pessoa)
print(pessoa2)
pessoa.morrer()
print(pessoa)
print(pessoa2)

# agora vou criar testes usando pytest para verificar se as funções estão funcionando corretamente

# Para rodar os testes, você pode usar o comando: