class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._size = 0
        self.top = None

    def push(self, data):
        # Add on top of stack

        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._size += 1

    def print_stack(self):
        # Print the stack

        if self.top:
            node = self.top
            while node:
                print(f"[{node.data}]")
                node = node.next
        else:
            raise IndexError("List is empty")

    def is_empty(self) -> bool:
        # Verify if the stack is empty

        if self._size == 0:
            return True
        else:
            return False

    def top_(self):
        # Get the top of the stack

        if self.top:
            return self.top.data
        else:
            raise IndexError("Lista vazia")

    def pop(self):
        # Remove the last element from the stack

        if self.top:
            self.top.data = None
            self.top = self.top.next
            self._size -= 1
        else:
            raise IndexError("List is already empty")

    def __size__(self):
        return self._size

    def delete_stack(self):
        self.top = None
        self._size = None


stack = Stack()
stack.is_empty()
stack.push(10)
stack.push(23)
stack.push(40)
stack.print_stack()
stack.delete_stack()
print("/q")
stack.print_stack()