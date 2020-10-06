class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            current = self.head
            self.head = node
            node.prev = None
            node.next = current
        self.length += 1

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            current = self.head
            while current.next:
                current = current.next
            last = current
            current.next = node
            self.tail = node
            node.prev = last
        self.length += 1

    def popFirst(self):
        if self.head:
            current = self.head
            self.head = current.next
            current.next.prev = None
            self.length -= 1

    def pop(self):
        if self.head:
            second_last = self.tail.prev
            self.tail = second_last
            self.tail.next = None
            self.length -= 1

    def toArray(self):
        array = []
        if self.head:
            current = self.head
            while current:
                array.append(current.data)
                current = current.next
        return array

    def size(self):
        return self.length


if __name__ == "__main__":
    doublyLinkedList = DoublyLinkedList()
    doublyLinkedList.prepend(100)
    doublyLinkedList.append("A")
    doublyLinkedList.popFirst()
    doublyLinkedList.prepend("500")
    doublyLinkedList.append(-10)
    doublyLinkedList.pop()
    print(doublyLinkedList.toArray())
    print(doublyLinkedList.isEmpty())
