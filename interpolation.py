
import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt
import sympy as sp
from scipy.interpolate import lagrange as lg
from numpy.polynomial import Polynomial

"""Cette fonction est l'interpolation
de Lagrange qui nous servira sur la 
Green Function"""
#A noter que n est l'ordre du polynome

def lagrange(f,a,b,n,k):
    #Création de l'ensemble des valeurs de r
    x=np.linspace(a,b,n)
    
    #Initialisation du polynome
    X=Polynomial([0,1])
    P=Polynomial([0])
    #Création du Polynome
    for j in range(n):
        L=Polynomial([1,0])
        for m in range (0,j):
            L=L*(X-x[m])/(x[j]-x[m])
        for m in range (j+1, n):
            L=L*(X-x[m])/(x[j]-x[m])
    #Formule d'interpolation
        P=P+L*f(k,x[j])

        
    return P

"""Cette fonction nous donnera l'erreur 
sur l'interpolation"""

def erreurLagrange(f,a,b,n):
    #Création de l'ensemble des valeurs de r
    x=np.linspace(a,b,n+1)  
    #Initialisation du polynome
    X=np.poly1d([1,0])
    #Calcul de la dérivée n+1
    y=derivOrdreN(f,x,n)
    #On prend le max de cette dérivée
    fmax=max(abs(y))
    #Calcul de la factorielle 
    factn=fact(n+1)
    #Init
    E=fmax/factn
    #Calcul du majorant de l'erreur
    for i in range(n+1):
        E*=(X-x[i])
    return max(E)
    
#Fonction permettant de dériver
def deriv(f,x):
    #Nous donne la taille de l'ensemble des valeurs de f
    n=f.size
    #Initialisation d'un tableau de zero
    #Initialisation en tant que complexe
    d=np.zeros(n,'d')
    #Calcul de la dérivée
    for i in range (1, n-1):
        d[i]=(f[i+1]-f[i-1])/(x[i+1]-x[i-1])
    d[0]=(f[1]-f[0])/(x[1]-x[0])
    d[n-1]=(f[n-1]-f[n-2])/(x[n-1]-x[n-2])
    return d

#Fonction calculant la factorielle récursivement
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

def interpolLin(x, y):
    #x est le linspace sur le nombre de points à sampler
    #y est la fonction samplée 
        def interpFn(x0):
            #x0 est le point sur lequel on travaille 
            if x0 < x[0] or x0 > x[-1]:
                raise BaseException
            elif x0 == x[0]:
                return y[0]
            elif x0 == x[-1]:
                return y[-1]
            else:
                i2 = 0
                while x0 > x[i2]:
                    i2 += 1
                i1 = i2 - 1
                t = (x0 - x[i1])/(x[i2]-x[i1])
                return y[i1]*(1-t) + t*y[i2]
        return interpFn


    

def erreurLinear(f,a,b,n):
     #Création de l'ensemble des valeurs de r
    x=np.linspace(a,b,n+1)  
    #Initialisation du polynome
    X=np.poly1d([1,0])
    #Initialisation de la dérivée
    y=derivOrdreN(f,x,n)
    #On prend le max de cette dérivée
    fmax=max(abs(y))
    #Calcul de la factorielle 
    factn=fact(n+1)
    #On retourne le majorant de l'erreur
    return (((b-a)/n)**(n+1))*fmax/(4*factn)

def derivOrdreN(y,x,n):
    #Initialisation de la dérivée
    y=deriv(y,x)
    i=1
    #Calcul de la dérivée n+1
    while i<n+1:
        y=deriv(y,x)
        i+=1
    return y