class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data
        
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.__size = None
        self.tail = None

def __len__(self):
    return self.__size

def cleaner(self):
    self.head = None
    self.tail = None
    self.__size = None
        