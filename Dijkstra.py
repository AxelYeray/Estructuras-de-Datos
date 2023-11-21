## Grafo inicial
def crear_grafo():
    diccionario = {
        "1": {"2": 3, "3": 1},
        "2": {"6": 4},
        "3": {"4": 5},
        "4": {"1": 2, "5": 1},
        "5": {"3": 2, "2": 2},
        "6": {"5": 2},
    }
    return diccionario


grafo = crear_grafo()

print(
    "El grafo dirigido de origen único y con pesos no negativos es: \n {} \n".format(
        grafo
    )
)

nodos_disponibles = list(grafo.keys())

nodo_fuente = input(
    "Ingrese el nodo de origen de la siguiente lista:  \n {} - ".format(
        nodos_disponibles
    )
)
while nodo_fuente not in nodos_disponibles:
    nodo_fuente = input(
        "Ingrese un nodo de origen válido de la siguiente lista:  \n {} - ".format(
            nodos_disponibles
        )
    )

nodo_destino = input(
    "Ingrese el nodo de destino de la siguiente lista:  \n {} - ".format(
        nodos_disponibles
    )
)
while nodo_destino not in nodos_disponibles:
    nodo_destino = input(
        "Ingrese un nodo de destino válido de la siguiente lista:  \n {} - ".format(
            nodos_disponibles
        )
    )

while nodo_fuente == nodo_destino:
    print("El nodo de origen y destino son iguales.")
    nodo_destino = input(
        "Ingrese un nodo de destino diferente:  \n {} - ".format(nodos_disponibles)
    )

nodo_fuente_final = nodo_fuente
camino = {nodo: float("inf") for nodo in grafo}

print("Diccionario de camino inicial \n {}".format(camino))

distancia = 0
visitados = []

while nodo_fuente in grafo:
    en_diccionario = grafo[nodo_fuente]

    corto = min(en_diccionario.values())
    s = None

    for k in grafo[nodo_fuente]:
        if grafo[nodo_fuente][k] == corto and (k not in visitados):
            visitados.append(k)
            distancia += corto  # Actualizar la distancia acumulada
            s = k

    nodo_fuente = s

    if nodo_fuente == nodo_destino:
        print("Has llegado a tu destino.")
        visitados_finales = " -> ".join([str(item) for item in visitados])
        print("Camino seguido: {} -> {}".format(nodo_fuente_final, visitados_finales))
        print("Costo: {}".format(distancia))

if nodo_fuente not in grafo:
    print(
        "No se puede llegar al punto final desde este origen debido a la falta de un camino disponible."
    )