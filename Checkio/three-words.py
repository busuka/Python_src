def checkio(words):

    n = 0
    s = words.split(" ")
    for x in s:
        if not x.isalpha():
            n = 0
        else:
            n += 1
        if n >= 3:
            return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"