from Think_stat import survey2
from Think_stat import Cdf
from Think_stat import Pmf
from Think_stat import myplot

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

#レコードを読み込んでオブジェクトとする.
table = survey2.Pregnancies()
table.ReadRecords()
table_record = table.records

births = distributions()
first_rec  = births[0].records
nfirst_rec = births[1].records

firsts= []
nfirsts = []

for i in first_rec:
    firsts.append(i.birthwgt_oz)

for p in nfirst_rec:
    nfirsts.append(p.birthwgt_oz)

first_cdf = Cdf.MakeCdfFromList(firsts)
nfirst_cdf = Cdf.MakeCdfFromList(nfirsts)
