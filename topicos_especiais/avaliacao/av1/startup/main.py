import os
from utils.limpar_banco import limpar_banco
from tests.usuario_test import Testar_usuario 
from tests.posts_tests import Testar_posts


(lambda: os.system("clear"))()
limpar_banco()

# teste_de_usuario = Testar_usuario()
#teste_de_usuario.testar_tudo()
teste_de_post = Testar_posts()
teste_de_post.testar_tudo()








