import os
from utils import limpar_terminal, limpar_banco
from tests.usuario_test import Testar_usuario 
from tests.posts_tests import Testar_posts
from tests.comentarios_tests import Testar_comentarios
from tests.telefone_teste import Testar_telefones
from tests.like_tests import Testar_likes
from tests.amizade_tests import Testar_amizade




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











