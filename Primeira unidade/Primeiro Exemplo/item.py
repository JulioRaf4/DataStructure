from abc import ABC, abastractmethod


# Como o python não tem algo como 
# > private String titulo; < 
# Usei __titulo como um bom dev python

class Item:
    def __ini__(self, titulo, ano_lancamento, comentario):
        self.__titulo = titulo
        self.__ano_lancamento = ano_lancamento
        self.__comentario = comentario

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_ano_lancamento(self):
        return self.ano_lancamento

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