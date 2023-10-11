class Node:
    def __init__(self, *args):
        self.data = args
        self.next = None
        
class Stack:
    def __init__(self):
        self._size = 0
        self.top = None

    def pull_on_top(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._size += 1

    def top_(self):
        if self.top: return self.top.data
        else: raise IndexError("Lista vazia")
    
    def push(self):
        pass
    
    def pop(self):
        pass
    
    def __size__(self):
        return self._size


stack = Stack()
stack.pull_on_top(10)
stack.pull_on_top(23)
stack.pull_on_top(40)
print(stack.top_())
