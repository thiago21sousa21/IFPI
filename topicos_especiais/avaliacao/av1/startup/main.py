import os
from utils import limpar_terminal, limpar_banco
from tests import Testar_amizade, Testar_comentarios, Testar_likes, Testar_posts, Testar_telefones, Testar_usuario

def limpar_geral():
    limpar_banco()
    limpar_terminal()

limpar_geral()
Testar_usuario().testar_tudo()

limpar_geral()
Testar_telefones().testar_tudo()

limpar_geral()
Testar_posts().testar_tudo()

limpar_geral()
Testar_comentarios().testar_tudo()

limpar_geral()
Testar_likes().testar_tudo()

limpar_geral()
Testar_amizade().testar_tudo()











