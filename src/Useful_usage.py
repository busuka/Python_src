# 文字列を複製
s = "abc"
print(s * 3)  # => "abcabcabc"

# 重複する文字列を削除
s = "letter"
print(set(s))  # => {"r","l","e","t"} ただし順番は変わってしまう.

# !注意 リストのコピーはポインタのコピーである
l = ["a", "b", "c"]
lc = l
l[0] = "d"
print(lc)  # lc = ["d","b","c"]

# リストのコピーの解決方法
l = ["a", "b", "c"]
lc = l.copy()
l[0] = "d"
print(lc)  # lc = ["a","b","c"]

# 辞書包括表記(文字列に含まれる文字のカウントをしたい)
l = "letter"
letter_count = {x: l.count(x) for x in l}
print(letter_count)  # letter_count = {'l': 1, 't': 2, 'e': 2, 'r': 1}

# カウンター関数も使える
from collections import Counter
breakfast = ['spam','eggs','spam']
breakfast_cnt = Counter(breakfast)
print(breakfast_cnt)

# 1から5までの奇数リストを作成（条件付きリスト内包表現を用いて）
odd_list = [num for num in range(1, 6) if num % 2 == 1]
print(odd_list)

# 1から5までの奇数リストを作成（スライスを用いて）
odd_list = list(range(1, 6))[::2]
print(odd_list)

