from Think_stat import Pmf
def PmfMean():
    pmf = Pmf.MakePmfFromList([1,2,2,3,4,2])
    print(pmf.Prob(2))

PmfMean()
