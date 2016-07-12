def checkio(words_set):
    word = list(words_set)[0]
    for x in list(words_set)[1:]:
        if word.startswith(x) or word.endswith(x):
            pass
        else:
            return False

    print(words_set)

    if len(words_set) == 0:
        return False
    else:
        return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
