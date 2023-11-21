def prim(graph, root):
    assert type(graph) == dict

    nodes = list(graph.keys())
    nodes.remove(root)

    visited = [root]
    path = []
    next_node = None

    while nodes:
        distance = float('inf')
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next_node = d
        path.append((pre, next_node))
        visited.append(next_node)
        nodes.remove(next_node)

    return path

if __name__ == '__main__':
    graph_dict = {
        "s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
        "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
        "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
    }

    while True:
        print("\n=== Menú ===")
        print("1. Ejecutar algoritmo de Prim")
        print("2. Salir")

        choice = input("Seleccione una opción (1/2): ")

        if choice == '1':
            root_node = input("Ingrese el nodo raíz: ")
            if root_node in graph_dict:
                path = prim(graph_dict, root_node)
                print("Camino mínimo:")
                print(path)
            else:
                print(f"El nodo '{root_node}' no existe en el grafo.")
        elif choice == '2':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
