import 'package:flutter/material.dart';
import 'mapa_screen.dart'; 
import 'lista_contatos_screen.dart'; 

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("App de contatos"), 
        backgroundColor: Colors.amber, 
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: <Widget>[
            Image.asset('assets/logo_ifpi.png', height: 100),
            const SizedBox(height: 50),

            Expanded(
              child: GridView.count(
                crossAxisCount: 2,
                crossAxisSpacing: 20, 
                mainAxisSpacing: 20, 
                children: <Widget>[
                  _buildMenuButton(
                    context,
                    title: 'Contatos',
                    icon: Icons.people,
                    color: Colors.amber,
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const ListaContatosScreen()),
                      );
                    },
                  ),
                  _buildMenuButton(
                    context,
                    title: 'Mapas',
                    icon: Icons.map,
                    color: Colors.amber,
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const MapaScreen()),
                      );
                    },
                  ),
                  //_buildMenuButton(context, title: 'Extra', icon: Icons.star, color: Colors.amber, onTap: () {}),
                  //_buildMenuButton(context, title: 'Extra', icon: Icons.star, color: Colors.amber, onTap: () {}),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMenuButton(
    BuildContext context, {
    required String title,
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return InkWell( 
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