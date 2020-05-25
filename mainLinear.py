from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import cmath
import accelCalcul as ac
import time


def mainLinear(): 
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

    exact=0
    x=np.linspace(a,b,n+1, dtype=complex)
    
    
    if a<rmin:
            x1=np.linspace(rmin,b,n+1, dtype=complex)
            x2=np.linspace(a,rmin,ceil(n/(b-a)*(rmin-a)))
            exact=green_functions.green2(k,x2)
            P=interpolation.linear(green_functions.green2,rmin,b,n,k)
            Y=P(x)
            plt.plot(x1.real,Y.real)
            plt.plot(x1.real,Y.imag)
        
            plt.plot(x2.real, exact.real)
            plt.plot(x2.real, exact.imag)
    else:
             P=interpolation.linear(green_functions.green2,a,b,n,k)
             Y=P(x)
             plt.plot(x.real,Y.real,'b')
         
             plt.plot(x.real,Y.imag,'r')
        
    plt.show() 

def tempsLinear(a,b,n,k): 
    rmin=1e-5

    exact=0
    #Création de l'abscisse
    x=np.linspace(a,b,n+1, dtype=complex)
    
    #Même raison
    if a<rmin:
            x1=np.linspace(rmin,b,n+1, dtype=complex)
            x2=np.linspace(a,rmin,ceil(n/(b-a)*(rmin-a)))
            t1=time.time()
            exact=green_functions.green2(k,x2) #partie exacte
            P=interpolation.linear(green_functions.green2,rmin,b,n,k) #partie interpolée
            Y=P(x)
            t2=time.time()
            temps=ac.temps(t1,t2)

    else:
             t1=time.time()
             P=interpolation.linear(green_functions.green2,a,b,n,k)
             Y=P(x)
             t2=time.time()
             temps=ac.temps(t1,t2)
    return temps        
