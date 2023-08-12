from classes.disco import Disco
from classes.filme import Filme
from classes.locadora import Locadora


locadora = Locadora()
disco1 = Disco("Thriller", 1982, "Um dos álbuns mais vendidos de todos os tempos", "Michael Jackson", 9, "CD")
disco2 = Disco("Back in Black", 1980, "Clássico do rock", "AC/DC")
filme1 = Filme("Matrix", 1999, "Um filme revolucionário", "2h 16min")
filme2 = Filme("Pulp Fiction", 1994, "Um filme cult", "2h 34min")

locadora.novoDisco(disco1)
locadora.novoDisco(disco2)
locadora.novoFilme(filme1)
locadora.novoFilme(filme2)

print("Discos na locadora:")
locadora.ListarDiscos()

print("\nFilmes na locadora:")
locadora.ListarFilmes()