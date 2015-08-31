from Think_stat import Pmf

#学部長観点の算術平均
def dean(pmf):
    print(pmf.Mean())

#学生観点の算術平均
def stud(pmf):
    print(pmf.Mean())



#データの準備
d = {7:8, 12:8, 17:14, 22:4, 27: 6,32: 12, 37:8,  42:3, 47: 2}
classsize = Pmf.MakePmfFromDict(d)
dean(classsize)
stud(classsize)