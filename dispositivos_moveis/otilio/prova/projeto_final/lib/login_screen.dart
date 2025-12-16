import 'package:flutter/material.dart';
import 'package:projeto_final/cadastro_contato_screen.dart';
import 'package:projeto_final/cadastro_usuario_screen.dart';
import 'package:projeto_final/controller/usuario_helper.dart';
import 'package:projeto_final/home_screen.dart';
import 'package:projeto_final/model/usuario.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController _emailController = TextEditingController();
  TextEditingController _senhaController = TextEditingController();
  final UsuarioHelper _helper = UsuarioHelper();

  // Função fictícia para simular a autenticação
  void _fazerLogin() async{
    String email = _emailController.text;
    String senha = _senhaController.text;

    Usuario? usuario = await _helper.autenticar(email, senha);

    if (usuario != null) {
      // Login bem-sucedido: Navegar para a tela de entrada (Home)
     Navigator.pushReplacement(
      context, 
      MaterialPageRoute(builder: (context) => HomeScreen())
    );
      
    } else {
      // Exibir erro
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Email ou senha incorretos.")),
      );
    }
  }

  Future<void> _iniciarRecuperacaoSenha(BuildContext context) async {
    TextEditingController emailRecController = TextEditingController();
    TextEditingController perguntaRecController = TextEditingController();

    await showDialog(
      context: context, 
      builder: (context) => AlertDialog(
        title: const Text("Recuperação de Senha"),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(controller:  emailRecController, decoration: const InputDecoration( labelText: "Email Cadastrado")),
            TextField(controller: perguntaRecController, decoration: const InputDecoration(labelText: "Resposta Secreta"),)
          ],
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: const Text("Cancelar ")),
          TextButton(
            onPressed: () async {
              Navigator.pop(context);
              Usuario? usuario = await _helper.buscarPorEmailPergunta(
                emailRecController.text, 
                perguntaRecController.text
              );

              if (usuario !=null){
                Navigator.pushReplacement(
                  context, 
                  MaterialPageRoute(
                    builder: (context) => CadastroUsuarioScreen(
                      modo: ModoAutenticacao.redefinir,
                      usuarioParaEdicao: usuario
                    )
                  )
                );
              } else {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text("Email ou resposta secreta incorretos.")),
                );
              }
            }, 
            child: const Text("Verificar")
          )
        ],
      )
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        padding: EdgeInsets.all(32.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SizedBox(height: 50),
           
            Image.asset('assets/logo_ifpi.png', height: 100),
            Container(
              height: 100,
              alignment: Alignment.center,
              child: Text(
                "INSTITUTO FEDERAL\nPIAUÍ", 
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF4C7D5F)),
              ),
            ),
            
            SizedBox(height: 80),

            TextField(
              controller: _emailController,
              keyboardType: TextInputType.emailAddress,
              decoration: InputDecoration(
                labelText: "Email",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            TextField(
              controller: _senhaController,
              obscureText: true,
              decoration: InputDecoration(
                labelText: "Senha",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 40),

            ElevatedButton(
              onPressed: _fazerLogin,
              child: Text(
                "Entrar",
                style: TextStyle(fontSize: 20, color: Colors.white),
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.amber, 
                minimumSize: Size(double.infinity, 50), 
              ),
            ),
            
            SizedBox(height: 20),
            
            TextButton(
              onPressed: () async {
                await showDialog(
                  context: context, 
                  builder: (context) => AlertDialog(
                    title: const Text("Opções de Conta"),
                    content: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        ElevatedButton(
                          onPressed: () {
                            Navigator.pop(context);
                            Navigator.push(
                              context, 
                              MaterialPageRoute(
                                builder: (context) => const CadastroUsuarioScreen(modo: ModoAutenticacao.cadastro)
                              )
                            );
                          }, 
                          child: const Text("Cadastrar Nova Conta")
                        ),
                        TextButton(
                          onPressed: () async {
                            Navigator.pop(context);
                            await _iniciarRecuperacaoSenha(context);
                          }, 
                          child: const Text("Recuperar Senha")
                        )
                      ],
                    ),
                  )
                );
              },
              child: Text("Gerenciar conta"),
            ),
          ],
        ),
      ),
    );
  }
}