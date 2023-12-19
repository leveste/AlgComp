#2. Determinați grupul Galois asociat unui polinom de gradul 3
#sau 4. 

from sympy import *
import sympy as sp
import sys

def cit_polin(n):
    x = sp.Symbol('x')
    arr = []
    print("Dați valorile polinomului:")
    for i in range(n+1):
        k = int(input())
        arr.append(k)

    p =Poly(arr,x)
    return p

def calc_rezultanta(polin_coeff, polin_der_coef, n):
    m = 2*n - 1 #calculam ordinul rezultantei
    rez = [] #inițializăm rezultanta

    for i in range(n-1): #adăugăm coeficienții polinomului la rezultantă
        a = [0]*m
        k=0
        for j in range(m):
            if j>=len(polin_coeff):
                break
            else:
                a[j+i] = polin_coeff[k]
            k += 1
        rez.append(a)

    off = 0
    for i in range(n-1,m):
        a = [0]*m
        k=0
        for j in range(m):
            if j>=len(polin_der_coef):
                break
            else:
                a[j+off] = polin_der_coef[k]
            k += 1
        off += 1
        rez.append(a)

    print("\nRezultanta este:\n", '\n'.join(['\t'.join([str(val) for val in linie]) for linie in rez]))

    det = sp.Matrix(rez).det()
    print("Determinantul rezultantei este: ", det)
    return det * (-1)**(n*(n-1)/2) * polin_coeff[0]

def det_gr_Galois(polin, n):
    der = Poly(Derivative(polin,x).doit())
    polin_coeff = polin.all_coeffs()
    polin_der_coef = der.all_coeffs()

    r = calc_rezultanta(polin_coeff, polin_der_coef, n)
    if r>0:
        rad = r**0.5

    if r>=0 and rad**2 == r:
        print("Grupul Galois este grupul alternant A3!")
    else:
        print("Grupul Galois este simetric S3!")

    return

if __name__=="__main__":
    n = int(input("Introduceți gradul polinomului(3 sau 4): "))
    x = sp.Symbol('x')
    if not n in [3,4]:
        print("Valoarea dată nu e validă!")
        sys.exit(0)
    polin = cit_polin(n)

    print("Polinomul este: ", polin)

    det_gr_Galois(polin, n)
