class cofre():
    def __init__(self):
        self.password = None
        self.attemp = 3
        self.closed = False
        self.blocked = False

    def abrir_cofre(self):
        if self.blocked:
            return print("Cofre bloqueado contate o fabricante com nota fiscal")
        if not self.password:
            return print("O cofre já está aberto!")
        for n in range(self.attemp):
            senha =  input(f"Digite a senha ({n}º tentativa:) ")
            if (senha == self.password):
                self.resetar_tentativas()
                self.closed = False
                print("Cofre Aberto")
                self.resetar_tentativas()
                break
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
            self.password = nova_senha
            print("senha alterada")
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
            self.password = nova_senha
            self.resetar_tentativas()

    def resetar_tentativas(self):
        self.attemp = 3  

cofre1 = cofre()
cofre1.abrir_cofre()
cofre1.fechar_cofre()
cofre1.trocar_senha()
cofre1.fechar_cofre()
cofre1.abrir_cofre()
cofre.trocar_senha()

