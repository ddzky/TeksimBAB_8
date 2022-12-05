import random
import numpy as np
import statistics

n = int(input("Masukkan jumlah bilangan yang ingin digenerate : "))
R = [random.uniform(0,1) for i in range(n)]
true_mean = 5
X = []

for r in R :
    if 0<r<= 1/3 :
        x = 1 + np.sqrt(27*r)
        X.append(x)
    else :
        x = 10 - np.sqrt(54-54*r)
        X.append(x)
sample_mean = statistics.mean(X)
print(f"True Mean : {true_mean}")
print(f"Sample Mean : {sample_mean}")