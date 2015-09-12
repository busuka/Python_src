#たくさんのファイルを作成する.

import os
os.getcwd()                 #カレントフォルダを表示
os.chdir("./MakeManyFiles") #フォルダを移動して新ファイルを作るフォルダに指定

#UNIXのdateを使い新ファイルを自動で100個作る
for x in range(1,101):
    f_names = str(x)
    p_names = ".txt"
    os.system("date > " + f_names + p_names)
