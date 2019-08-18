class DoubleHash:
    def __init__(self):
        self.table_size = 13
        self.prime = 7
        self.current_size = 0
        self.hash_table = []*self.table_size
        for i in range(0, self.table_size):
            self.hash_table[i] = -1

    def is_full(self):
        return self.current_size == self.table_size

    def hash1(self, key):
        return key % self.table_size

    def hash2(self, key):
        return self.prime - key % self.prime

    def insert_hash(self, key):
        if self.is_full():
            return
        index = self.hash1(key)

        if self.hash_table[index] != -1:
            index2 = self.hash2(key)
            i = 1
            while True:
                new_index = (index + i * index2) % self.table_size
                if self.hash_table[new_index] == -1:
                    self.hash_table[new_index] = key
                    break
                i += 1
        else:
            self.hash_table[index] = key
            self.current_size += 1

    def display_hash_table(self):
        for i in range(0, self.table_size):
            if self.hash_table[i] != -1:
                print("{}-->{}".format(i, self.hash_table[i]), end=" ")
            else:
                print(i, end=" ")


if __name__ == '__main__':
    arr = [19, 27, 36, 10, 64]
    length = len(arr)
    dh = DoubleHash()
    for i in range(0, length):
        dh.insert_hash(arr[i])
    print("Hash Table after inserting all the key")
    dh.display_hash_table()
