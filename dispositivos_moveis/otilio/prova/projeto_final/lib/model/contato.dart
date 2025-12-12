class Contato {
  int? id;
  String nome;
  String email;
  double? latitude;
  double? longitude;

  Contato({this.id, required this.nome,required this.email, this.latitude, this.longitude});

  factory Contato.fromMap(Map<String, dynamic> map){
    return Contato(
      id: map['id'],
      nome: map['nome'],
      email: map['email'],
      latitude: map['latitude'],
      longitude: map['longitude']
    );
  }

  Map<String, dynamic> toMap(){
    return {
      'id': id,
      'nome': nome,
      'email': email,
      'latitude': latitude,
      'longitude': longitude
    };
  }
}