import random
import numpy as np

#Mendefinisikan fungsi lambda
def f_x(x) :
    if 0<=x<1 :
        return 30
    elif 1<=x<2 :
        return 45
    elif 2<=x<4 :
        return 20
    
def main() :
    #Jumlah bilangan yang ingin dibangkitkan
    n = 100
    #List untuk waktu kedatangan ke-i
    T_i = []
    #Menetapkan nilai maksimum dari fungsi lambda
    lmbd = 45
    #inisiasi nilai awal
    t = 0
    i = 0

    while i < n :
        R_a = random.uniform(0,1)
        E = -1/lmbd*np.log(1-R_a)
        t = t + E

        R_b = random.uniform(0,1)
        if R_b <= f_x(t)/lmbd :
            T_i.append(t) 
            i = i + 1
    
    print("============================== Pembangkitan waktu kedatangan 100-pertama ==============================")
    print(T_i)
    print(len(T_i))
if __name__=="__main__" :
    main()
