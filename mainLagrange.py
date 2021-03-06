from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import cmath
import time 
import accelCalcul as ac
frequence=int(1e5)
N=10*frequence
#Ce morceau de code est l'interpolation de Lagrange de la Green function
def mainLagrange(): 
    print("Entrer le début de l'intervalle")
    a=input()
    a=float(a)
    print("Entrer la fin de l'intervalle")
    b=input()
    b=float(b)
    print("Entrer l'ordre du polynome")
    n=input()
    n=int(n)
    print("Enter le paramètre k")
    k=input()
    k=float(k)

    rmin=1e-5

    exact=0
    
    #création de l'abscisse
    x=np.linspace(a,b,n+1, dtype=complex)
    
    
    #On a une singularité en 0 ainsi lorqu'on s'en approche on calcule exactement la fonction
    if a<rmin:
            x1=np.linspace(rmin,b,n+1, dtype=complex)
            x2=np.linspace(a,rmin,ceil(n/(b-a)*(rmin-a)))
            exact=green_functions.green2(k,x2) #partie exacte
            P=interpolation.lagrange(green_functions.green2,rmin,b,n,k) #partie interpolée
            Y=P(x)

            plt.plot(x1.real,Y.real)
            plt.plot(x1.real,Y.imag)
            plt.plot(x2.real, exact.real)
            plt.plot(x2.real, exact.imag)
    else:
             P=interpolation.lagrange(green_functions.green2,a,b,n,k)
             Y=P(x)
             
             
             plt.plot(x.real,Y.real,'b')
             plt.plot(x.real,Y.imag,'r')

    plt.show() 

def tempsLagrange(a,b,order,k): 
    rmin=1e-5

    exact=0
    #Création de l'abscisse
    x=np.linspace(a,b,N)
    
    #Même raison
    if a<rmin:
                 t1=time.time()
                 x1=np.linspace(rmin,b,N)
                 x2=np.linspace(a,rmin,ceil(N/10))
                 exact=green_functions.green2(k,x2) #partie exacte
                 P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                 Y=P(x)
                 
    else:
                 
                 P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 
                 t1=time.time()
                 Y=P(x)
                 t2=time.time()
                 
    temps2=ac.temps(t1,t2)
    return temps2
