import scipy as sp
import os
import matplotlib.pyplot as plt

#モデルのあてはめ
def error(f,x,y):
	return sp.sum((f(x)-y)**2)




data = sp.genfromtxt(os.path.expanduser("~/Python_src/src/MachineLearningSystem/exdata/ch01/data/web_traffic.tsv"))

print(data.shape)

print(data[:10])
x = data[:,0]
y = data[:,1]

#NAN値の処理

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
plt.scatter(x,y)

#fp1=切片と変数,residuals=残差 , full指定で残差等を取得可能, 1は次数を示す
fp1,residuals,rank,s,rcond = sp.polyfit(x,y,1,full=True)
f1 = sp.poly1d(fp1) #モデルパラメータからモデル関数の作成f1(x)= ~
print(error(f1,x,y))

print("Model parameters: %s", fp1)

#多項式のあてはめ
f2p = sp.polyfit(x,y,2)
print(f2p)


#Pyplotの設定
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hit/Hour")
plt.xticks([w*7*24 for w in range(10)],
    ["week %i" %w for w in range(10)])
fx = sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.legend(["d=%i" % f1.order],loc="upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()

#変化点を
inflection = 3.5*7*24