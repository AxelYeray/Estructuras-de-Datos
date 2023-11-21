class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # Inicializar como una lista vacía

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        result = []  # Almacenará el árbol de expansión mínima
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # Ordena las aristas por peso

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        # Función para encontrar el conjunto al que pertenece un nodo
        def find_parent(i):
            if parent[i] == i:
                return i
            return find_parent(parent[i])

        # Función para unir dos conjuntos en uno solo
        def union(x, y):
            root_x = find_parent(x)
            root_y = find_parent(y)

            if root_x != root_y:
                    if rank[root_x] < rank[root_y]:
                        parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
            else:
                    parent[root_x] = root_y
                    rank[root_y] += 1


        e = 0  # Contador de aristas
        i = 0  # Índice para recorrer las aristas

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = find_parent(u)
            y = find_parent(v)

            if x != y:
                e += 1
                result.append((u, v, w))
                union(x, y)

        return result

# Crear el grafo
g = Graph(6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 2)
g.add_edge(2, 6, 4)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 2)
g.add_edge(4, 5, 1)
g.add_edge(6, 5, 2)

# Obtener el árbol de expansión mínima usando Kruskal
result = g.kruskal()

# Imprimir el resultado
for u, v, w in result:
    print(f"({u}, {v}, {w})")
