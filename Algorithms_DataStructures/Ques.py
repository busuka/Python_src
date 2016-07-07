class Ques():

    def __init__(self,max=5):
        self.list = [None for x in range(max)]
        self.max = max
        self.head = 0
        self.tail = 0

    def initialize(self):
        self.list = [None for x in range(max)]
        self.head = 0
        self.tail = 0

    def enqueue(self,val):
        self.list[self.tail] = val
        self.tail += 1
        self.tail %= self.max

    def dequeue(self):
        self.head += 1
        self.head %= self.max
        rval = self.list[self.head - 1]
        self.list[self.head - 1] = None
        return rval

    def display(self):
        print(self.list,self.head,self.tail)

q = Ques()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.dequeue()
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)
q.dequeue()
q.display()