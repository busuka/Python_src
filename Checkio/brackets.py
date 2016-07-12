# Point
# popができなかった場合も実装している.(いきなり'}'や')'が与えられた場合)
# リストが空であればFalseを返すのをReturnで利用している.


def checkio(expression):
    ex_dict = {"}": "{", ")": "(", "]": "["}
    ex_stack = []
    for e in expression:
        if e in ['(', '{', '[']:
            ex_stack.append(e)
        if e in [')', '}', ']']:
            try:
                popv = ex_stack.pop()
                if ex_dict[e] != popv:
                    return False
            except:
                return False
    return bool(not ex_stack)




# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
