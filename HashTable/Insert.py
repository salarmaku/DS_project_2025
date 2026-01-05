class HashTable:
    def __init__(self, ht_size):
        self.size = ht_size
        self.ht = [None] * ht_size
    
    def hashFunction(self, key):
        return (key % self.size)
    
    '''CHAINING METHOD: if we don't have enough room for all of the values
       we turn each index into a "LIST" or a "SET" so we can store all of
       vallues with the same key inside one room.'''

    def insert(self, value, key):
        index = self.hashFunction(key)
        if self.ht[index] == None:
            self.ht[index] = [(key, value)]
        else:
            self.ht[index].append((key, value))

#TEST
ht = HashTable(5)
ht.insert("A", 2)
ht.insert("B", 3)
ht.insert("C", 7) #this key should "collide" with the first inserted value so we used chaining method.

print(ht.ht[2])
print(ht.ht[3])
