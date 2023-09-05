
class Locadora:
    def __init__(self):
        self.indiceD = 0
        self.indiceF = 0
        self.array_disco = [None, ]
        self.array_filme = []
    
    def novoDisco(self, disco):
        if len(self.array_disco) <= 2:
            self.array_disco.append(disco)
        else:
            print("Número excedido!")
        
    def novoFilme(self, Filme):
        if len(self.array_disco) <= 2:
            self.array_filme.append(Filme)
        else:
            print("Número excedido!")
            
    def listarDiscos(self):
        for x in self.array_disco:
            x.lista_informacoes()
    
    def listarFilme(self):
        for x in self.array_filme:
            x.lista_informacoes()
