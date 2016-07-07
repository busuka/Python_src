class Dictionary():

    def __init__(self, max=10):
        self.dic = [[None for x in range(max)], [None for y in range(max)]]
        self.max = max

    def h(self, key):
        return key % self.max

    def insert(self, key, value):
        hash_key = self.h(key)
        self.dic[0][hash_key] = key
        self.dic[1][hash_key] = value

    def search(self, key):
        hash_key = key % 10
        print(self.dic[1][hash_key])

    def display(self):
        print(self.dic)


a = Dictionary()
a.insert(33, "a")
a.insert(45,"dd")
a.search(33)
a.display()
