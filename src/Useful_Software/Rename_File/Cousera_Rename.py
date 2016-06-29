# Courseraファイル名を自動で変更するプログラム
# NameをSection1_Titleに変更→フォルダ整理をする
# pattern = re.compile("^/d+") #検索したいパターン
# x = 検索文字列
# pattern.match(x) = 先頭からマッチ確認 pattern.search => 全文字列を走査
# /d 数字
# +  1回以上の繰り返し


import os
import re

direct = "../../Desktop/Cousera/Machine_Learning"
FileFold = os.listdir(direct)
FileNameList = FileFold[1:]

for x in FileNameList:
    old_name = direct + x
    new_name = direct + "Section" + "aaa"
    print(new_name)
    os.rename(old_name,new_name)