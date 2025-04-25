import datetime

class cofre():
    def __init__(self):
        self.password = None
        self.attemp = 3
        self.closed = False
        self.blocked = False
        self.historic = []

    def abrir_cofre(self):
        if self.blocked:
            return print("Cofre bloqueado contate o fabricante com nota fiscal")
        if not self.password:
            return print("O cofre já está aberto!")
        for n in range(self.attemp):
            current_moment = datetime.datetime.now()
            tentativa = {"moment":current_moment, "sucess": False}
            senha =  input(f"Digite a senha ({n}º tentativa:) ")
            if (senha == self.password):
                tentativa["sucess"] = True
                self.historic.append(tentativa)
                self.exibir_historico()
                self.resetar_tentativas()
                self.closed = False
                print("Cofre Aberto")
                self.resetar_tentativas()
                break
            else:
                self.historic.append(tentativa)
                if n < 2: continue
                print("Cofre bloqueado contate o fabricante com nota fiscal")
                self.blocked =True   
             

    def fechar_cofre(self):
        if not self.password:
            return print("Você precisa primeiro definir uma senha para fechar o cofre!")
        self.closed = True
        print("Cofre fechado")
    
    def trocar_senha(self):
        if not self.password:
            print("Vamos definir sua primeira senha, certifique-se de nunca perder, pois após 3 erros apenas o fabricante com nota fiscal poderá abrir o cofre:")
            nova_senha = input("digite aqui a nova senha: ")
            self.validar_senha(nova_senha)
        else:
            print("Para trocar de senha primeiro digite a senha antiga")
            for n in range(self.attemp):
                senha =  input(f"{n}º tentativa: ")
                if (senha == self.password):
                    self.resetar_tentativas()
                    print("Senha validada")
                    break
                self.blocked =True
            nova_senha = input("Digite a nova senha: ")
            self.validar_senha(nova_senha)
            self.resetar_tentativas()

    def resetar_tentativas(self):
        self.attemp = 3  

    def exibir_historico(self):
        for idx,tentativa in enumerate(self.historic):
            print(f"{idx+1}° tentativa - momento: {tentativa["moment"]} - sucesso: {"sim" if tentativa["sucess"] else "não"}")
    
    def validar_senha(self, senha):
        tem_numero = any(caractere.isdigit() for caractere in senha)
        if not tem_numero: 
            return print("A senhe precisa ter ao menos um número")
        if len(senha)< 6: 
            return  print("A senhe precisa ter no mínimo 6 dígitos")
        self.password = senha
        print("senha alterada")
     
           


cofre1 = cofre()
cofre1.trocar_senha()