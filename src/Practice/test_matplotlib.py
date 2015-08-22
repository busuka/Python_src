#minicondaの動作確認
__author__ = 'Owner'

import os
import numpy as np
import matplotlib.pyplot as plt

print(plt.get_backend())
x = np.arange(-3, 3, 0.1)
y = np.sin(x)
plt.plot([1,2,3])
plt.plot(x, y)
plt.show()
