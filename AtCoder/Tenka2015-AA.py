# http://tenka1.klab.jp/2015/explain/quala_a.html

def diceNumber(n, s=""):

    s += str(n)

    if n - 1 > 0 and len(s) < 5:
        return diceNumber(n - 1, s)

    if n + 1 < 6 and len(s) < 5:
        return diceNumber(n + 1, s)

    return s

if __name__ == "__main__":
    print(diceNumber(6))
