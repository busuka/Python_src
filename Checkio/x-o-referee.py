def checkio(game_result):
    v = game_result

    # 横
    for i in range(3):
        c = v[i][0]
        cnt = 1
        if c == ".":
            continue

        for j in range(1,3):
            if c == v[i][j]:
                cnt += 1
        if cnt == 3:
            return c

    # 縦
    for j in range(3):
        c = v[0][j]
        cnt = 1
        if c == ".":
            continue

        for i in range(1,3):
            if c == v[i][j]:
                cnt += 1
        if cnt == 3:
            return c

    # 右斜め
    c = v[0][0]
    cnt = 1
    for i in range(1, 3):
        if c == v[i][i]:
            cnt += 1

    if cnt == 3 and c != ".":
        return c

    # 左斜め
    c = v[2][0]
    cnt = 1
    i = 1
    j = 1
    for x in range(1,3):
        if c == v[i][j]:
            cnt += 1
        i -= 1
        j += 1

    if cnt == 3 and c != ".":
        return c

    else:
        return "D"

def checkio2(game_result):
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != '.':
        return game_result[0][0]

    if game_result[0][2] == game_result[1][1] == game_result[2][0] != '.':
        return game_result[0][2]

    for x in range(3):
        if game_result[x][0] == game_result[x][1] == game_result[x][2] != '.':
            return game_result[x][0]

    for x in range(3):
        if game_result[0][x] == game_result[1][x] == game_result[2][x] != '.':
            return game_result[0][x]

    return "D"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

