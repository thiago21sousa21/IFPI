import 'package:flutter/material.dart';
import 'package:projeto_final/home_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController _emailController = TextEditingController();
  TextEditingController _senhaController = TextEditingController();

  // Função fictícia para simular a autenticação
  void _fazerLogin() {
    String email = _emailController.text;
    String senha = _senhaController.text;

    // Lógica simples de validação (a validação real do projeto final virá depois)
    if (email == "teste@ifpi.edu.br" && senha == "123") {
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        padding: EdgeInsets.all(32.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SizedBox(height: 50),
            
            // 1. Logo do IFPI (Imagem) [cite: 105]
            // Nota: Você precisará adicionar o logo do IFPI (e a referência no pubspec.yaml) para que funcione.
            // Para o nosso projeto, vamos usar um placeholder de texto por enquanto.
            // Image.asset('caminho/para/logo_ifpi.png', height: 100),
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

            // 2. Campo de Email [cite: 106]
            TextField(
              controller: _emailController,
              keyboardType: TextInputType.emailAddress, // Teclado de email [cite: 106]
              decoration: InputDecoration(
                labelText: "Email",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            // 3. Campo de Senha [cite: 107]
            TextField(
              controller: _senhaController,
              obscureText: true, // Caracteres não visíveis [cite: 107]
              decoration: InputDecoration(
                labelText: "Senha",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 40),

            // 4. Botão Entrar [cite: 115]
            ElevatedButton(
              onPressed: _fazerLogin,
              child: Text(
                "Entrar",
                style: TextStyle(fontSize: 20, color: Colors.white),
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.amber, // Cor amarela como na imagem [cite: 115]
                minimumSize: Size(double.infinity, 50), // Largura total
              ),
            ),
            
            SizedBox(height: 20),
            
            // 5. Botão Cadastrar conta / Recuperar senha [cite: 108, 110]
            TextButton(
              onPressed: () {
                print("Navegar para Cadastro de Usuário ou Recuperar Senha.");
              },
              child: Text("Cadastrar conta / Recuperar senha"),
            ),
          ],
        ),
      ),
    );
  }
}