class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Key: {self.key} Value: {self.value}"

    def __str__(self):
        return str({self.key: self.value})


class HashTable:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [None for _ in range(table_size)]

    def __str__(self):
        return str([item for item in self.table])

    def _hash(self, key):
        return key % self.table_size

    def _quadratic_probing(self, index, i):
        return (index + i**2) % self.table_size

    def _get_index(self, key):
        index = self._hash(key)
        i = 1
        while self.table[index]:
            if self.table[index].key == key:
                return index
            index = self._quadratic_probing(self._hash(key), i)
            i += 1
        return None

    def put(self, key, value):
        index = self._hash(key)
        i = 1
        while self.table[index]:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index = self._quadratic_probing(self._hash(key), i)
            i += 1
        self.table[index] = KeyValue(key, value)

    def get(self, key):
        index = self._get_index(key)
        if not index is None:
            return self.table[index].value
        return None

    def remove(self, key):
        index = self._get_index(key)
        if not index is None:
            return self.table.pop(index).value
        return None


if __name__ == "__main__":
    table = HashTable()
    table.put(10, "Bimal Timilsina")
    table.put(11, "Kamal Timilsina")
    table.put(14, 50)
    table.put(20, "Hello")
    print(table.get(10))
    print(table.remove(20))
    print(table)
