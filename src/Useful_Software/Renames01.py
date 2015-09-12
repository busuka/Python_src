# ファイル名を自動で変更するプログラム
# New_Nameに新しい名前を入力する.

import os
import glob

direct = "../../Desktop/unit/RenameTest/"
files = os.listdir(direct)
filess = files[1:]
filess = glob.glob("*.txt")

for x in filess:
    old_name = direct + x
    new_name = direct + x + "aaa"
    print(new_name)
    os.rename(old_name,new_name)

print(os.listdir(direct))