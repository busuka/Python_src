# http://abc021.contest.atcoder.jp/tasks/abc021_a

def squeres(v,rlt=""):
    if v < 0: return
    if v == 0: return rlt
    for x in [8, 4, 2, 1]:
        rlt += str(x)
        squeres(v - x,rlt)
        if v == 0: return rlt

def OnlyOne(i):
    print(i)
    for x in range(i):
        print(1)


if __name__ == "__main__":
    OnlyOne(4)