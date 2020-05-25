from math import *
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import green_functions
import interval
import erreurFonctionParamètre as efp
import cmath
import choixInterpolation as ci
import mainErreurLagrange as melg
import mainErreurLinear as mel
import accelCalcul as ac
import time
import mainLagrange
import mainLinear
            

#Ce fichier est le main et permet d'éxécuter le code
N=1000
rmin=1e-5
print("Souhaitez-vous faire une nouvelle interpolation ou vérifier l'erreur d'une interpolation en fonction d'un paramètre,")
print("Vérifier l'accélération du calcul et l'erreur ou comparer une interpolation avec la vraie fonction sur un graphique")
print("Nouvelle interpolation (1)")
print("Vérification erreur (2)")
print("Calcul de l'accélération (3)")
print("Comparer interpolation et vraie fonction sur un graphique (4)")
print("Comparer interpolation et vraie fonction sur un graphique (log) (5)")
print("Générer des graphiques d'erreurs relatives avec erreurs théoriques (6)")
print("Générer des graphiques du temps de calcul en fonction du degré d'interpolation (7)")

souhait=input()
souhait=int(souhait)
if souhait==1:
    ci.choix()
if souhait==2:
    print("Souhaitez vous modifier un paramètre et garder les autres par défaut ou modifier tous les paramètres ?")
    print("Modifier un paramètre (1)")
    print("Modifier tous les paramètres (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
        efp.erreurParametre()
    if choix==2:
        print("De quelle interpolation souhaitez-vous l'erreur ?")
        print("Interpolation par polynôme de Lagrange (1)")
        print("Interpolation Linéaire (2)")
        choix=input()
        choix=int(choix)
        if choix==1:
            melg.erreurLagrange()
        if choix==2:
            mel.erreurLinear()
    
if souhait==3:
       print("Quelle interpolation souhaitez vous ?")
       print("Interpolation par Polynome de Lagrange (1)")
       print("Interpolation linéaire (2)")
       choix=input()
       choix=int(choix)
       if choix==1:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer le nombre de points pour la vraie fonction")
            n=input()
            n=int(n)
            print("Entrer l'ordre du polynôme interpolateur")
            order=input()
            order=int(order)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            temps1=mainLagrange.tempsLagrange(a,b,order,k)
            x=np.linspace(a,b,n)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps2=ac.temps(t1,t2)
            accel=ac.accel(t1,t2)
            print("L'accélération est de : ", 100-accel, " %")
            melg.erreurLagrangeParametre(a,b,order,k)
       if choix==2:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer le nombre de points à sampler")
            order=input()
            order=int(order)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            temps1=mainLinear.tempsLinear(a,b,order,k)
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps2=ac.temps(t1,t2)
            accel=ac.accel(t1,t2)
            print("L'accélération est de : ", 100-accel, " %")
            mel.erreurLinearParametre(a,b,order,k)
if souhait==4:
       print("Quelle interpolation souhaitez vous ?")
       print("Interpolation par Polynome de Lagrange (1)")
       print("Interpolation linéaire (2)")
       choix=input()
       choix=int(choix)
       if choix==1:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer l'ordre du polynome")
            order=input()
            order=int(order)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            plt.plot(x,y.real)
            plt.plot(x,y.imag)
            if a<rmin:
                 x1=np.linspace(rmin,b,N, dtype=complex)
                 x2=np.linspace(a,rmin,ceil(N/10))
                 exact=green_functions.green2(k,x2) #partie exacte
                 P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                 Y=P(x)
                 plt.plot(x1.real,Y.real)
                 plt.plot(x1.real,Y.imag)
        
                 plt.plot(x2.real, exact.real)
                 plt.plot(x2.real, exact.imag)
                 plt.show()
             
            else:
                 P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 Y=P(x)
             
                
                 plt.plot(x,Y.real,'b')
                 plt.plot(x,Y.imag,'r')
                 plt.show()
             
            
       if choix==2:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer le nombre de points à sampler")
            n=input()
            n=int(n)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            plt.plot(x,y.real)
            plt.plot(x,y.imag)
    
            if a<rmin:
                x1=np.linspace(rmin,b,N+1, dtype=complex)
                x2=np.linspace(a,rmin,ceil(N/10))
                exact=green_functions.green2(k,x2)
                P=interpolation.linear(green_functions.green2,rmin,b,n,k)
                Y=P(x)
                plt.plot(x1.real,Y.real)
                plt.plot(x1.real,Y.imag)
                plt.plot(x2.real, exact.real)
                plt.plot(x2.real, exact.imag)
                plt.show()
            else:
                P=interpolation.linear(green_functions.green2,a,b,n,k)
                Y=P(x)
                plt.plot(x,Y.real,'b')
                plt.plot(x,Y.imag,'r')
                plt.show()
if souhait==5:
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation par Polynome de Lagrange (1)")
    print("Interpolation linéaire (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer l'ordre du polynome")
            order=input()
            order=int(order)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            x=np.linspace(a,b,N)
            y=np.log(green_functions.green2(k,x))
            plt.plot(x,y.real,label='Partie réelle fonction exacte')
            plt.plot(x,y.imag, label='Partie imaginaire fonction exacte')
            if a<rmin:
                 x1=np.linspace(rmin,b,N, dtype=complex)
                 x2=np.linspace(a,rmin,ceil(N/10))
                 exact=np.log(green_functions.green2(k,x2)) #partie exacte
                 P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                 Y=np.log(P(x))
                 plt.plot(x1.real,Y.real, label='Partie réelle interpolation')
                 plt.plot(x1.real,Y.imag, label='Partie imaginaire interpolation')
        
                 plt.plot(x2.real, exact.real, label='Partie réelle interpolation')
                 plt.plot(x2.real, exact.imag,label='Partie imaginaire interpolation')
                 plt.legend()
                 plt.show()
             
            else:
                 P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 Y=np.log(P(x))
             
                
                 plt.plot(x,Y.real,label='Partie réelle interpolation')
                 plt.plot(x,Y.imag,label='Partie imaginaire interpolation')
                 plt.legend()
                 plt.show()
             
            
    if choix==2:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Entrer le nombre de points à sampler")
            n=input()
            n=int(n)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            x=np.linspace(a,b,N)
            y=np.log(green_functions.green2(k,x))
            plt.plot(x,y.real, label='Partie réelle fonction exacte')
            plt.plot(x,y.imag, label='Partie imaginaire fonction exacte')
    
            if a<rmin:
                x1=np.linspace(rmin,b,N+1, dtype=complex)
                x2=np.linspace(a,rmin,ceil(N/10))
                exact=green_functions.green2(k,x2)
                P=interpolation.linear(green_functions.green2,rmin,b,n,k)
                Y=np.log(P(x))
                plt.plot(x1.real,Y.real, label='Partie réelle interpolation')
                plt.plot(x1.real,Y.imag, label='Partie imaginaire interpolation')
                plt.plot(x2.real, exact.real, label='Partie réelle interpolation')
                plt.plot(x2.real, exact.imag, label='Partie imaginaire interpolation')
                plt.legend()
                plt.show()

            else:
                P=interpolation.linear(green_functions.green2,a,b,n,k)
                Y=np.log(P(x))
                plt.plot(x,Y.real,label='Partie réelle interpolation')
                plt.plot(x,Y.imag,label='Partie imaginaire interpolation')
                plt.legend()
                plt.show()
if souhait==6:
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation par Polynome de Lagrange (1)")
    print("Interpolation linéaire (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            print("Entrer jusqu'à quelle ordre vous souhaitez les erreurs d'interpolations")
            n=input()
            n=int(n)
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            errRelative=[]
            liste=[]
            errTh=[]
            for i in range(2,n+1): 
                liste.append(i)
                P=interpolation.lagrange(green_functions.green2,a,b,i,k)
                Y=P(x)
                errRelative.append(np.max(np.log(np.abs(y-Y)/np.abs(y))))
                errTh.append(melg.erreurLagrangeParametre(a,b,i,k))
            plt.plot(liste,errRelative, label="Erreur relative d'interpolation (log)")
            plt.plot(liste,errTh,label="Erreur théorique d'interpolation")
            plt.xlabel("Ordre du polynome")
            plt.legend()
            plt.show()
    if choix==2:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            n=input()
            n=int(n)
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            errRelative=[]
            liste=[]
            errTh=[]
            for i in range(n+1): 
                liste.append(i)
                P=interpolation.linear(green_functions.green2,a,b,i,k)
                Y=P(x)
                errRelative.append(np.max(np.log(np.abs(y-Y)/np.abs(y))))
                errTh.append(mel.erreurLinearParametre(a,b,i,k))
            plt.plot(liste,errRelative, label="Erreur relative d'interpolation (log)")
            plt.plot(liste,errTh,label="Erreur théorique d'interpolation")
            plt.xlabel("Nombre de points samplés")
            plt.legend()
            plt.show()
if souhait==7:
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation par Polynome de Lagrange (1)")
    print("Interpolation linéaire (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
         
           
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            print("Entrer jusqu'à quel ordre vous souhaitez le temps de calcul du polynôme interpolateur")
            order=input()
            order=int(order)
            temps=[]
            liste=[]
            for i in range(2,order+1):
                liste.append(i)
                temps.append(mainLagrange.tempsLagrange(a,b,i,k))
            plt.plot(liste,temps)
            plt.xlabel('Ordre du polynome')
            plt.ylabel('Temps de calcul en s')
            plt.legend()
            plt.show()
    if choix==2:
            print("Entrer le début de l'intervalle")
            a=input()
            a=float(a)
            print("Entrer la fin de l'intervalle")
            b=input()
            b=float(b)
         
           
            print("Enter le paramètre k")
            k=input()
            k=float(k)
            print("Entrer jusqu'à combien de points samplés vous souhaitez le temps de calcul du polynôme interpolateur")
            order=input()
            order=int(order)
            temps=[]
            liste=[]
            for i in range(2,order+1):
                liste.append(i)
                temps.append(mainLinear.tempsLinear(a,b,i,k))
            plt.plot(liste,temps)
            plt.xlabel('Ordre du polynome')
            plt.ylabel('Temps de calcul en s')
            plt.legend()
            plt.show()