class TestingOne:

    def __init__(self):
        self.start = "7 4 5"
        self.a = "1 3 1"  # 1番目の横線 1番目の縦線の上から3cmの位置から、2番目の縦線の上から1cmの位置に線が引かれる
        self.b = "3 2 2"  # 2番目の横線 3番目の縦線の上から2cmの位置から、4番目の縦線の上から2cmの位置に線が引かれる
        self.c = "2 3 5"  # 3番目の横線 2番目の縦線の上から3cmの位置から、3番目の縦線の上から5cmの位置に線が引かれる
        self.d = "3 4 4"  # 4番目の横線 3番目の縦線の上から4cmの位置から、4番目の縦線の上から4cmの位置に線が引かれる
        self.e = "1 6 6"  # 5番目の横線 1番目の縦線の上から6cmの位置から、2番目の縦線の上から6cmの位置に線が引かれる
        self.l = [self.a, self.b, self.c, self.d, self.e]

    def insert(self, i):
        return self.l[i]