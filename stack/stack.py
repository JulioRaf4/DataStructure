class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._size = 0
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._size += 1

    def print_stack(self):
        if self.top:
            node = self.top
            while node:
                print(f"[{node.data}]")
                node = node.next
        else:
            pass

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def top_(self):
        if self.top:
            return self.top.data
        else:
            raise IndexError("Lista vazia")

    def pop(self):
        if self.top:
            self.top.data = None
            self.top = self.top.next
            self._size -= 1
        else:
            pass

    def __size__(self):
        return self._size


stack = Stack()
stack.is_empty()
stack.push(10)
stack.push(23)
stack.push(40)

stack.pop()


stack.print_stack()
