class Usuario {
  int? id;
  String email;
  String senha;
  String perguntaSecreta;

  Usuario({this.id, required this.email, required this.senha, required this.perguntaSecreta});

  factory Usuario.fromMap(Map<String, dynamic> map){
    return Usuario(
      id: map['id'],
      email: map['email'], 
      senha: map['senha'], 
      perguntaSecreta: map['perguntaSecreta']
    );
  }

  Map<String, dynamic> toMap(){
    return {
      'id': id,
      'email': email,
      'senha': senha,
      'perguntaSecreta': perguntaSecreta
    };
  }
}