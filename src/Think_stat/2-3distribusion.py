#データのカウントを辞書型に格納し、データの頻度を確認する.
t = ["A","C","C","C","D","F","G","D","A","B","G","C","C"]
hist = {}
for x in t:
    hist[x] = hist.get(x,0) + 1 #値ごとにディクショナリに保存する.

n = float(len(t)) #データの個数.
pmf = {}
for x , freq in hist.items(): #辞書を一つづつとりだし確率を求める.
    pmf[x] = freq / n
print(hist)
print(pmf)