from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import cmath

def erreurLinear():
    print("Entrer le début de l'intervalle")
    a=input()
    a=float(a)
    print("Entrer la fin de l'intervalle")
    b=input()
    b=float(b)
    print("Entrer le nombre de points")
    n=input()
    n=int(n)
    print("Enter le paramètre k")
    k=input()
    k=float(k)

    rmin=1e-5

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
    

def erreurLinearParametre(a,b,n,k):
  
    rmin=1e-5

    x=np.linspace(a,b,n)
    y=green_functions.green2(k,x)

    if a>rmin:
         Dreal=interpolation.erreurLinear(y.real,a,b,n)
         Dim=interpolation.erreurLinear(y.imag,a,b,n)

    else:
         Dreal=interpolation.erreurLinear(y.real,rmin,b,n)
         Dim=interpolation.erreurLinear(y.imag,rmin,b,n)

    erreur =sqrt(Dreal**2+Dim**2)
    
    print("L'erreur est de : ", erreur)
    return erreur
