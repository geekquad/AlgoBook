class Node:
    def __init__(self, item):
        self.item = item 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def to_linkedlist(self, input_list):
        #Function to create a linked list from a input list.
        self.tail = None
        
        for item in input_list:
            if self.head is None:
                self.head = Node(item)
                self.tail = self.head
            
            else:
                self.tail.next = Node(item)
                self.tail = self.tail.next
        
        return self.head
    
    def append(self, item):
        # function to add item to the end of linkedlist.
        
        if self.head is None:
            self.head = Node(item) # if linkedlist is empty 
            return
        
        # Now , moving to the end of linkedlist to add item if linkedlist is not empty.
        node = self.head
        while node.next:
            node = node.next
            
        node.next = Node(item)
        return 
    
    def prepend(self, item):
        # function to add item at the front/beginning of the linkedlist.
        if self.head is None:
            self.head = Node(item) #when linkedlist is empty.
            return
        
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node # changing head of linkedlist to new node when linkedlist is not empty.
    
    def pop(self):
        # function returns the first node's item and remove it from the linkedlist.
        if self.head is None:
            return None
        
        node = self.head
        self.head = self.head.next
        
        return node.item
    
    def remove(self, item):
        # delete the first coming node with the desired item .
        if self.head is None:
            return None  #when linkedlist is empty.
        
        if self.head.item == item:
            self.head = self.head.next
            return
        
        node = self.head
        while node.next:
            if node.next.item == item:
                node.next = node.next.next
                return 
            node = node.next
            
        print('Value not found')
            
    def size(self):
        #function returns the size of the linkedlist.
        size = 0  # initialising size with value 0.
        node = self.head
        while node:
            size += 1
            node = node.next #Iterating through linkedlist.
            
        return size
    
    
    
    def to_list(self):
        # Function to create a simple list from Linkedlist.
        output_list = []
        
        node = self.head
        
        while node:
            output_list.append(node.item)
            node = node.next # loop terminates at last item of linkedlist.
            
        return output_list
    
    def insert_at_position(self, pos, item):
        """
        Function to insert a node with a given item value at a given position.

        Parameters:
        pos (int): The position at which the new node is placed. Position is 0 indexed.
        item (object): An item value to be placed inside a node.
        """

        # case of prepend
        if pos == 0:
            self.prepend(item)

        # case of append
        elif pos == self.size():
            self.append(item)

        # case at any position
        else:
            # traverse the linked list
            node = self.head
            count = 0
            new_node = Node(item)
            while node:
                # previous node found
                if pos == count+1:
                    new_node.next = node.next
                    node.next = new_node
                    break
                node = node.next
                count += 1
    
