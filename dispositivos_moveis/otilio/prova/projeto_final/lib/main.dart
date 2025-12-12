import 'package:flutter/material.dart';
import 'package:projeto_final/login_screen.dart';
import 'mapa_screen.dart';
import 'cadastro_contato_screen.dart';
import 'lista_contatos_screen.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'projeto final flutter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true
      ),
      home: const LoginScreen(),
    );
  }
}

