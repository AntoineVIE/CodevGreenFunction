from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import interval
import cmath

rmin=1e-5
a = 1
b=10
f=1e4
µr=1
epsilonr=1
k=10
c=1e8
n=ceil(c/(f*1e3*sqrt(µr*epsilonr)))

def varParametre():

    print("Quel paramètre voulez vous modifier ? :")
    print("Début de l'intervalle (1)")
    print("Fin de l'intervalle (2)")
    print("Fréquence (3)")
    print("Perméabilité relative magnétique relative (4)")
    print("Permittivité relative (5)")
    print("k (6)")
    
    param=input()
    param=float(param)
    
    if param==1:
        print("Entrer le début de l'intervalle")
        global a
        a=input()
        a=float(a)
    if param==2:
        print("Entrer la fin de l'intervalle")
        global b
        b=input()
        b=float(b)
    if param==3:
        print("Entrer la fréquence")
        global f
        f=input()
        f=float(f)
    if param==4:
        print("Entrer le paramètre de permeablité magnétique relative")
        global µr
        µr=input()
        µr=float(µr)
    if param==5:
        print("Entrer le paramètre de permittivité relative")
        global epsilonr
        epsilonr=input()
        epsilonr=float(epsilonr)
    if param==6:
        print("Enter le paramètre k")
        global k
        k=input()
        k=float(k)
    global n
    n=ceil((b-a)/(c/(f*1e3*sqrt(µr*epsilonr))))
    

def erreurParametre():
    print("Quelle erreur d'interpolation souhaitez-vous évaluer en fonction d'un parametre ?")
    print("Interpolation par polynôme de Lagrange (1)")
    print("Interpolation linéaire (2)")
    case=input()
    case=float(case)
    if case==1:
        varParametre()

        x=np.linspace(a,b,n)
        y=green_functions.green2(k,x)

        if a>rmin:
            Dreal=interpolation.erreurLagrange(y.real,a,b,n)
            Dim=interpolation.erreurLagrange(y.imag,a,b,n)

        else:
            Dreal=interpolation.erreurLagrange(y.real,rmin,b,n)
            Dim=interpolation.erreurLagrange(y.imag,rmin,b,n)

        
        erreur =sqrt(Dreal**2+Dim**2)
        print("L'erreur est de ", erreur)

    if case==2:
        varParametre()

        x=np.linspace(a,b,n)
        y=green_functions.green2(k,x)

        if a>rmin:
            Dreal=interpolation.erreurLinear(y.real,a,b,n)
            Dim=interpolation.erreurLinear(y.imag,a,b,n)

        else:
            Dreal=interpolation.erreurLinear(y.real,rmin,b,n)
            Dim=interpolation.erreurLinear(y.imag,rmin,b,n)


        
        erreur =sqrt(Dreal**2+Dim**2)
        print("L'erreur est de ", erreur)
