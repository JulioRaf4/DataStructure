class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class List:
    def __init__(self):
        self.head = None
        self.tail = None


    def createDLL(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node


    def __iter__(self):
        node = self.head
        
        while node:
            yield node
            node = next


    def printList(self):
        node = self.head
        while node:
            print(node.data)
        
    def InsertAtBeginning(self, data):
        new_node = Node(data)
        self.head.prev = self.head
        new_node.next = self.head
        self.head = new_node
        
    
    def inMid(self,prev_node, value):
        if prev_node is None:
            raise ValueError("Invalid")

        next_node = prev_node.next 
        new_node = Node(value)
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        
        
    def atEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            last_node = self.head
            while(last_node.next is not None):
                last_node = last_node.next
                
            last_node.next = new_node
            new_node.prev = last_node
            self.tail = new_node


    def printForward(self):
        if self.head == None:
            raise ValueError("No data in the list")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                
    
    def printReversed(self):
        if self.head == None:
            raise ValueError("No data in the list")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    
    def searchList(self, value): 
        position = 0
        found = 0
        if self.head is None:
            print ("The linked list does not exist")
        else:
            temp_node = self.head  
            while temp_node is not None:
                    position = position + 1
                    if temp_node.value == value:
                            print ("The required value was found at position: " + str(position))
                            found = 1
                    temp_node = temp_node.next    
        if found == 0:
            print ("The required value does not exist in the list")
            
            
    def delBeg(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        elif (self.head is not None):
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            return


    def delMid(self, del_value):
       if(self.head == None):
                return
       temp_node = self.head
       found = False
       while (temp_node) :
             if(temp_node.value == del_value):
                  found = True
                  break
             temp_node = temp_node.next
       if (found == True):
             prev_node = temp_node.prev
             next_node = temp_node.next
             prev_node.next = next_node
             next_node.prev = prev_node
             return
       else:
             print("Element not found.") 
             
    
    def delEnd(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            while (temp_node.next is not self.tail):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            return