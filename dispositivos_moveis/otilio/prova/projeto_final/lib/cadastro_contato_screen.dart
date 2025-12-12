import 'package:flutter/material.dart';
import 'package:projeto_final/controller/database_helper.dart';
import 'package:projeto_final/model/contato.dart';

class CadastroContatoScreen extends StatefulWidget{
  final Contato? contatoParaEdicao;

  const CadastroContatoScreen({super.key, this.contatoParaEdicao});

  @override
  State<CadastroContatoScreen> createState() => _CadastroContatoScreen();
}

class _CadastroContatoScreen extends State<CadastroContatoScreen> {
  TextEditingController _nomeController = TextEditingController();
  TextEditingController _emailController = TextEditingController();
  TextEditingController _latController = TextEditingController();
  TextEditingController _longController = TextEditingController();



  ContatoHelper helper = ContatoHelper();

  @override
  void initState(){
    super.initState();
    if(widget.contatoParaEdicao != null){
      _nomeController.text = widget.contatoParaEdicao!.nome;
      _emailController.text = widget.contatoParaEdicao!.email;
      _latController.text = widget.contatoParaEdicao!.latitude?.toString() ?? '';
      _longController.text = widget.contatoParaEdicao!.longitude?.toString() ?? '';
    }
  }

  @override
  void dispose(){
    _nomeController.dispose();
    _emailController.dispose();
    super.dispose();
  }

  void _salvarContato() async {
    String nome = _nomeController.text;
    String email = _emailController.text;

    double? latitude = double.tryParse(_latController.text);
    double? longitude = double.tryParse(_longController.text);

    if (nome.isNotEmpty && email.isNotEmpty){
      Contato contato = Contato(
        id: widget.contatoParaEdicao?.id,
        nome: nome, 
        email: email,
        latitude: latitude,
        longitude: longitude
      );

      int resultadoId;
      String acao;

      if (contato.id == null){
        resultadoId = await helper.salvarContato(contato);
        acao = "salvo";
      } else {
        resultadoId = await helper.updateContato(contato);
        acao = "atualizado";
      }

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Contato $acao com sucesso Id: ${contato.id ?? resultadoId}"))
      );

      if (contato.id == null){
        _nomeController.clear();
        _emailController.clear();
      }

      
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Por favor, preencha todos os campos"))
      );
    }
  }

  void _excluirContato() async {
    if (widget.contatoParaEdicao!.id != null){
      int id = widget.contatoParaEdicao!.id!;
      await helper.deleteContato(id);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Contato ID $id exluído com sucesso!")),
      );
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.contatoParaEdicao == null ? "novo contato" : "editar contato"),
        actions: [
          if (widget.contatoParaEdicao != null )
            IconButton(
              icon: Icon(Icons.delete),
              onPressed: _excluirContato,  
            )
        ],
      ),
      body: Column(
        children: <Widget>[
          TextField(
            controller: _nomeController,
            decoration: InputDecoration(
              labelText: "Nome",
              hintText: "Digite o nome do contato"
            ),
          ),
          SizedBox(height: 20),
          
          TextField(
            controller: _emailController,
            keyboardType: TextInputType.emailAddress,
            decoration: InputDecoration(
              labelText: "Email",
              hintText: "Digite o email do contatol"
            ),
          ),

          SizedBox(height: 20,),
          TextField(
            controller: _latController,
            keyboardType: TextInputType.number,
            decoration: InputDecoration(
              labelText: "Latitude (opcional)",
              hintText: "-5.088544",
              border: OutlineInputBorder()
            ),
          ),

          SizedBox(height: 20,),

          TextField(
            controller: _longController,
            keyboardType: TextInputType.number,
            decoration: InputDecoration(
              labelText: "Longitude (opcional)",
              hintText: "-42.811238",
              border: OutlineInputBorder()
            ),
          ),

          SizedBox(height: 40),

          ElevatedButton(
            onPressed: _salvarContato, 
            child: Text("Salvar Contato"),
            style: ElevatedButton.styleFrom(
              padding: EdgeInsets.symmetric(horizontal: 50, vertical: 15)
            ),
          )
        ],
      ),
    );
  }
}