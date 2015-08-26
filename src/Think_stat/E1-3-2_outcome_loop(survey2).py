from Think_stat import survey2 #この文言からカレントディレクトリがsrcでありfrom文で取ってきている形だとわかる.
table = survey2.Pregnancies()  #空のtableはPregnancies型なのでlenやappendのような初期メソッドではないので注意.
table.ReadRecords()            #tableのメソッドであるファイルからデータの読み込みを行っている
table_record = table.records   #tableの各レコードが格納されている.recordsで読み込んだファイルを書き出し(List型)
a = 0
for i in table_record:
    if i.outcome == 1:
        a = a + 1
print("出産した子どもの数 :",a)