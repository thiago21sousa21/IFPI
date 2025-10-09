###################
### TESTE LIKES ###
###################

# CRIAR UM LIKE

#primeiro deletar todos os usuarios


#precisa existir um usuario pra criar um post
# print("criando primeiro um usuario")
# usuario_exempo: Usuario = Usuario("thiago", "@mail", "2021-01-01")
# print("Inserindo no banco")
# usuario_exempo.id = UsuarioDao.inserir_usuario(usuario_exempo)
# print(vars(usuario_exempo))

# # precisa existir um post os likes do post
# print("Criando o post exemplo ...")
# post_exemplo:Post = Post(datetime.now(), "Bom dia!", usuario_exempo, midia="meu link 0")
# print(vars(post_exemplo))
# print("Inserindo no banco...")
# post_exemplo.id = PostDao.inserir_post(post_exemplo)
# print(vars(post_exemplo))

# #agora se pode criar o like
# print("Criando like...")
# like_exemplo:Like = Like(post_exemplo, usuario_exempo)
# print(vars(like_exemplo))
# print("Inserindo o like exemplo no banco")
# like_exemplo.id = LikeDao.inserir_like(like_exemplo)
# print(vars(like_exemplo))

# #agora listar todos os likes
# print("Listando todos os likes")
# print(LikeDao.listar_todos_os_likes())
# print(f"Agora buscando like especifico, like com id: {like_exemplo.id}")
# like_buscado:Like = LikeDao.buscar_like(like_exemplo)
# print(like_buscado)

# #Atualizar like
# like_exemplo.data_hora = None
# print(vars(like_exemplo))
# print(f"atualizando o like exemplo que tinha data inserida por default para none")
# LikeDao.atualizar_like(like_exemplo)
# print(LikeDao.buscar_like(like_exemplo))