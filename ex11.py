#11) (din Teoria codurilor) Calculați distanța minimala a unui
#cod dat în (Fq)^n

import sys

def ver_baza(cuv, baza):

    for i in range(len(cuv)):
        if not cuv[i].isnumeric():
            return False
        elif int(cuv[i]) >= baza:
            return False
    return True

def cit_cod(n,M,q):
    cod = []
    print("Dați valorile codului:")
    for i in range(M):
        cuv = input()
        while len(cuv) != n or not(ver_baza(cuv, q)):
            cuv = input("Cuvântul nu are lungimea corectă sau nu este în baza corespunzătoare. Mai încercați: ")
        cod.append(cuv)

    print("Codul este: ", cod)
    return cod

def distanta_minimala(cod):
    dist=len(cod[0])

    for i in range(len(cod)):
        for j in range(i+1, len(cod)):
            d=sum(cod[i][k] != cod[j][k] for k in range(len(cod[i])))
            if dist > d:
                dist = d

    return dist

if __name__=="__main__":
    n = int(input("Lungimea codului: "))
    M = int(input("Numărul de cuvinte: "))
    q = int(input("Baza codului: "))

    while q >10:
        q=int(input("Baza 10 e maximul acceptat. Introduceți din nou: "))

    cod = cit_cod(n,M,q)
    print(distanta_minimala(cod))
