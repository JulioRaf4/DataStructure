from classes.classes import *

n1 = Node(10)
n2 = Node(25)
n3 = Node(50)
n12 = Node(44)
n23 = Node(222)
n34 = Node(533)
a = LinkedList()

a.append(n1)
a.append(n2)
a.append(n3)
a.append(n12)
a.append(n23)
a.append(n34)

print(f'Tamanho de a = {len(a)}')

print("~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(a)):
    print(a[i])


a.pop_last()

print("~~~~~~~~~~~~~~~~~~~~~~")

for i in range(len(a)):
    print(a[i])

print("~~~~~~~~~~~~~~~~~~~~~~")

a.append_inicio(Node(100))

for i in range(len(a)):
    print(a[i])
    
print("~~~~~~~~~~~~~~~~~~~~~~")

a.pop_first()

for i in range(len(a)):
    print(a[i])
    