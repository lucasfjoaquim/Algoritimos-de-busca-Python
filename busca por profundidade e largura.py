from collections import deque


def busca_largura(arvore, raiz):
    visitados = set()
    fila = deque([raiz])

    while fila:
        no = fila.popleft()
        if no not in visitados:
            print(no, end=" ")
            visitados.add(no)
            fila.extend(arvore[no])
    print("\n")


def busca_profundidade(arvore, vertice_inicial):
    visitados = set()
    pilha = [vertice_inicial]

    while pilha:
         vertice = pilha.pop()
         if vertice not in visitados:
              print(vertice, end=" ")
              visitados.add(vertice)
              for vizinho in arvore.get(vertice, []):
                    if vizinho not in visitados:
                        pilha.append(vizinho)
    print("\n")

arvore = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': []
}

print("Busca em profundidade a partir do vértice 'A':")
busca_profundidade(arvore,"A")
busca_largura(arvore,"A")