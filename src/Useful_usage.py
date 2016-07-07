# Ctlr + del で単語消し

# 16進数→10進数
print(0xAAA)

# 文字列を複製
s = "abc"
print(s * 3)  # => "abcabcabc"

# 重複する文字列を削除
s = "letter"
print(set(s))  # => {"r","l","e","t"} ただし順番は変わってしまう.

# 順序が変わってしまう辞書型を順序付き辞書にする.
from collections import OrderedDict
eg_dict = dict(a=3, b=2, c=1)
print(eg_dict)
print(OrderedDict(sorted(eg_dict.items(), key=lambda t: t[1])))  # 値ごとでソートして返す辞書


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

# 文字列カウントにはカウンター関数も使える
from collections import Counter
breakfast = ['spam', 'eggs', 'spam']
breakfast_cnt = Counter(breakfast)
print(breakfast_cnt)

# 1から5までの奇数リストを作成（条件付きリスト内包表現を用いて）
odd_list = [num for num in range(1, 6) if num % 2 == 1]
print(odd_list)

# 1から5までの奇数リストを作成（スライスを用いて）
odd_list = list(range(1, 6))[::2]
print(odd_list)

# 末尾の文字に一致するかを検証する
print("abcdef".endswith("def"))


# リストの中身に対して個々に関数(処理式)を適用する.
# 以下の2つの方法がある.(mapを使用する,リスト内包型)
# lambda式はリスト（シーケンス)でなくても利用することが出来る.

strings_list = ["left", "fight", "left"]
print(list(map(lambda v: v.replace("left", "right"), strings_list)))
print([v.replace("left", "right") for v in strings_list])

# リストから条件に一致する式を適用する
# 以下の2つの方法がある（filterを使用する,リスト内包型)

strings_list = ["left", "fight", "left"]
print(list(filter(lambda v : v == "left", strings_list)))
strings_list = ["left", "fight", "left"]
print(list(filter(lambda v : v == "left", strings_list)))
print([v for v in strings_list if v == "left"])

# 引数の要素が全てTrueならTrueを返すAll
# 引数の要素が一つでもTrueならTrueを返すany
print(all(x % 2 == 0 for x in [1, 2, 3]))
print(any(x % 2 == 0 for x in [1, 2, 3]))

# itertoolsを用いることでイテレータを自由自在に操れる.
import itertools

# itertool.chain:リストを合体してあたかも同じイテラブルかのように動作させる
print([items for items in itertools.chain([1, 2], ['a', 'b'])])

# itertool.accumulate:要素を一つにまとめた値を計算する.デフォルトでは和.
# 第2引数には関数を受け付ける.例えばlambdaでは総乗を計算する関数を適用してみる.
print([items for items in itertools.accumulate([1,2,3,4,5])])
print([items for items in itertools.accumulate([1,2,3,4,5], lambda a, b: a * b)])