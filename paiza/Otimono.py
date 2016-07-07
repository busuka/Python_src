# とりあえずクラスを用いて実装すべきでした。

# inputの代わり(テストコード)
from paiza import ImportCase
p = ImportCase.auto_input("otimono2.txt")
input_lines = p.__next__()
input_lines = list(map(int, input_lines.split(" ")))


fields = []
for y in range(input_lines[0]):
    fields.append(["." for x in range(input_lines[1])])

numRow = input_lines[0]
numCol = input_lines[1]
numLoop = input_lines[2]


def searchRow(StartPos, Putpos):
    # 行の走査
    while StartPos < numRow - 1:
        if fields[StartPos][putPos] == "#":
            StartPos -= 1
            break
        StartPos += 1

    for x in range(colPos):
        if fields[StartPos][putPos + x] == "#":
            searchRow(StartPos)
    return StartPos


def searchCol(StartPos, Putpos):

    # 列の走査
    for y in range(colPos):
        if fields[StartPos][Putpos + y] == "#":
            return searchCol(StartPos - 1, Putpos)

    return StartPos


for n in range(numLoop):
    input_lines = p.__next__()
    input_lines = list(map(int, input_lines.split(" ")))
    rowPos = input_lines[0]
    colPos = input_lines[1]
    putPos = input_lines[2]
    StartPos = 0
    print(rowPos, colPos, putPos)

    # 走査
    StartPos = searchRow(StartPos, putPos)
    StartPos = searchCol(StartPos, putPos)

    # テトリミノを置く.
    for row in range(rowPos):
        for col in range(colPos):
            rows = StartPos - row
            cols = putPos + col
            fields[rows][cols] = "#"


#出力
for out in fields:
    print("".join(out))