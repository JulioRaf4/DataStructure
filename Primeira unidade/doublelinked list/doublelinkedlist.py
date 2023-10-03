class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    