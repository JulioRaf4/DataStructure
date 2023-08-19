from classes.classes import Vetor

a = Vetor(10)

print(a)
a.adiciona(4, "$$$$")
print(a)

a.adiciona_inicio("INICIO 1")
a.adiciona_fim("FIM 1")
print(a)

a.adiciona_inicio("INICIO 2")
print(a)

a.adiciona_inicio("INICIO 3")
print(a)