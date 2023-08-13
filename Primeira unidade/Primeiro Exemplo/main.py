from classes.classes import Locadora, Disco, Filme

locadora = Locadora()
disco1 = Disco("Thriller", 1982,
               "Um dos álbuns mais vendidos de todos os tempos", "Michael Jackson", 9)
disco2 = Disco("Back in Black", 1980, "Clássico do rock", "AC/DC", 5)
filme1 = Filme("Matrix", 1999, "Um filme revolucionário", "Michael", "Ficção")
filme2 = Filme("Pulp Fiction", 1994, "Um filme cult", "Julio", "Humor")

locadora.novoDisco(disco1)
locadora.novoDisco(disco2)
locadora.novoFilme(filme1)
locadora.novoFilme(filme2)

locadora.listarDiscos()
locadora.listarFilmes()
