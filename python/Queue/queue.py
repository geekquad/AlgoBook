class QueueOverflowError(BaseException):
    pass


class QueueUnderflowError(BaseException):
    pass


class Queue:
    def __init__(self, limit=10):
        self.limit = limit
        self._size = 0
        self.queue = []

    def __bool__(self):
        return bool(self.queue)

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return self._size

    def __contains__(self, item) -> bool:
        return item in self.queue

    def enqueue(self, item):
        """
        Inserts an item at the end of queue.
        The runtime complexity of this method is O(1).
        """
        if len(self.queue) >= self.limit:
            raise QueueOverflowError("Cannot insert item in a full queue.")
        self.queue.append(item)
        self._size += 1

    def dequeue(self):
        """
        Removed item from the front of queue.
        The runtime complexity of this method is O(1).
        """
        if self.isEmpty():
            raise QueueUnderflowError("Cannot Remove an item from empty Queue.")
        self.queue.pop(0)
        self._size -= 1

    def peek(self):
        """
        Return item from the front of queue.
        The runtime complexity of this method is O(1).
        """
        return self.queue[0]

    def isFull(self):
        """
        Returns if the queue is full or not.
        """
        return self._size == self.limit

    def isEmpty(self):
        """
        Returns if the queue is empty or not.
        """
        return self._size == 0


if __name__ == "__main__":
    queue = Queue(3)
    print(queue.isEmpty())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.isFull())
    print(queue)
    queue.dequeue()
    print(queue.peek())
    print(queue.isEmpty())
    print(queue.isFull())
    print(queue)
