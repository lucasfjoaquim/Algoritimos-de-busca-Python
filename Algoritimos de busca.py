class Algoritimos:

    def __init__(self, lista, alvo):
        self.lista = lista
        self.alvo = alvo


    def linear(self):
        for i in range(len(self.lista)):
            if self.lista[i] == self.alvo:
                return i

    def busca_binaria(self):
        inicio = 0
        fim = len(self.lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.lista[meio] == self.alvo:
                return meio
            elif self.lista[meio] < self.alvo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return -1