import sklearn.datasets
import numpy as np
from matplotlib import pyplot as plt

#データの入力
boston = sklearn.datasets.load_boston()
x = boston.data[:,5]
y = boston.target

#散布図の描画
plt.scatter(x,y,color="r")

#Hypothesisと導関数を返す
def model1(x,t0,t1):
	return t0 + t1 * x

#Hypothesisの導関数(偏微分した結果)
#def model1_prime(x,kind_theta,t0,t1):
#	    diff(t0 + t1 * x ,kind_theta)

#Cost Function
def costfunc(theta1,theta2):
	m = x.size
	p_costs = 0
	for a in x:
		p_costs = p_costs + (model1(a) - y[x.shape])^2
	costs = p_costs / (2*m)

#最急降下法
def GradientDescent():
	
	iterationmax = 100
	learningrate = 0.5


	init_value = 100
	theta0 = 100
	theta1 = 100
	print(costfunc(theta0 , theta1))
	
#	for i in range(iterationmax):
#		#最急降下法計算式
#		theta0 = learningrate * model1_prime(i , "theta0")
#		theta1 = learningrate * model1_prime(i , "theta1")
#		print(costfunc(theta0,theta1))


