class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def size(self):
        return self.count

    def add(self, data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        self.count += 1

    def printList(self):
        temp = self.head
        if self.head != None:
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.add(1)
    cll.add(-2)
    cll.add(40)
    cll.add(-101)
    cll.add(220)
    cll.add(13)
    cll.printList()
    print(cll.size())
