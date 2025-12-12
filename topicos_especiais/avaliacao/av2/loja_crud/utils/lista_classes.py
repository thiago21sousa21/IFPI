def retornar_lista_instancias(classe, resultados):
    instancias = []
    for resultado in resultados:
        instancia = classe(**resultado) 
        instancias.append(instancia)

    return instancias
