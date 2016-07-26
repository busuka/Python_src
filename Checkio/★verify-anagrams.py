def verify_anagrams(first_word, second_word):
    f = [x.lower() for x in first_word if x.isalpha()]
    s = [x.lower() for x in second_word if x.isalpha()]
    for x in s:

        try: f.remove(x)
        except: return False

    if len(f) == 0:
        return True
    else:
        return False

def verify_anagramsNO1(a,b):
    return sorted(a.lower().replace(' ','')) == sorted(b.lower().replace(' ',''))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
