from Think_stat import Pmf
hist = Pmf.MakeHistFromList(["A","B","B","C","E"])
print(hist.Freq("B"))
print(hist.Values())
print(hist.Mode())
print(hist.AllModes)
"""
    演習問題2-3
    def Mode(self):
        "This method is to calculate mode of x"
        return max(self.d.values())
"""

"""
.keysの返り値はlistではない.
辞書型のキー指定でリストやタプルは使えない
"""

