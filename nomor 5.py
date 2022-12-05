from matplotlib import pyplot as plt
import random
import numpy as np

n = int(input("Masukkan jumlah bilangan yang ingin digenerate : "))
R = [random.uniform(0,1) for i in range(n)]
X = []

for r in R :
    if 0<r<= 0.5 :
        x = 6*r - 3
        X.append(x)
    else :
        x = np.sqrt(32*r - 16)
        X.append(x)

fig, ax = plt.subplots(figsize =(5, 3))
ax.hist(X)
plt.show()
