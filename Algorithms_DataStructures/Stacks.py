class Stacks():

    def __init__(self, max=10):
        self.list = [None for x in range(max)]
        self.top = 0
        self.max = max

    def initialize(self):
        self.list = []
        self.top = 0

    def push(self, push_val):
        if self.top >= self.max:
            print("これ以上データは格納できません")
            return 1
        if push_val == "+":
            self.list[self.top - 2] = self.list[self.top - 1] + self.list[self.top - 2]
            self.list[self.top - 1] = None
            self.top -= 1
            return 0
        self.list[self.top] = push_val
        self.top += 1

    def pop(self):
        if self.top == 0:
            print("格納しているデータがありません")
            return 1
        self.top -= 1
        pop_val = self.list[self.top]
        self.list[self.top] = None
        return pop_val

    def check(self):
        print(self.list)

    # TODO Write optimize the def.




if __name__ == "__main__":
    s = Stacks(5)
    s.push(5)
    s.push(3)
    s.push("+")
    s.check()