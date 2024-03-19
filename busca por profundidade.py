class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices:
            self.vertices[vertice1].append(vertice2)
        else:
            self.vertices[vertice1] = [vertice2]

    def busca_profundidade(self, vertice_inicial):
        visitados = set()
        pilha = [vertice_inicial]

        while pilha:
            vertice = pilha.pop()
            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                for vizinho in self.vertices.get(vertice, []):
                    if vizinho not in visitados:
                        pilha.append(vizinho)


grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_vertice('E')
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'D')
grafo.adicionar_aresta('B', 'E')

print("Busca em profundidade a partir do vértice 'A':")
grafo.busca_profundidade('A')