class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.prev = None
           
class DEQueue: 
    def __init__(self): 
        self.head = None
        self.tail = None

    def insertFront(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            n = Node(data)
            n.next = self.head
            self.head = n

    def insertRear(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def deleteFront(self):
        if self.head is None or self.tail is None:
            print("Underflow")

        elif self.head == self.tail:
            self.head = self.tail = None

        else:
            self.head = self.head.next
            self.head.tail = None

    def deleteRear(self):
        if self.tail is None or self.tail is None:
            print("Underflow")

        elif self.head == self.tail:
            self.head = self.tail = None
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None
   
    def getFront(self): 
        return self.head.data 

    def getRear(self): 
        return self.tail.data 
       
    def isEmpty(self): 
        if self.head is None: 
            return True
        else: 
            return False
               
    def printQueue(self):
        print("queue elements are:") 
        temp = self.head 
        while temp is not None: 
            print(temp.data, end = "->") 
            temp = temp.next
       
           
if __name__=='__main__':  
    queue = DEQueue() 

    while True:
        choice = int(input("1-Insert Front, 2-Insert Rear, 3-Delete Front, 4-Delete Rear, 5-Get Front, 6-Get Rear, 7-Is Empty, 8-Print, 9-Exit"))   
  
        if choice == 1:
            queue.insertFront()
        elif choice == 2:
            queue.insertRear()
        elif choice == 3:
            queue.deleteFront()
        elif choice == 4:
            queue.deleteRear()
        elif choice == 5:
            queue.getFront()
        elif choice == 6:
            queue.getRear()
        elif choice == 7:
            queue.isEmpty()
        elif choice == 8:
            queue.printQueue()
        elif choice == 9:
            break