import random

class field:
    #ボードクラス
    def __init__(self,goal = 10):
        self.goal = goal



class dice:
    #すごろくクラス

    def __init__(self, Num = 6):
        self.Num = Num

    def roll(self):
        print(random.randrange(1,self.Num + 1))


d = dice()
d.roll()