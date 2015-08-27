class foods():
    def __init__(self,ham,egg): #foodsクラスをインスタンス生成の際に呼び出すと__init__メソッドが呼び出される.（初期化をする)
        self.ham = ham
        self.egg = egg
        print(self.ham,self,egg)

food = foods(100,200)
