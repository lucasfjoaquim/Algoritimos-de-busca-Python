from collections import deque


def busca_largura(arvore, raiz):
    visitados = set()
    fila = deque([raiz])

    while fila:
        no = fila.popleft()
        if no not in visitados:
            print(no)
            visitados.add(no)
            fila.extend(arvore[no])


arvore = {
    'A': ['B', 'B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': []
}

busca_largura(arvore,"A")