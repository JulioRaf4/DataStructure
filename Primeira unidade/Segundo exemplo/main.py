from classes.classes import Vetor

a = Vetor(5)

print(a)
a.adiciona(1, "NADA")
print(a)

a.adiciona_inicio("INICIO")
a.adiciona_fim("FIM")

print(a)

print(a.existe_dado(0))
print(a.existe_dado(2))

print(f'Tamanho -> {a.tamanho()}')

a.adiciona(2, "Dois")
a.adiciona(3, "Três")

print(f'Tamanho -> {a.tamanho()}')

a.redimensionar
print(a)