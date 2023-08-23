from classes.classes import *

n1 = Node(10)
n2 = Node(25)
n3 = Node(50)
a = LinkedList()

a.append(n1)
a.append(n2)
a.append(n3)
print(f'Tamanho de a = {len(a)}')

print(f'Primeira posição da lista = {a[0]}')

print(a.index(n3))