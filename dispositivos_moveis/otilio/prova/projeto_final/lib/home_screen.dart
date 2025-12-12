import 'package:flutter/material.dart';
import 'mapa_screen.dart'; // Para o botão Mapas
import 'lista_contatos_screen.dart'; // Para o botão Contatos

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("App de contatos"), // Título como na imagem [cite: 146]
        backgroundColor: Colors.amber, // Cor amarela como no slide [cite: 146]
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: <Widget>[
            // 1. Logo do IFPI (Placeholder)
            Image.asset('assets/ifpi_logo.png', height: 100), // Usaria o caminho da imagem real
            const SizedBox(height: 50),

            // 2. Grade de Botões (Grid 2x2)
            Expanded(
              child: GridView.count(
                crossAxisCount: 2, // 2 colunas
                crossAxisSpacing: 20, // Espaçamento horizontal
                mainAxisSpacing: 20, // Espaçamento vertical
                children: <Widget>[
                  // Botão Contatos
                  _buildMenuButton(
                    context,
                    title: 'Contatos',
                    icon: Icons.people,
                    color: Colors.amber,
                    onTap: () {
                      // Navegar para a lista de contatos
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const ListaContatosScreen()),
                      );
                    },
                  ),
                  // Botão Mapas
                  _buildMenuButton(
                    context,
                    title: 'Mapas',
                    icon: Icons.map,
                    color: Colors.amber,
                    onTap: () {
                      // Navegar para a tela de mapas
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const MapaScreen()),
                      );
                    },
                  ),
                  // Botões Extra 1 e Extra 2
                  _buildMenuButton(context, title: 'Extra', icon: Icons.star, color: Colors.amber, onTap: () {}),
                  _buildMenuButton(context, title: 'Extra', icon: Icons.star, color: Colors.amber, onTap: () {}),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Widget de ajuda para construir os botões do menu
  Widget _buildMenuButton(
    BuildContext context, {
    required String title,
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return InkWell( // Faz o widget responder a toques
      onTap: onTap,
      child: Container(
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(10),
        ),
        child: Center(
          child: Text(
            title,
            style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
          ),
        ),
      ),
    );
  }
}