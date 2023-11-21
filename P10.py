# ...

while True:
    print("\nMenú:")
    print("1. Mostrar grafo")
    print("2. Ingresar arista")
    print("3. Eliminar arista")
    print("4. Encontrar camino")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    
    # Mostrar el grafo
    if opcion == '1':
        print("Grafo actual:")
        print(grafo.edges())
    
    # Ingresar arista
    elif opcion == '2':
        arista = input("Ingrese una arista en el formato 'nodo_inicial nodo_final': ")
        try:
            nodo_inicial, nodo_final = map(int, arista.split())
            grafo.add_edge(nodo_inicial, nodo_final)
            print(f"Arista ({nodo_inicial} -> {nodo_final}) agregada al grafo.")
        except ValueError:
            print("Formato incorrecto. Debe ingresar dos números separados por un espacio.")
    
    # Eliminar arista
    elif opcion == '3':
        arista = input("Ingrese una arista a eliminar en el formato 'nodo_inicial nodo_final': ")
        try:
            nodo_inicial, nodo_final = map(int, arista.split())
            if grafo.has_edge(nodo_inicial, nodo_final):
                grafo.remove_edge(nodo_inicial, nodo_final)
                print(f"Arista ({nodo_inicial} -> {nodo_final}) eliminada del grafo.")
            else:
                print(f"No se encontró la arista ({nodo_inicial} -> {nodo_final}) en el grafo.")
        except ValueError:
            print("Formato incorrecto. Debe ingresar dos números separados por un espacio.")
    
    # Buscar camino
    elif opcion == '4':
        nodo_inicial = int(input("Ingrese el nodo inicial: "))
        nodo_final = int(input("Ingrese el nodo final: "))
        resultado = buscar_camino_en_grafo(grafo, nodo_inicial, nodo_final)
        if resultado is not None:
            print(f"Se encontró un camino entre {nodo_inicial} y {nodo_final}: {resultado}")
        else:
            print(f"No se encontró un camino entre {nodo_inicial} y {nodo_final}.")

    # Salir
    elif opcion == '5':
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida del menú.")
