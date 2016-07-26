# 初のModerateクリア.
# 1回目のAlreadyペンギンの処理のループは1回１回条件分岐をしなくても良い気がする.
# numberから一気にAlreadyPeigenos匹分をひいて0以下だったらreturn AlreadyPegionsしてしまえばいい.

def checkio(number):

    alreadyPigeons = 0
    newPegeons = (x for x in range(100000) if x != 0)

    while number > 0:

        for times in range(alreadyPigeons):
            number -= 1

            if bool(not number):
                return alreadyPigeons

        for times in range(newPegeons.__next__()):

            number -= 1
            alreadyPigeons += 1

            if bool(not number):
                return alreadyPigeons

    return alreadyPigeons

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"