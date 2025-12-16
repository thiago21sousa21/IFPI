import 'package:projeto_final/model/usuario.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

import 'database_helper.dart';

final String nomeTabelaUser = 'usuarios';
final String colunaUserId = 'id';
final String colunaUserEmail = 'email';
final String colunaUserSenha = 'senha';
final String colunaUserPergunta = 'perguntaSecreta';

class UsuarioHelper {
  static final UsuarioHelper _instance = UsuarioHelper.internal();
  factory UsuarioHelper()=> _instance;

  UsuarioHelper.internal();

  Database? _db;

  Future<Database> get db async{
    _db??= await initDb();
    return _db!;
  }

  Future<Database> initDb() async {
    final databasesPath = await getDatabasesPath();
    final path = join(databasesPath, 'banco.db');

    return await openDatabase(path, version: 1, onCreate: _onCreate);
  }

  void _onCreate(Database db, int versaoRecente) async {
    String sqlUser = 
    "CREATE TABLE $nomeTabelaUser("
    "$colunaUserId INTEGER PRIMARY KEY AUTOINCREMENT, "
    "$colunaUserEmail VARCHAR, "
    "$colunaUserSenha VARCHAR, "
    "$colunaUserPergunta VARCHAR)";

    await db.execute(sqlUser);

    String sqlContatos = 
          "CREATE TABLE contatos("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "nome VARCHAR, " 
          "email VARCHAR,"
          "latitude REAL,"
          "longitude REAL)";
        
    await db.execute(sqlContatos);
  }

  Future<int> cadastrarUsuario(Usuario usuario) async {
    Database database = await db;

    List<Map> existing = await database.query(
      nomeTabelaUser,
      where: "$colunaUserEmail = ?", whereArgs: [usuario.email]
    );

    if (existing.isNotEmpty){
      return -1;
    }

    return await database.insert(nomeTabelaUser, usuario.toMap());
  }

  Future<Usuario?> autenticar(String email, String senha) async {
    Database database = await db;
    List<Map> maps = await database.query(nomeTabelaUser,
    where:  "$colunaUserEmail = ? AND $colunaUserSenha = ?",
    whereArgs: [email, senha]);

    if(maps.isNotEmpty){
      return Usuario.fromMap(maps.first as Map<String, dynamic>);
    }

    return null;
  }

  Future<Usuario?> buscarPorEmailPergunta(String email, String pergunta) async {
    Database database = await db;
    List<Map> maps = await database.query(nomeTabelaUser,
    where: "$colunaUserEmail = ? AND $colunaUserPergunta = ?",
    whereArgs: [email, pergunta]);

    if (maps.isNotEmpty){
      return Usuario.fromMap(maps.first as Map<String, dynamic>);
    }

    return null;
  }

  Future<int> updateUsuario(Usuario usuario) async {
    Database database = await db;
    return await database.update(
      nomeTabelaUser, 
      usuario.toMap(),
      where: "$colunaUserId = ? ",
      whereArgs: [usuario.id]
    );
  }

  Future<int> deletarUsuario(int id) async {
    Database database = await db;
    return await database.delete(
      nomeTabelaUser,
      where: "$colunaUserId = ? ",
      whereArgs: [id]
    );
  }

}