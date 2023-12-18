#1. Calculați valorile proprii asociate unei matrici de ordinul 2
#sau 3, afișând polinomul caracteristic asociat. 

import numpy as np
import sys


def cit_mat(n): #citirea matricei
    mat = [] #inițializăm matricea

    print("Introduceți valorile matricii!")
    for linie in range(n):
        print("Rândul: ", linie+1)
        a = []
        for col in range(n):
            a.append(int(input()))
        mat.append(a)

    return mat

def calc_val_proprii(mat):
    return np.linalg.eigvals(mat)

if __name__ == "__main__":
    n=int(input("Introduceți mărimea matricii: "))

    if not n in [2,3] or not(isinstance(n, int)):
        print("Mărimea matricii nu e validă. Matricea trebuie să fie de ordinul 2 sau 3.")
        sys.exit(0)

    mat = cit_mat(n)


    print("\nMatricea este:\n", '\n'.join(['\t'.join([str(val) for val in linie]) for linie in mat]))

    print("Valorile proprii sunt: ", calc_val_proprii(mat))
