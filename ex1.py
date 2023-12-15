#1) Verificați dacă inversa unei matrici triunghiulare este tot
#triunghiulară. 

import numpy as np
import sys

def cit_mat(n): #citirea matricei
    mat = [] #inițializăm matricea

    print("Introduceți valorile matricii!")
    for linie in range(n):
        a = []
        for col in range(n):
            a.append(int(input()))
        mat.append(a)

    return mat

def ver_triung_sup(mat): #verifică dacă matricea este triunghiulară superior
    sf = True
    sup = np.triu(mat, 1) #aflăm triunghiul de sub diagonaleo matricii
    if np.count_nonzero(sup) != 0: #verificăm dacă triunghiul de sub digonal este doar 0
        sf = False

    return sf

def ver_triung_inf(mat): #verifică dacă matricea este triunghiulară inferior
    sf = True
    inf = np.tril(mat, -1) #aflăm triunghiul de deaspupra diagonaleo matricii
    if np.count_nonzero(inf) != 0: #verificăm dacă triunghiul de deasupra digonalei este doar 0
        sf = False

    return sf

def inv_matrice(mat): #inversează matricea
    return np.linalg.inv(mat)

if __name__ == "__main__":
    n=int(input("Introduceți mărimea matricii: "))

    if (n<=1) or not(isinstance(n, int)):
        print("Mărimea matricii nu e validă. Trebuie să fie un număr natural, mai mare de 1.")
        sys.exit(0)

    mat = cit_mat(n)


    print("\nMatricea este:\n", '\n'.join(['\t'.join([str(val) for val in linie]) for linie in mat]))

    if not(ver_triung_sup(mat)) and not(ver_triung_inf(mat)):
        print("Matricea dată nu este triunghiulară!")
        sys.exit(0)


    invMat = inv_matrice(mat)
    print("\nInversa matricii este:\n", '\n'.join(['\t'.join([str(round(val,2)) for val in linie]) for linie in inv_matrice(invMat)]))

    if ver_triung_inf(invMat) == True:
        print("Matricea inversă este triunghiulară inferior!")
    elif ver_triung_sup(invMat) == True:
        print("Matricea inversă este triunghiulară superior!")
