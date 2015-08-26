from Think_stat import survey2
def distributions():
    #元のデータを１人目と２人目以降とに分ける.
    first  = survey2.Pregnancies()
    nfirst = survey2.Pregnancies()
    for i in table_record:
        if i.outcome != 1:
            continue

        if i.birthord  == 1:
            first.AddRecord(i)
        else:
            nfirst.AddRecord(i)
    return(first , nfirst) # #
def mean(data):
    #平均を求める.
    sums = 0
    for i in data:
        sums = sums + i.prglength
    return sums / len(data)

#レコードを読み込んでオブジェクトとする.
table = survey2.Pregnancies()
table.ReadRecords()
table_record = table.records

births = distributions()
first_rec  = births[0].records
nfirst_rec = births[1].records
mfr  = mean(first_rec)
mnfr = mean(nfirst_rec)

print ("First babies", mfr)
print ('Others', mnfr)
print ('Difference in days', (mfr - mnfr) * 7.0)