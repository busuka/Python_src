#たくさんのフォルダを作成する.

import os
print(os.getcwd())                 #カレントフォルダを表示

#新フォルダを自動で100個作る
for x in range(1,101):
    f_names = str(x)
    os.mkdir(os.getcwd() + "/" + f_names)
