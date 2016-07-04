"""

==概要==

txtファイルからデータを受け取り、paizaのように1行ずつinputデータを読み込むためのPythonモジュール


==使い方==

1.txtファイルでケースを作成する.
2.ソースコードに以下の2行を追加する.

from paiza import ImportCase
p = ImportCase.auto_input(filepath) <= ファイルパスを入力する.

=> pはジェネレータ関数であり、__next__メソッドを実行することでpaizaのinput()と同じ動作をする.
=> つまり、p.__next__()  ==  input()

"""


def _getinputdata(text):
    # txtデータを1行ずつ取り込みリストで返す変数
    f_list = []
    with open(text, "r") as f:
        for line in f:
            f_list.append(line)
    return f_list


def _delenter(inputdata):
    # txtファイルの\nを削除したリストを返す関数
    return_list = []
    for strings in inputdata:
        del_list = [char for char in strings if char != "\n"]
        return_list.append("".join(del_list))
    return return_list


def _makegen(inputdata):
    # ジェネレータ関数. paizaのようにinputデータ（ここではリスト)を1つずつ取り出すための関数.
    for rows in inputdata:
        yield rows


def auto_input(filepath):
    # メイン処理1. 変形したいtxtファイルを指定してジェネレータ関数を返す関数.
    divlist = _getinputdata(filepath)
    paiza_list = _delenter(divlist)
    return _makegen(paiza_list)


def autoinput_returnlist(filepath):
    # メイン処理2. 変形したいtxtファイルを指定してリスト形式で返す関数.
    divlist = _getinputdata(filepath)
    paiza_list = _delenter(divlist)
    GeneList = _makegen(paiza_list)
    return_list = []
    for x in GeneList:
        return_list.append(x)
    print("Warning:返される値はstr型リストなので注意!")
    return return_list