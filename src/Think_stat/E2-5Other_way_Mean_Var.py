from Think_stat import Pmf

def PmfMean(pmf,hist):
    """hist.Values()で度数表（辞書）をキーで返す,それをリスト化
       キーリストをforで回し,キーと確率をかけて算術平均を求める.
     　"""
    return(sum([val * pmf.Prob(val) for val in list(hist.Values())]))

def PmfVar(pmf,hist):
    means = PmfMean(pmf,hist)
    residuals = [(pmf.Prob(val) * ((val - means)**2)) for val in list(hist.Values())]
    return sum(residuals)

hist = Pmf.MakeHistFromList([1,2,2,3,4,2])
pmf = Pmf.MakePmfFromList([1,2,2,3,4,2])
print("pmf平均 : " ,PmfMean(pmf,hist))
print("pmf分散 : " ,PmfVar(pmf,hist) )



