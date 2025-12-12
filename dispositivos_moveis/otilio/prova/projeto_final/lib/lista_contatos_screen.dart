import 'package:flutter/material.dart';
import 'package:projeto_final/cadastro_contato_screen.dart';
import 'package:projeto_final/controller/database_helper.dart';
import 'package:projeto_final/model/contato.dart';

class ListaContatosScreen  extends StatefulWidget{
  const ListaContatosScreen({super.key});
  @override
  State<ListaContatosScreen> createState() => _ListaContatosScreenState();
}

class _ListaContatosScreenState extends State<ListaContatosScreen> {
  final ContatoHelper helper = ContatoHelper();

  late Future<List<Contato>> _contatosFuture;

  @override
  void initState(){
    super.initState();
    _contatosFuture = helper.buscarContatos();
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: const Text("Lista de Contatos"),
        actions: [
          IconButton( 
            icon: Icon(Icons.refresh),
            onPressed: (){
              setState(() {
                _contatosFuture = helper.buscarContatos();
              });
            },
          )
        ]
      ),
      body: FutureBuilder<List<Contato>>(
        future: _contatosFuture, 
        builder: (context, snapshot){
          if(snapshot.connectionState == ConnectionState.waiting){
            return const Center(child: CircularProgressIndicator());
          } else if(snapshot.hasError){
            return Center(child: Text("Erro ao carregar dados: ${snapshot.error}"),);
          } else if(!snapshot.hasData || snapshot.data!.isEmpty){
            return const Center(child: Text("Nenhum contato cadastrado"));
          } else {
            List<Contato> contatos = snapshot.data!;
            return ListView.builder(
              itemCount: contatos.length,
              itemBuilder: (context, index){
                Contato contato = contatos[index];
                return ListTile(
                  leading: CircleAvatar(
                    child: Text(contato.nome[0]),
                  ),
                  title:  Text(contato.email),
                  subtitle: Text(contato.nome),
                  trailing: Text("ID ${contato.id}"),
                  onTap: () async {
                    await Navigator.push(
                      context, 
                      MaterialPageRoute(
                        builder: (context) => CadastroContatoScreen(contatoParaEdicao: contato,)
                      )
                    );
                    setState((){
                      _contatosFuture = helper.buscarContatos();
                    });
                  },
                );
              },
            );
          }
        }
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async{
          await Navigator.push(
            context,
            MaterialPageRoute(builder: (context)=> CadastroContatoScreen())
          );
          setState(() {
            _contatosFuture = helper.buscarContatos();
          });
        },
        child: Icon(Icons.add),
      ),
    );
  }
}