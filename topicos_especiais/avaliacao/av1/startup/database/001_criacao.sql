-- 2) Uma startup de tecnologia está desenvolvendo uma rede social acadêmica para conectar
-- estudantes, professores e pesquisadores. O sistema precisa armazenar diversas informações
-- para possibilitar interações entre os usuários.
-- ● Cada usuário possui um identificador único, nome completo, e-mail, data de nascimento e
-- pode ter múltiplos números de telefone e idade.
-- ● Um usuário pode criar vários posts, cada um com data/hora de publicação, conteúdo
-- textual e opcionalmente uma mídia (imagem ou vídeo).
-- ● Usuários podem curtir e comentar posts de outros usuários. Cada comentário possui
-- data/hora e texto.
-- ● Os usuários podem se conectar entre si através de relações de amizade. Essa relação
-- deve registrar a data em que a amizade foi estabelecida.
CREATE DATABASE IF NOT EXISTS startup;

USE startup;

CREATE TABLE IF NOT EXISTS  usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome_completo VARCHAR(255) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	data_nascimento DATE  NOT NULL,
	idade INT
);

CREATE TABLE  IF NOT EXISTS telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	numero VARCHAR(20) NOT NULL,
	usuario_id INT  NOT NULL
);
SELECT * FROM telefones WHERE id = 1;
CREATE TABLE IF NOT EXISTS  posts(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	conteudo TEXT NOT NULL,
	midia TEXT,
	usuario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS  likes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	post_id INT NOT NULL,
	usuario_id INT NOT NULL,
	data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS  comentarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	conteudo TEXT NOT NULL,
	post_id INT  NOT NULL,
	usuario_id INT  NOT NULL
);

CREATE TABLE IF NOT EXISTS  amizades(
	usuario_id_1 INT NOT NULL,
	usuario_id_2 INT NOT NULL,
	data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE telefones
ADD CONSTRAINT fk_telefones_usuarios
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id);

ALTER TABLE posts
ADD CONSTRAINT fk_posts_usuarios
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id);

ALTER TABLE likes
ADD CONSTRAINT fk_likes_posts
FOREIGN KEY (post_id)
REFERENCES posts(id),
ADD CONSTRAINT fk_likes_usuarios
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id);

ALTER TABLE comentarios
ADD CONSTRAINT fk_comentarios_posts
FOREIGN KEY (post_id)
REFERENCES posts(id),
ADD CONSTRAINT fk_comentarios_usuarios
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id);

ALTER TABLE amizades
ADD CONSTRAINT fk_amizades_usuario1
FOREIGN KEY (usuario_id_1)
REFERENCES usuarios(id),
ADD CONSTRAINT fk_amizades_usuario2
FOREIGN KEY (usuario_id_2)
REFERENCES usuarios(id),
ADD CONSTRAINT pk_usuario1_usuario2
PRIMARY KEY (usuario_id_1, usuario_id_2);

