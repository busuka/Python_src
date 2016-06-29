# This game is so good encounter of what class is .


class Ways():
    # class: choice that member decide
    def __init__(self):
        self.choice = 0

    def decidechoice(self):
        self.choice = input()

    def __privatechoice(self):  # メソッド名にアンダーバーをつけるとプライベートメソッド（っぽくなる)
        pass


class Rules():
    judgement = 0  # shared by All instance : クラス変数（インスタンスごとに固有の値を持たないこと）

    def __init__(self):
        self.lock = 0  # unique to each instance : インスタンス変数 （インスタンスごとに持つ固有の値)
        self.x = 1
        self.paper = 2


if __name__ == '__main__':
    print("---じゃんけんゲーム---")
    A_way = Ways()
    B_way = Ways()

    print("Aさん、どの手を出しますか? (0:グー,1:チョキ,2:パー) ")
    A_way.decidechoice()

    print("Bさん、どの手を出しますか? (0:グー,1:チョキ,2:パー) ")
    B_way.decidechoice()
