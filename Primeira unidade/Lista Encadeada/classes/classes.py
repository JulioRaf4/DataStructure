
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0
        self.tail = None

    def append(self, data):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(data)
            self.__size += 1
        else:
            self.head = Node(data)
            self.__size += 1

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, data):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = data
        else:
            raise IndexError("list index out of range")

    def index(self, data):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == data:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("data not found")
    
    def append_inicio(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__size += 1
    
    def clear(self):
        self.head = None
        self.__size = 0
    
    def pop_last(self):
        self[self.__size - 1] = None
        self.__size -= 1

    def pop_first(self):
        if self.head:
            self.head = self.head.next
            self.__size -= 1
        else:
            raise IndexError("pop from empty list")