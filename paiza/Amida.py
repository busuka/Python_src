# coding: utf-8

# inputの代わり(テストコード)
from paiza import ImportCase
p = ImportCase.auto_input("amidatest.txt")


# initialize the vector of amidakuji
input_lines = p.__next__()
input_lines = list(map(int, input_lines.split(" ")))

amida_list = [["0" for i in range(input_lines[0]+1)] for j in range(input_lines[1])]
lengthOfline = input_lines[0]
numOfvline = input_lines[1]
numOfhline = input_lines[2]


# あみだくじ作成
for i in range(numOfhline):
    input_lines = p.__next__()
    input_lines = list(map(int, input_lines.split(" ")))
    row = input_lines[0] - 1
    col = input_lines[1]
    val = input_lines[2]
    amida_list[row][col] = val
    amida_list[row+1][val] = -col

# search for the answer
for p in range(numOfvline):
    row_p = p
    col_p = 1
    while col_p < (lengthOfline + 1):
        if type(amida_list[row_p][col_p]) == str:
            col_p += 1

        elif amida_list[row_p][col_p] >= 0:
            col_p = amida_list[row_p][col_p] + 1
            row_p += 1

        else:
            col_p = abs(amida_list[row_p][col_p]) + 1
            row_p -= 1

    if row_p == 0:
        ans = p + 1
        print(" 一番左をゴールと持つような線は左から" + str(ans) + "番目です.")
        break
