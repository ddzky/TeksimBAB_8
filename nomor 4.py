import random
import numpy as np
import statistics

n = int(input("Masukkan jumlah bilangan yang ingin digenerate : "))
R = [random.uniform(0,1) for i in range(n)]
true_mean = 4
X = []

for r in R :
    x = 10 - np.sqrt(81-81*r)
    X.append(x)
sample_mean = statistics.mean(X)
print(f"True Mean : {true_mean}")
print(f"Sample Mean : {sample_mean}")