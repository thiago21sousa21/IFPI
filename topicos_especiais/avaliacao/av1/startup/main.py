from daos import UsuarioDao, TelefoneDao, PostDao, LikeDao
import os
from models import Usuario, Telefone, Post, Like
from datetime import datetime
from database.connection import DatabaseConnection

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

###################
### TESTE LIKES ###
###################

# CRIAR UM LIKE

#primeiro deletar todos os usuarios
with DatabaseConnection() as cnn:
    cnn.execute_query("DELETE FROM likes")
    cnn.execute_query("DELETE FROM posts")
    cnn.execute_query("DELETE FROM usuarios")

#precisa existir um usuario pra criar um post
print("criando primeiro um usuario")
usuario_exempo: Usuario = Usuario("thiago", "@mail", "2022-01-01")
print("Inserindo no banco")
usuario_exempo.id = UsuarioDao.inserir_usuario(usuario_exempo)
print(vars(usuario_exempo))

# precisa existir um post os likes do post
print("Criando o post exemplo ...")
post_exemplo:Post = Post(datetime.now(), "Bom dia!", usuario_exempo, midia="meu link 1")
print(vars(post_exemplo))
print("Inserindo no banco...")
post_exemplo.id = PostDao.inserir_post(post_exemplo)
print(vars(post_exemplo))

#agora se pode criar o like
print("Criando like...")
like_exemplo:Like = Like(post_exemplo, usuario_exempo)
print(vars(like_exemplo))
print("Inserindo o like exemplo no banco")
like_exemplo.id = LikeDao.inserir_like(like_exemplo)
print(vars(like_exemplo))

#agora listar todos os likes
print("Listando todos os likes")
print(LikeDao.listar_todos_os_likes())
print(f"Agora buscando like especifico, like com id: {like_exemplo.id}")
like_buscado:Like = LikeDao.buscar_like(like_exemplo)
print(like_buscado)

#Atualizar like
like_exemplo.data_hora = None
print(vars(like_exemplo))
print(f"atualizando o like exemplo que tinha data inserida por default para none")
LikeDao.atualizar_like(like_exemplo)
print(LikeDao.buscar_like(like_exemplo))


