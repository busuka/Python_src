# ☆ Queueの使い方(クラスやライブラリを用いずに表現してみる.)

def letter_queue(commands):
    queue = []
    for cs in commands:
        command = cs.split()

        if command[0] == "POP" and queue:
            queue.pop(0)

        if command[0] == "PUSH":
            queue.append(command[1])

    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
