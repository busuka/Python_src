#This code is made by me , but sample answer is absolute better...
#sample code = risk.py(../download/thinkstat/)

from Think_stat import survey2
from Think_stat import Pmf

def Reading_Data():
    table = survey2.Pregnancies()
    table.ReadRecords()
    return table.records
def distributions(table_records):
    #元のデータを１人目と２人目以降とに分ける.
    first  = survey2.Pregnancies()
    nfirst = survey2.Pregnancies()
    for i in table_records:
        if i.outcome != 1:
            continue

        if i.birthord  == 1:
            first.AddRecord(i)
        else:
            nfirst.AddRecord(i)
    return(first , nfirst)
def Convert_Prglength_Lists(lists):
    tmplist = []
    for val in lists:
        tmplist.append(val.prglength)
    return tmplist
def ProbEarly(hist,pmf):
    sum_pmf = 0
    tmplist = list(hist.Values())
    for val in tmplist:
        if val <= 37:
            sum_pmf = sum_pmf + pmf.Prob(val)
    return sum_pmf
def ProbOnTime(hist,pmf):
    sum_pmf = 0
    tmplist = list(hist.Values())
    for val in tmplist:
        if val >= 38 and val <=40 :
            sum_pmf = sum_pmf + pmf.Prob(val)
    return sum_pmf
def Problate(hist,pmf):
    sum_pmf = 0
    tmplist = list(hist.Values())
    for val in tmplist:
        if val >= 41:
            sum_pmf = sum_pmf + pmf.Prob(val)
    return sum_pmf


#データを読み込んで第一子と第二子に分ける.
table_record = Reading_Data()
births = distributions(table_record)

#各データから妊娠期間をリストで返す.
lfst_prg = Convert_Prglength_Lists(births[0].records)
lnfst_prg = Convert_Prglength_Lists(births[1].records)

#各妊娠期間リストをHistとPmfに適用してインスタンス化する.
first_hist = Pmf.MakeHistFromList(lfst_prg)
first_pmf = Pmf.MakePmfFromList(lfst_prg)
nfirst_hist = Pmf.MakeHistFromList(lnfst_prg)
nfirst_pmf = Pmf.MakePmfFromList(lnfst_prg)

#条件付き確率:第一子のみのデータで各期間ごとの確率を算出
print("第一子PMFのみ早産",ProbEarly(first_hist,first_pmf))
print("第一子PMFのみ標準",ProbOnTime(first_hist,first_pmf))
print("第一子PMFのみ遅産",Problate(first_hist,first_pmf))

#条件付き確率:第二子以降のみのデータで各期間ごとの確率を算出
print("第二子以降PMFのみ早産",ProbEarly(nfirst_hist,nfirst_pmf))
print("第二子以降PMFのみ標準",ProbOnTime(nfirst_hist,nfirst_pmf))
print("第二子以降PMFのみ遅産",Problate(nfirst_hist,nfirst_pmf))

#following codes are not correct.
print("PMF早産",ProbEarly(first_hist,first_pmf)+ProbEarly(nfirst_hist,nfirst_pmf))
print("PMF標準",ProbOnTime(first_hist,first_pmf)+ProbOnTime(nfirst_hist,nfirst_pmf))
print("PMF遅産",Problate(first_hist,first_pmf)+Problate(nfirst_hist,nfirst_pmf))





