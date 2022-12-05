import random
import numpy as np
import statistics

n = int(input("Masukkan jumlah bilangan yang ingin digenerate : "))
R = [random.uniform(0,1) for i in range(n)]
true_mean = 11/3
X = []

for r in R :
    if 0<r<=0.25 :
        x = 2 + 2*np.sqrt(r)
        X.append(x)
    else :
        x = 6 - np.sqrt(12-12*r)
        X.append(x)
sample_mean = statistics.mean(X)
print(f"True Mean : {true_mean}")
print(f"Sample Mean : {sample_mean}")