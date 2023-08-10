from abc import ABC, abstractmethod
from item import Item


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
