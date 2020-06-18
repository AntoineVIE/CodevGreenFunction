from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import cmath
import accelCalcul as ac
import time
frequence=int(1e3)
N=100*frequence

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
             P=interpolation.interpolLinear(green_functions.green2,a,b,n,k)
             Y=P(x)
             plt.plot(x.real,Y.real,'b')
         
             plt.plot(x.real,Y.imag,'r')
        
    plt.show() 

def tempsLinear(a,b,sample,k): 
    rmin=1e-5

    exact=0
    #Création de l'abscisse
    x=np.linspace(a,b,N,)
    
    #Même raison
    if a<rmin:
            x=np.linspace(rmin,b,N)
            x1=np.linspace(rmin,b,sample)
            x2=np.linspace(a,rmin,ceil(sample/10))
            t1=time.time()
            exact=green_functions.green2(k,x2)
            y=green_functions.green2(k,x1)
                
            f=interpolation.interpolLin(x1,y.real)
            fim=interpolation.interpolLin(x1,y.imag)
                
            y0=np.zeros(N)
            y0im=np.zeros(N)
            for i in range(N):
                 y0[i]=f(x[i])
                 y0im[i]=fim(x[i])
            t2=time.time()
            temps=ac.temps(t1,t2)

    else:
             x0=np.linspace(a,b,sample)
             y0=np.zeros(N)
             y0im=np.zeros(N)
             t1=time.time()
             y=green_functions.green2(k,x0)
             f=interpolation.interpolLin(x0,y.real)
             fim=interpolation.interpolLin(x0,y.imag)
             
             for i in range(N):
                    y0[i]=f(x[i])
                    y0im[i]=fim(x[i])
             t2=time.time()
             temps=ac.temps(t1,t2)
    return temps        

                

                
                
                
               