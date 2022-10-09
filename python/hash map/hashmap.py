class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):

        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):

        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"

    def delete_val(self, key):

        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(50)


hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()


print(hash_table.get_val('portal@example.com'))
print()

hash_table.delete_val('portal@example.com')
print(hash_table)
