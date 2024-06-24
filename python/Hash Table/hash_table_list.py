class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Key: {self.key}\n Value: {self.value}"

    def __str__(self):
        return str({self.key: self.value})


class HashTableList:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [None for _ in range(table_size)]

    def _hash(self, key):
        return key % self.table_size

    def put(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = list()
        bucket = self.table[index]
        if bucket:
            for item in bucket:
                if item.key == key:
                    item.value = value
        bucket.append(KeyValue(key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for item in bucket:
            if item.key == key:
                return item.value
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for idx, item in enumerate(bucket):
            if item.key == key:
                return bucket.pop(idx).value


if __name__ == "__main__":
    table = HashTableList()
    table.put(5, "Bimal Timilsina")
    table.put(20, "Kamal Timilsina")
    table.put(5, 50)
    print(table.get(5))
    print(table.remove(20))
