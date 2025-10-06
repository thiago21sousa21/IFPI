from daos import UsuarioDao, TelefoneDao, PostDao
import os
from models import Usuario, Telefone, Post
from datetime import datetime

(lambda: os.system("clear"))()

u1: Usuario = Usuario("thiago", "@mail", "2022-01-01")

# print(UsuarioDao().listar_todos_os_usuarios())

# u1.id = 2
# u1.nome_completo = "aguim"
# print(vars(u1))

#UsuarioDao().delete_usuario(u1)
#UsuarioDao().inserir_usuario(u1)
#UsuarioDao.atualizar_usuario(u1)


# print(UsuarioDao().listar_todos_os_usuarios())


######################
### TESTE TELEFONE ###
######################

# t1: Telefone = Telefone("4567", u1)
# t1.id = 1

#print(TelefoneDao.listar_todos_telefones())
#print(TelefoneDao.inserir_telefone(t1))
# print(TelefoneDao.listar_todos_telefones())
#print('####')
#print(TelefoneDao.buscar_telefone(t1))
#TelefoneDao.delete_telefone(t1)
# print(TelefoneDao.listar_todos_telefones())
# t1.id = 2
# t1.numero = "3333333333"
# TelefoneDao.atualizar_telefone(t1)
# print(TelefoneDao.listar_todos_telefones())


###################
### TESTE POSTS ###
###################

# post1:Post = Post(datetime.now(), "Bom dia!", u1, midia="meu link 1")
# print(PostDao.listar_todos_posts())
# u1.id = 2
# post1.id = 2
# PostDao.inserir_post(post1)

#print(PostDao.buscar_post(post1))
#PostDao.delete_post(post1)

#ATUALIZAR  POST
# post1.conteudo = "Boa tarde"
# post1.midia = "Meu link 2"
# PostDao.atualizar_post(post1)
# print(PostDao.listar_todos_posts())
#PostDao.atualizar_post()

print()

