__author__ = 'Owner'

box = [1,2,3,4,5] #リスト

# 変数valにbox[０]から入り込む.
for val in box:
    print(val)

# print(box[box[0]])となっている.
#i = box[0]からだからそうなるのである,
#for i in box:
#    print(box[i])

box = {"Saga":"Kyusyu","Hyogo":"Kinki","Tokyo":"Kanto"}

#辞書にfor分を適用
for val in box:
    print(val) #キーが出力される.(しかし順番はバラバラであることに注意する)