import scipy as sp
data = sp.genformtxt("web_traffic.tsv",delimiter="/t")

print(data[1:10])
x = data[:,0]
y = data[:,1]

