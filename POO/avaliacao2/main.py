# Importando classes dos sub-pacotes modelos e servicos
from sistema.modelos.prato import Prato
from sistema.modelos.bebida import Bebida
from sistema.modelos.cliente import Cliente
from sistema.servicos.restaurante import Restaurante
from sistema.servicos.mesa import Mesa


if __name__ == "__main__":
    restaurante_show = Restaurante("Restaurante Show")
    mesa1 = Mesa(1)
    
    cliente_joao = Cliente("João")
    prato_picanha = Prato("Picanha na Brasa", 80.00, 25)
    
    