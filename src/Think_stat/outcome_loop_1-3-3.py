from Think_stat import survey2
def distributions():
    for i in table_record:
        if i.outcome != 1:
            continue

        if i.birthord  == 1:
            first.AddRecord(i)
        else:
            nfirst.AddRecord(i)
    return(first , nfirst)

#レコードを読み込んでオブジェクトとする.
table = survey2.Pregnancies() #空のタプルを作成
table.ReadRecords() #全データの読み込み
table_record = table.records #列の取得

first  = survey2.Pregnancies()
nfirst = survey2.Pregnancies()
births = distributions()
len(births[0])
len(births[1])