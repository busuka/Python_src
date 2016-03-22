from sklearn.datasets import load_boston
import numpy as np
from matplotlib import pyplot as plt

boston = load_boston()

#まずはプロットをしてみる（散布図)
#plt.scatter(boston.data[:,5],boston.target,color="r")

x = boston.data[:,5]
x = np.array([[v] for v in x])

y = boston.target
slope,_,_,_ = np.linalg.lstsq(x,y)