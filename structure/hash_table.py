class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(8)]

    def __len__(self):
        return len(self.table)

    def _hash(self, key):
        return key % len(self)

    def put(self, key: int, value: int):
        k = self._hash(key)
        for i in self.table[k]:
            if i[0] == key:
                i[1] = value
                return
        self.table[k].append([key, value])

    def get(self, key):
        k = self._hash(key)
        for i in self.table[k]:
            if i[0] == key:
                return i[1]
        return None

    def resize(self, new_size):
        old_table = self.table
        self.table = [[] for _ in range(new_size)]
        for i in old_table:
            for j in i:
                self.put(j[0], j[1])
