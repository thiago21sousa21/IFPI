import os
from utils.limpar_banco import limpar_banco
from tests.usuario_test import Testar_usuario 
from tests.posts_tests import Testar_posts
from tests.comentarios_tests import Testar_comentarios
from tests.telefone_teste import Testar_telefones


(lambda: os.system("clear"))()
limpar_banco()

Testar_comentarios().testar_tudo()









