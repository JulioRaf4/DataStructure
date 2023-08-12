
class Locadora:
    def __init__(self):
        self.indiceD = 0
        self.indiceF = 0
        self.array_disco = [None, None]
        self.array_filme = [None, None]

    def novoDisco(self, disco):
        if self.indiceD <= 2:
            self.array_disco.append(disco)
            self.indiceD += 1
        else:
            print("Capacidade máxima atingida.")

    def novoFilme(self, Filme):
        if self.indiceF <= 2:
            self.array_filme.append(Filme)
            self.indiceF += 1
        else:
            print("Capacidade máxima atingida.")

    def listarDiscos(self):
        for x in self.array_disco:
            x.lista_informacoes()

    def listarFilme(self):
        for x in self.array_filme:
            x.lista_informacoes()
