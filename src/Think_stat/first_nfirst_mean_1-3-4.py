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
def mean(data,value):
    sums = 0
    for i in data:
        sums = sums + value
    return sums / len(data)

#レコードを読み込んでオブジェクトとする.
table = survey2.Pregnancies()
table.ReadRecords()
table_record = table.records

first  = survey2.Pregnancies()
nfirst = survey2.Pregnancies()
births = distributions()
first_record =first.records
nfirst_record = nfirst.records
mean(first_record,first_record.prglength)
mean(nfirst_record)