import random
import numpy as np

n = int(input("Masukkan jumlah bilangan yang ingin digenerate : "))
R  = [random.uniform(0,1) for i in range(n)]
X = []

for r in R :
    if 0<r<=0.5 :
        x = 0.5*np.log(2*r)
        X.append(x)
    else :
        x = -0.5*np.log(2-2*r)
        X.append(x)
print(X)