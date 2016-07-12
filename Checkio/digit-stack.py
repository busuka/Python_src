def digit_stack(commands):
    stack = [0 for x in range(len(commands))]
    head = 0
    sum = 0

    for order in commands:
        if order == "POP":
            head -= 1
            sum += stack[head]
        elif order == "PEEK":
            sum += stack[head - 1]
        else:
            stack[head] = int(order.split()[1])
            head += 1
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
