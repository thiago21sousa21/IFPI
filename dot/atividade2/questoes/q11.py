# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo 
# usuário. 
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições. 
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente. 
# ==== =MENU======== 
# 1)Cadastar nome 
# 2)Pesquisar nome 
# 3)Listar todos os nome 
# 0) Sair do programa
import os

opcoes = list(range(4))
nomes = []

pedir_um_nome = lambda : input("Digite um nome: ")

def cadastrar_um_nome():
    nomes.append(pedir_um_nome())

limpar_terminal = lambda:os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    print("""# ======MENU======== 
# 1)Cadastar nome 
# 2)Pesquisar nome 
# 3)Listar todos os nome 
# 0) Sair do programa""")
    return ""
    
def escolher_opocao():
    opc = input("Selecione a opção desejada: ")
    while True:
        try:
            opc = int(opc)
            if opc in opcoes:
                return opc
            
            limpar_terminal()
            print(f"opção inválida: {opc} não está no menu!")
            opc = input(f"{exibir_menu()}\nTente novamente: ")
        except:
            limpar_terminal()
            print(f"Você precisa digitar um número! {opc} não é numero!")
            opc = input(f"{exibir_menu()}\nTente novamente, faça sua escolha: ")

def pesquisar_nome(num):
    try:
        num = int(num)
        print("pesquisando...")
        if num not in range(len(nomes)):
            print(f"{num} não está na lista")
            return
        print(f"O numero {num} é o nome {nomes[num]}")
    except:
        print(f"voce precisa digitar um número!")

def lista_todos_os_nomes():
    for idx, nome in enumerate(nomes):
        print(f"nome {idx} - {nome}") 

def decidir_o_que_fazer(opc):
    if opc == 1:
        limpar_terminal()
        print("Você escolheu adicionar um novo nome")
        cadastrar_um_nome()
        print("cadastrado com sucesso!")
        press_any_2_continue()
    if opc ==2:
        limpar_terminal()
        print("Você escolheu pesquisar por um nome")
        num = input("Digite o numero do nome a ser pesquisado: ")
        pesquisar_nome(num)
        press_any_2_continue()
    if opc == 3:
        limpar_terminal()
        print("Listando todos os nomes..")
        if len(nomes) == 0:
            print("Não há nomes para serem  listados")
            press_any_2_continue()
        lista_todos_os_nomes()
        press_any_2_continue()
    if opc == 0:
        limpar_terminal()
        print("Você decidiu sair")
        return False
    return True

press_any_2_continue = lambda: input("pressione alguma tecla para continuar")

def rodar_app():
    manter = True
    while manter:
        limpar_terminal()
        exibir_menu()
        opc = escolher_opocao()
        manter =decidir_o_que_fazer(opc)


if __name__ == "__main__":
    rodar_app()