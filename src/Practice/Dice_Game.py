import random

class dice:
    #すごろくクラス

    def __init__(self, Num = 6):
        self.Num = Num

    def roll(self):
        print(random.randrange(1,self.Num + 1))


d = dice()
d.roll()