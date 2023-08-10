from abc import ABC, abstractmethod
from item import Item


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
        pass
