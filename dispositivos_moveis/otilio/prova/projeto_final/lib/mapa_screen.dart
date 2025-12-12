import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:projeto_final/controller/database_helper.dart';
import 'package:projeto_final/model/contato.dart';


class MapaScreen extends StatefulWidget {
  const MapaScreen({super.key});
  @override
  State<MapaScreen> createState() => _MapaScreenState();
}

class _MapaScreenState extends State<MapaScreen> {
  ContatoHelper _helper = ContatoHelper();

  final CameraPosition _posicaoInicial = CameraPosition(
    target: LatLng(-5.0803407, -42.8150323),
    zoom: 14,
  );

  Set<Marker> _marcadores = {}; // Variável definida aqui 

  @override
  void initState() {
    super.initState();
    _carregarMarcadores();
  }

  void _carregarMarcadores() async {
    Set<Marker> marcadoresLocal = {};

    //temos que buscar todos os contatos do banco
    List<Contato> contatos = await _helper.buscarContatos();

    // temos agora que iterar sobre os contatos e criar um marcador para cada um

    for (Contato c in contatos){
      if (c.latitude != null && c.longitude != null){
        Marker marcador = Marker(
          markerId: MarkerId(c.id.toString()),
          position: LatLng(c.latitude!, c.longitude!),
          infoWindow: InfoWindow(
            title: c.nome,
            snippet: c.email,
            onTap: (){
              print("Clicou no marcador do contato: ${c.nome}");
            }
          )
        );
        marcadoresLocal.add(marcador);
      }
    }

    Marker marcadoIfpi = Marker(
      markerId: MarkerId('IFPI central'),
      position: LatLng(-5.0803407, -42.8150323),
      infoWindow: InfoWindow(title: 'IFPI - Campus Central'),
    );

    marcadoresLocal.add(marcadoIfpi);

    setState(() {
      _marcadores = marcadoresLocal;
    });
  }

  // 2. Método BUILD (OBRIGATÓRIO para retornar o widget)
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Mapas"),
      ),
      body: Center(
        child: GoogleMap(
          initialCameraPosition: _posicaoInicial,
          markers: _marcadores, // Aqui passamos o conjunto de marcadores 
          myLocationButtonEnabled: true,
          myLocationEnabled: true,
          mapType: MapType.normal,
          onMapCreated: (GoogleMapController controller){
            
          },
        ),
      ),
    );
  }
}