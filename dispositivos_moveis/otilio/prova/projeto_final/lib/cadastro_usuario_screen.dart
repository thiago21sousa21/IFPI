

import 'package:flutter/material.dart';
import 'package:projeto_final/controller/usuario_helper.dart';
import 'package:projeto_final/login_screen.dart';
import 'package:projeto_final/model/usuario.dart';

enum ModoAutenticacao {cadastro, redefinir}

class CadastroUsuarioScreen extends StatefulWidget {
  final ModoAutenticacao modo;
  final Usuario? usuarioParaEdicao;

  const CadastroUsuarioScreen({super.key, required this.modo, this.usuarioParaEdicao});

  @override
  State<CadastroUsuarioScreen> createState() => _CadastroUsuarioScreenState();
}

class _CadastroUsuarioScreenState extends State<CadastroUsuarioScreen> {

  final _emailController = TextEditingController();
  final _senhaController  = TextEditingController();
  final _perguntaController = TextEditingController();
  final UsuarioHelper _helper = UsuarioHelper();

  bool _isLoading = false;

  @override
  void initState(){
    super.initState();

    if (widget.usuarioParaEdicao != null){
      _emailController.text = widget.usuarioParaEdicao!.email;
      _perguntaController.text = widget.usuarioParaEdicao!.perguntaSecreta;
    }
  }

  void _acaoPrincipal() async {
    final email = _emailController.text;
    final senha = _senhaController.text;
    final pergunta = _perguntaController.text;

    if (email.isEmpty || senha.isEmpty || pergunta.isEmpty){
      _mostrarMensagem("Por favor, preencha todos os campos.");
      return;
    }

    setState(() {
      _isLoading = true;
    });

    if(widget.modo == ModoAutenticacao.cadastro){
      Usuario novoUsuario = Usuario(email: email, senha: senha, perguntaSecreta: pergunta);
      int id = await _helper.cadastrarUsuario(novoUsuario);
    
      if (id > 0){
        _mostrarMensagem("Conta cadastrada com sucesso! ID: $id");
        Navigator.pop(context);
      } else if (id == -1){
        _mostrarMensagem("Email já cadastrado.");
      } else{
        _mostrarMensagem("Erro ao cadastrar.");
      }
    } else {
      Usuario usuario = widget.usuarioParaEdicao!;
      usuario.senha = senha;

      await _helper.updateUsuario(usuario);
      _mostrarMensagem("Senha alterada com sucesso!");

      Navigator.pushAndRemoveUntil(
        context, 
        MaterialPageRoute(builder: (context) => const LoginScreen()),
        (Route<dynamic> route) => false
      );
    }

    setState(() {
      _isLoading = false;
    });

  }

  void _deletarConta() async {
    if(widget.usuarioParaEdicao?.id != null){
      await _helper.deletarUsuario(widget.usuarioParaEdicao!.id!);
      _mostrarMensagem("const excluida com sucesso.");

      Navigator.pushAndRemoveUntil(
        context, 
        MaterialPageRoute(builder: (context) => const LoginScreen()),
        (Route<dynamic> route) => false
      );
    }
  }

  void _mostrarMensagem(String msg){
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(msg))
    );
  }

  @override
  Widget build(BuildContext context) {
    final bool isCadastro = widget.modo == ModoAutenticacao.cadastro;
    final String titulo = isCadastro ? "Criar Conta" : "Alterar Senha";
    final String botaoTexto = isCadastro ? "Cadastrar" : "Redefinir Senha";

    return Scaffold(
      appBar: AppBar(
        title: Text(titulo),
        actions: [
          if(!isCadastro)
            IconButton(
              icon: const Icon(Icons.delete),
              onPressed: _deletarConta,
            )
        ],
      ),
      body: _isLoading
        ? const Center(child: CircularProgressIndicator())
        : SingleChildScrollView(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            children: <Widget>[
              TextField(
                controller: _emailController,
                readOnly: !isCadastro,
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(labelText: "Email"),
              ),
              const SizedBox(height: 20,),

              TextField(
                controller: _senhaController,
                obscureText: true,
                decoration: InputDecoration(labelText: isCadastro ? "Senha" : "Nova senha"),
              ),
              const SizedBox(height: 20,),

              TextField(
                controller: _perguntaController,
                readOnly: !isCadastro,
                decoration: const InputDecoration(labelText: "Pergunta Secreta (Nome da Mãe, Pet, etc.)"),
              ),
              const SizedBox(height: 40,),

              ElevatedButton(
                onPressed: _acaoPrincipal,
                child: Text(botaoTexto),
              )
            ],
          ),
        ),
    );
  }
}