
import dudraw

class Node:
    def __init__(self, v, n, p):
        self.value = v
        self.next = n
        self.prev = p

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __str__(self):
        listy = "["
        if self.header.next is None:
            raise ValueError("List is Empty!")
        temp_node = self.header.next
        while temp_node is not self.trailer:
            listy = listy + (str(temp_node.value))
            if temp_node.next is not None:
                listy = listy + " " 
            temp_node = temp_node.next
        return f"{str(listy)}]"

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def get_size(self):
        return self.size

    def add_between(self, v, n1, n2):
        if n1.next is not n2:
            raise ValueError("Wrong Nodes Passed")
        else:
            new_node = Node(v, n2, n1)
            n1.next = new_node
            n2.prev = new_node
        self.size += 1

    def add_first(self, v):
        return self.add_between(v, self.header, self.header.next)
    
    def add_last(self, v):
        return self.add_between(v, self.trailer.prev, self.trailer)

    def remove_between(self, n1, n2):
        if n1 is None or n2 is None:
            raise ValueError("Nodes are empty")
        if self.size == 0:
            raise ValueError("List is empty")
        if n1.next.next is not n2:# checks to make sure there's only one node in between n1 and n2
            raise ValueError("Wrong nodes passed, multiple nodes between") 
        
        return_value = n1.next.value
        n1.next = n2
        n2.prev = n1
        self.size-=1
        return return_value

    def remove_first(self):
        return self.remove_between(self.header, self.header.next.next)
    
    def remove_last(self):
        return self.remove_between(self.trailer.prev.prev, self.trailer)
    
    def first(self):
        return self.header.next.value

    def last(self):
        return self.trailer.prev.value
    
    def get(self, i):
        if self.header.next is None:
            return None
        if i >= self.size:
            raise IndexError("Invalid Index")

        temp_node = self.header.next
        for i in range(i-1):
            temp_node - temp_node.next
        index_value = temp_node.value
        return index_value

    def search(self, value):
        if self.header.next is None:
            return ValueError("The list is empty!")
        
        else:
            temp_node = self.header.next
            for i in range(self.size):
                if temp_node.value == value:
                    return_value = (i)
                    return return_value
                elif temp_node.value != value:
                    return_value = -1
                    temp_node = temp_node.next
            return return_value