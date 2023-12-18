#2. Determinați grupul Galois asociat unui polinom de gradul 3
#sau 4. 

from sympy import *
import sympy as sp
import sys

def cit_polin(n):
    x = sp.Symbol('x')
    arr = []
    print("Dați valorile polinomului:")
    for i in range(n):
        k = int(input())
        arr.append(k)

    p =Poly(arr,x)
    return p

def det_gr_Galois(polin, n):

    return

if __name__=="__main__":
    n = int(input("Introduceți gradul polinomului(3 sau 4): "))
    if not n in [3,4]:
        print("Valoarea dată nu e validă!")
        sys.exit(0)
    polin = cit_polin(n)

    print("")
