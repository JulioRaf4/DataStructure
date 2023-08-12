from item import Item
from abc import ABC, abstractmethod


# Como o python não tem algo como
# > private String titulo; <
# Usei __titulo como um bom dev python

class Item(ABC):
    def __init__(self, titulo, ano_lancamento, comentario):
        self.__titulo = titulo
        self.__ano_lancamento = ano_lancamento
        self.__comentario = comentario

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_ano_lancamento(self):
        return self.__ano_lancamento

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def get_comentario(self):
        return self.__comentario

    def set_comentario(self, comentario):
        self.__comentario = comentario

    # Usei o decorator @abstractmethod
    # Para instanciar o metodo abastrato
    @abstractmethod
    def lista_informacoes(self):
        pass


class Disco(Item):
    def __init__(self, titulo, ano_lancamento, comentario, nome_artista, quantidade_faixas):
        super().__init__(titulo, ano_lancamento, comentario)
        self.nome_artista = nome_artista  # Construtor especifico
        self.quantidade_faixas = quantidade_faixas  # Construtor especifico
        self.midia = ""  # Construtor padrão

    def get_nome_artista(self):
        return self.nome_artista

    def set_nome_artista(self, nome_artista):
        self.nome_artista = nome_artista

    def get_quantidade_faixas(self):
        return self.quantidade_faixas

    def set_quantidade_faixas(self, quantidade_faixas):
        self.quantidade_faixas = quantidade_faixas

    def get_midia(self):
        return self.midia

    def set_midia(self, midia):
        self.midia = midia

    @abstractmethod
    def lista_informacoes(self):
        print("Titulo: {self.titulo}")
        print("Ano lançamento: {self.ano_lancamento}")
        print("Comentario : {self.comentario}")
        print("Nome do artista: {self.nome_artista}")
        print("Quantidade de faixas: {self.quantidade_faixas}")
        print("Tipo de mídia: {self.midia}")


class Disco(Item):
    def __init__(self, titulo, ano_lancamento, comentario, nome_diretor, genero_do_filme):
        super().__init__(titulo, ano_lancamento, comentario)
        self.nome_diretor = nome_diretor  # Construtor especifico
        self.genero_do_filme = genero_do_filme  # Construtor especifico
        self.duracao = 0  # Construtor padrão

    def get_nome_diretor(self):
        return self.nome_diretor

    def set_nome_diretor(self, nome_diretor):
        self.nome_diretor = nome_diretor

    def get_genero_do_filme(self):
        return self.genero_do_filme

    def set_genero_do_filme(self, genero_do_filme):
        self.genero_do_filme = genero_do_filme

    def get_duracao(self):
        return self.duracao

    def set_duracao(self, duracao):
        self.duracao = duracao

    @abstractmethod
    def lista_informacoes(self):
        print("Titulo: {self.titulo}")
        print("Ano lançamento: {self.ano_lancamento}")
        print("Comentario : {self.comentario}")
        print("Nome do diretor: {self.nome_diretor}")
        print("Gênero do filme: {self.genero_do_filme}")
        print("Duração do filme: {self.duracao}")


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
