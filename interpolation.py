
import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt
import sympy as sp
from scipy.interpolate import lagrange as lg


"""Cette fonction est l'interpolation
de Lagrange qui nous servira sur la 
Green Function"""
#A noter que n est l'ordre du polynome

def lagrange(f,a,b,n,k):
    #Création de l'ensemble des valeurs de r
    x=np.linspace(a,b,n+1)
    #Initialisation du polynome
    X=np.poly1d([1,0])
    P=0
    #Création du Polynome
    for i in range(n+1):
        L=1
        for j in range (0,i):
            L=L*(X-x[j])/(x[i]-x[j])
        for j in range (i+1, n+1):
            L=L*(X-x[j])/(x[i]-x[j])
    #Formule d'interpolation
        P=P+L*f(k,x[i])
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

def linear(f,a,b,n,k):
    #Création de l'ensemble des valeurs de r
    x=np.linspace(a,b,n+2) 
    #Initialisation du polynome
    X=np.poly1d([1,0])
    L=0
    for i in range(n+1):
        P=(X-x[i+1])/(x[i]-x[i+1])
        L=L+P*f(k,x[i])
    return L

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