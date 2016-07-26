# すごく良い例. text.replaceを難業も繰り返す場合は、正規表現を用いるか以下のように一度変換文字列を作成し、
# それをLoopで回すことでReplace繰り返していくとコードがスッキリする.
# ここでのポイントは,モン切り型にテキストをすぐにリストにするのでなく、一度全ての文字をリストとせず文字列として扱うことで,
# Replace分を容易に実装していることである.

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()

    for x in VOWELS:
        text = text.replace(x, "v")
    for y in CONSONANTS:
        text = text.replace(y, "c")

    words = text.split()
    print(text)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
