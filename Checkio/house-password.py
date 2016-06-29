def checkio(data):
    
    flgd = 0
    flgle = 0
    flglo = 0
    flgs = 0

    if len(data) >= 10:
        flgle = 1
    
    for x in data:
        if x.isdigit():
            flgd = 1

        if x.islower():
            flglo = 1

        if x.isupper():
            flgs = 1

    if flgle == 1 and flgd == 1 and flglo == 1 and flgs == 1:
        return True
    else:
        return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
