import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../model/contato.dart';

final String nomeTabela = 'contatos';
final String colunaId = 'id';
final String colunaNome = 'nome';
final String colunaEmail = 'email';
final String colunaLatitude = 'latitude';
final String colunaLongitude = 'longitude';

class ContatoHelper{
  static final ContatoHelper _instance = ContatoHelper.internal();
  factory ContatoHelper() => _instance;
  ContatoHelper.internal();

  Database? _db;

  Future<Database> get db async {
    if (_db == null){
      _db = await initDb();
    }
    return _db!;
  }

  Future<Database> initDb() async {
    final databasePath = await getDatabasesPath();
    final path = join(databasePath, 'banco.db');

    return await openDatabase(path, version:1, onCreate: _onCreate);
  }

  void _onCreate(Database db, int versaoRecente) async {
    String sql = 
      "CREATE TABLE $nomeTabela("
      "$colunaId INTEGER PRIMARY KEY AUTOINCREMENT, "
      "$colunaNome VARCHAR, " 
      "$colunaEmail VARCHAR,"
      "$colunaLatitude REAL,"
      "$colunaLongitude REAL)";
    await db.execute(sql);
  }

  Future<int> salvarContato(Contato contato) async {
    Database? database = await db;
    Map<String, dynamic> dadosParaSalvar = contato.toMap();

    int idContato = await database!.insert(nomeTabela, dadosParaSalvar);

    return idContato;
  }

  Future <List<Map<String,dynamic>>> buscarTodos() async {
    Database database = await db;
    return await database.query(nomeTabela);
  }

  Future <List<Contato>> buscarContatos() async {
    List<Map<String, dynamic>> listaMaps = await buscarTodos();

    List<Contato> listaContatos = [];

    for (Map<String, dynamic> m in listaMaps){
      listaContatos.add(Contato.fromMap(m));
    }

    return listaContatos;
  }

  Future<int?> getCount() async {
    Database database = await db;
    return Sqflite.firstIntValue(await database.rawQuery("SELECT COUNT(*) FROM $nomeTabela"));
  }

  Future close() async {
    Database? database = await db;
    database?.close();
  }

  Future<int> updateContato(Contato contato) async {
    Database database = await db;

    return await database.update(
      nomeTabela,
      contato.toMap(),
      where: "$colunaId =?",
      whereArgs: [contato.id]
    );
  }

  Future<int> deleteContato(int id) async {
    Database database = await db;
    return await database.delete(
      nomeTabela,
      where: "$colunaId = ?",
      whereArgs:  [id]
    );
  }
}
