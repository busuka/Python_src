def checkio(text):
    low_texts = text.lower()
    alpha_texts = [x for x in low_texts if x.isalpha()]
    cnt_table = {x: alpha_texts.count(x) for x in alpha_texts}
    maxcnt_table = [x for x in cnt_table if cnt_table[x] == max(cnt_table.values())]
    return sorted(maxcnt_table)[0]

    # replace this for solution
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
