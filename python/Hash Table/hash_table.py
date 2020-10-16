import sys
sys.path.append('/Data_Structures/')
from linked_lists.linked_list import LinkedList



class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class KeyDoesnotExistError(BaseException):
    pass


class HashTable:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [None for _ in range(self.table_size)]

    def _hash(self, key):
        return key % self.table_size

    def put(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = LinkedList()
        bucket = self.table[index]
        if not bucket.isEmpty():
            current_bucket = bucket.first
            while current_bucket:
                if current_bucket.value.key == key:
                    current_bucket.value.value = value
                current_bucket = current_bucket.next
        self.table[index].addLast(KeyValue(key, value))

    def _get_bucket(self,key):
        return self.table[self._hash(key)]

    def get(self, key):
        bucket = self._get_bucket(key)
        if not bucket.isEmpty():
            current = bucket.first
            while current:
                if current.value.key == key:
                    return current.value.value
                else:
                    current = current.next
        else:
            return KeyDoesnotExistError("The key you are passing doesnot exist.")

    def remove(self, key):
        bucket = self._get_bucket(key)
        if not bucket.isEmpty():
            previous = None
            current = bucket.first
            while current:
                if current.value.key == key:
                    previous.next = current.next
                    return current.value.value
                else:
                    previous = current
                    current = current.next

if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.put(10, 20)
    hash_table.put(20, 30)
    hash_table.put(5, 50)
    print(hash_table.get(5))
    print(hash_table.remove(20))
    print("Hello World")
