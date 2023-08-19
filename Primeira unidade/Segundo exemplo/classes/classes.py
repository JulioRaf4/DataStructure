
class Vetor:
    def __init__(self, x=0):
        self.x = x
        self.dados = [None]*self.x

    def __str__(self):
        return f"Vetor: {self.dados}"

    def adiciona(self, posicao, elemento):
        self.dados[posicao] = elemento

    def adiciona_inicio(self, elemento):
        self.dados[0] = elemento

    def adiciona_fim(self, elemento):
        self.dados[-1] = elemento

    def existe_dado(self, posicao):
        if self.dados[posicao]:
            return True
        else:
            return False

    def recupera(self, posicao):
        return self.dados[posicao]

    def vazio(self, posicao):
        if self.dados[posicao]:
            return False
        else:
            return True

    def remove(self, posicao):
        self.dados[posicao] = None

    def remove_fim(self):
        self.dados[-1] = None

    def remove_inicio(self):
        self.dados[0] = None

    def tamanho(self):
        c = 0
        for i in range(self.x):
            if self.dados[i]:
                c += 1
        return c

    def limpa(self):
        for i in range(self.x):
            self.dados[i] = None

    def redimensionar(self):
        if self.tamanho() == self.x:
            for i in range(self.x):
                self.dados.append(None)
