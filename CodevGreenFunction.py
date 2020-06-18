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
from numpy.polynomial import Polynomial            
from scipy.interpolate import lagrange as lgtest
#Ce fichier est le main et permet d'éxécuter le code
frequence=int(1e3)
N=10*frequence

rmin=1e-3
print("Souhaitez-vous faire une nouvelle interpolation ou vérifier l'erreur d'une interpolation en fonction d'un paramètre,")
print("Vérifier l'accélération du calcul et l'erreur ou comparer une interpolation avec la vraie fonction sur un graphique")
print("Nouvelle interpolation (1)")
print("Vérification erreur (2)")
print("Calcul de l'accélération (3)")
print("Comparer interpolation et vraie fonction sur un graphique (4)")
print("Comparer interpolation et vraie fonction sur un graphique (log) (5)")
print("Générer des graphiques d'erreurs relatives avec erreurs théoriques (6)")
print("Générer des graphiques du temps de calcul en fonction du degré d'interpolation (7)")
print("Comparer les erreurs des deux interpolations (8)")
print("Voir les erreurs relatives sur le domaine (9)")
print("Comparer les accélérations des deux algorithmes (10)")
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
           #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            order=18
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps1=ac.temps(t1,t2)
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
            
            accel=ac.accel(temps1,temps2)
            print("L'accélération est de : ", accel, " %")
            melg.erreurLagrangeParametre(a,b,order,k)
       if choix==2:
            #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            sample=100
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps1=ac.temps(t1,t2)

            if a<rmin:
                x=np.linspace(rmin,b,N)
                x1=np.linspace(rmin,b,sample)
                x2=np.linspace(a,rmin,ceil(sample/10))
                
                exact=green_functions.green2(k,x2)
                y=green_functions.green2(k,x1)
                
                f=interpolation.interpolLin(x1,y.real)
                fim=interpolation.interpolLin(x1,y.imag)
                
                y0=np.zeros(N)
                y0im=np.zeros(N)
                t1=time.time()
                for i in range(N):
                    y0[i]=f(x[i])
                    y0im[i]=fim(x[i])
                t2=time.time()
                temps2=ac.temps(t1,t2)

            else:
                x0=np.linspace(a,b,sample)
                y0=np.zeros(N)
                y0im=np.zeros(N)
                
                y=green_functions.green2(k,x0)
                f=interpolation.interpolLin(x0,y.real)
                fim=interpolation.interpolLin(x0,y.imag)
                t1=time.time()
                for i in range(N):
                        y0[i]=f(x[i])
                        y0im[i]=fim(x[i])
                t2=time.time()
                temps2=ac.temps(t1,t2)
            
            accel=ac.accel(temps1,temps2)
            print("L'accélération est de : ", accel, " %")
            print(temps1)
            print(temps2)
            mel.erreurLinearParametre(a,b,sample,k)
if souhait==4:
       print("Quelle interpolation souhaitez vous ?")
       print("Interpolation par Polynome de Lagrange (1)")
       print("Interpolation linéaire (2)")
       choix=input()
       choix=int(choix)
       if choix==1:
            #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            order=18
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            plt.plot(x,y.real,label="Partie reelle fonction exacte")
            plt.plot(x,y.imag,label="Partie imaginaire fonction exacte")
            if a<rmin:
                 x1=np.linspace(rmin,b,N)
                 x2=np.linspace(a,rmin,ceil(N/10))
                 exact=green_functions.green2(k,x2) #partie exacte
                 P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                 Y=P(x)
                 plt.plot(x1.real,Y.real,label="Partie reelle interpolation "+str(order))
                 plt.plot(x1.real,Y.imag,label="Partie imaginaire de interpolation "+str(order))
        
                 plt.plot(x2.real, exact.real,label="Partie reelle interpolation "+str(order))
                 plt.plot(x2.real, exact.imag,label="Partie imaginaire interpolation "+str(order))
                 plt.show()
             
            else:
                 P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 Y=P(x)
                 xtest=np.linspace(a,b,order)
                 xtest=green_functions.green2(k,xtest)
                 poly=lgtest(xtest,ytest)
                 Ytest=poly(x)
                 #plt.plot(x,Ytest.real,marker="x",linestyle='None')
                 #plt.plot(x,Ytest.imag, marker="x",linestyle='None')
                 plt.plot(x,Y.real,label="Partie reelle interpolation "+str(order),linestyle='None',marker="x")
                 plt.plot(x,Y.imag,label="Partie imaginaire interpolation "+str(order), linestyle='None',marker="x")
                 plt.legend()
                 plt.show()
             
            
       if choix==2:
            #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            sample=100
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            plt.plot(x,y.real,label="Partie réelle fonction exacte")
            plt.plot(x,y.imag,label="Partie imaginaire fonction exacte")
    
            if a<rmin:
                x=np.linspace(rmin,b,N)
                x1=np.linspace(rmin,b,sample)
                x2=np.linspace(a,rmin,ceil(sample/10))
                exact=green_functions.green2(k,x2)
                y=green_functions.green2(k,x1)
                
                f=interpolation.interpolLin(x1,y.real)
                fim=interpolation.interpolLin(x1,y.imag)
                
                y0=np.zeros(N)
                y0im=np.zeros(N)
                for i in range(N):
                    y0[i]=f(x[i])
                    y0im[i]=fim(x[i])

                plt.plot(x,y0,label="Partie réelle de l'interpolation "+str(sample))
                plt.plot(x,y0im,label="Partie imaginaire de l'interpolation "+str(sample))
                plt.plot(x2, exact.real,label="Partie réelle de l'interpolation "+str(sample/10))
                plt.plot(x2, exact.imag,label="Partie imaginaire de l'interpolation "+str(sample/10))

                
            else:
                x0=np.linspace(a,b,sample)
                y=green_functions.green2(k,x0)
                f=interpolation.interpolLin(x0,y.real)
                fim=interpolation.interpolLin(x0,y.imag)
                y0=np.zeros(N)
                y0im=np.zeros(N)
                for i in range(N):
                    y0[i]=f(x[i])
                    y0im[i]=fim(x[i])
                plt.plot(x,y0,label="Partie réelle de l'interpolation " +str(sample),linestyle='None',marker="x")
                plt.plot(x,y0im,label="Partie imaginaire de l'interpolation "+str(sample),linestyle='None',marker="x")
            
            plt.legend()
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
            y=green_functions.green2(k,x)
            plt.semilogy(x,y.real,label='Partie réelle fonction exacte' )
            plt.semilogy(x,y.imag, label='Partie imaginaire fonction exacte')
            plt.semilogy(x,np.abs(y), label='ABSOLU')
            if a<rmin:
                 x1=np.linspace(rmin,b,N)
                 x2=np.linspace(a,rmin,ceil(N/10))
                 exact=green_functions.green2(k,x2) #partie exacte
                 P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                 Y=P(x)
                 plt.semilogy(x1,Y.real, label='Partie réelle interpolation '+str(order))
                 plt.semilogy(x1,Y.imag, label='Partie imaginaire interpolation '+str(order))
        
                 plt.semilogy(x2, exact.real, label='Partie réelle interpolation '+str(order))
                 plt.semilogy(x2, exact.imag,label='Partie imaginaire interpolation '+str(order))
                 plt.legend()
                 plt.show()
             
            else:
                 P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 Y=P(x)
             
                
                 plt.semilogy(x,Y.real,label='Partie réelle interpolation '+str(order))
                 plt.semilogy(x,Y.imag,label='Partie imaginaire interpolation '+str(order))
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
            y=green_functions.green2(k,x)
            plt.plot(x,y.real, label='Partie réelle fonction exacte')
            plt.plot(x,y.imag, label='Partie imaginaire fonction exacte')
    
            if a<rmin:
                x1=np.linspace(rmin,b,N+1)
                x2=np.linspace(a,rmin,ceil(N/10))
                exact=green_functions.green2(k,x2)
                P=interpolation.linear(green_functions.green2,rmin,b,n,k)
                Y=np.log(P(x))
                plt.plot(x1,Y.real, label='Partie réelle interpolation'+str(sample))
                plt.plot(x1,Y.imag, label='Partie imaginaire interpolation'+str(sample))
                plt.plot(x2, exact.real, label='Partie réelle interpolation'+str(sample))
                plt.plot(x2, exact.imag, label='Partie imaginaire interpolation'+str(sample))
                plt.legend()
                plt.show()

            else:
                P=interpolation.linear(green_functions.green2,a,b,n,k)
                
                plt.plot(x,Y.real,label='Partie réelle interpolation'+str(sample))
                plt.plot(x,Y.imag,label='Partie imaginaire interpolation'+str(sample))
                plt.legend()
                plt.show()
if souhait==6:
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation par Polynome de Lagrange (1)")
    print("Interpolation linéaire (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
            #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            n=21
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            errRelative=[]
            liste=[]
            errTh=[]
            for i in range(2,n+1): 
                liste.append(i)
                P=interpolation.lagrange(green_functions.green2,a,b,i,k)
                Y=P(x)
                errRelative.append(np.max(np.abs(y-Y)/np.abs(y)))
                errTh.append(melg.erreurLagrangeParametre(a,b,i,k))
            plt.plot(liste,errRelative, label="Erreur relative d'interpolation")
            #plt.plot(liste,errTh,label="Erreur théorique d'interpolation")
            plt.xlabel("Ordre du polynome")
            plt.legend()
            plt.show()
    if choix==2:
            #print("Entrer le début de l'intervalle")
            #a=input()
            #a=float(a)
            #print("Entrer la fin de l'intervalle")
            #b=input()
            #b=float(b)
            #print("Enter le paramètre k")
            #k=input()
            #k=float(k)
            #print("Entrer jusqu'à quelle nombre de points samplés vous souhaitez les erreurs d'interpolations")
            #sample=input()
            #sample=int(sample)
            a=1
            b=10
            k=10
            sample=100
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            errRelative=[]
            liste=[]
            errTh=[]
            Y=np.zeros(N)
            
               
            for i in range(2,sample+1): 
                
                if a<rmin:
                    x=np.linspace(rmin,b,N)
                    x1=np.linspace(rmin,b,i)
                    x2=np.linspace(a,rmin,ceil(i/10))
                    exact=green_functions.green2(k,x2)
                    y1=green_functions.green2(k,x1)
                
                    f=interpolation.interpolLin(x1,y1.real)
                    fim=interpolation.interpolLin(x1,y1.imag)
                
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=(y0[j]+y0im[j])
                
                else:
                    x0=np.linspace(a,b,i)
                    y1=green_functions.green2(k,x0)
                    
                    f=interpolation.interpolLin(x0,y1.real)
                    fim=interpolation.interpolLin(x0,y1.imag)
                    
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=(y0[j]+y0im[j])
                    
                        
                liste.append(i)
                
                errRelative.append(np.max((np.abs(y-Y)/np.abs(y))))
                errTh.append(mel.erreurLinearParametre(a,b,i,k))
                print(errTh)
            plt.plot(liste,errRelative, label="Erreur relative d'interpolation")
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
            a=1
            b=10
            k=10
            order=21
            accelList=[]
            liste=[]
           
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps1=ac.temps(t1,t2)
            for i in range(2,order+1):
                 
                if a<rmin:
                    
                    x1=np.linspace(rmin,b,N)
                    x2=np.linspace(a,rmin,ceil(N/10))
                    exact=green_functions.green2(k,x2) #partie exacte
                    P=interpolation.lagrange(green_functions.green2,rmin,b,order,k) #partie interpolée
                    t1=time.time()
                    Y=P(x)
                    t2=time.time()
                 
                else:
                 
                    P=interpolation.lagrange(green_functions.green2,a,b,order,k)
                 
                    t1=time.time()
                    Y=P(x)
                    t2=time.time()
                 
                temps2=ac.temps(t1,t2)
                
                
                accel=ac.accel(temps1,temps2)
                print("L'accélération est de : ", accel, " %")
                accelList.append(accel)
                liste.append(i)

            plt.plot(liste,accelList)
            
            plt.xlabel('Ordre du polynome')
            plt.ylabel('Accelération en %')
            plt.legend()
            plt.show()
    if choix==2:
            a=1
            b=10
            k=10
            sample=100
            accelList=[]
            liste=[]
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps1=ac.temps(t1,t2)
            for i in range(2,sample+1):
                if a<rmin:
                    x=np.linspace(rmin,b,N)
                    x1=np.linspace(rmin,b,i)
                    x2=np.linspace(a,rmin,ceil(i/10))
                    
                    exact=green_functions.green2(k,x2)
                    y=green_functions.green2(k,x1)
                
                    f=interpolation.interpolLin(x1,y.real)
                    fim=interpolation.interpolLin(x1,y.imag)
                
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    t1=time.time()
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                    t2=time.time()
                    temps2=ac.temps(t1,t2)

                else:
                    x0=np.linspace(a,b,i)
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    
                    y=green_functions.green2(k,x0)
                    f=interpolation.interpolLin(x0,y.real)
                    fim=interpolation.interpolLin(x0,y.imag)
                    
                    t1=time.time()
                    for j in range(N):
                            y0[j]=f(x[j])
                            y0im[j]=fim(x[j])
                    t2=time.time()
                    temps2=ac.temps(t1,t2)
                
                accel=ac.accel(temps1,temps2)
                print("L'accélération est de : ", accel, " %")
                liste.append(i)
                accelList.append(accel)

            plt.plot(liste,accelList)
            plt.xlabel('Nombre de points samplés')
            plt.ylabel('Accélération en %')
            plt.legend()
            plt.show()

if souhait==8:
            
            a=1
            b=10
            k=10
            sample=20
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            errRelativeLg=[]
            liste=[]
            errRelativeLin=[]
           
            
            Y=np.zeros(N)
            for i in range(2,sample+1): 
                liste.append(i)
                P=interpolation.lagrange(green_functions.green2,a,b,i,k)
                Y=P(x)
                errRelativeLg.append(np.max(np.abs(y-Y)/np.abs(y)))
                print(errRelativeLg)

                if a<rmin:
                    x=np.linspace(rmin,b,N)
                    x1=np.linspace(rmin,b,i)
                    x2=np.linspace(a,rmin,ceil(i/10))
                    exact=green_functions.green2(k,x2)
                    y1=green_functions.green2(k,x1)
                
                    f=interpolation.interpolLin(x1,y1.real)
                    fim=interpolation.interpolLin(x1,y1.imag)
                
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=sqrt(y0[j]**2+y0im[j]**2)
                
                else:
                    x0=np.linspace(a,b,i)
                    y1=green_functions.green2(k,x0)
                    f=interpolation.interpolLin(x0,y1.real)
                    fim=interpolation.interpolLin(x0,y1.imag)
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=(sqrt(y0[j]**2+y0im[j]**2))
                errRelativeLin.append(np.max((np.abs(y-Y)/np.abs(y))))
                print(errRelativeLin)
            
            
            plt.semilogy(liste,errRelativeLg, label="Erreur relative d'interpolation par Lagrange")
            plt.semilogy(liste,errRelativeLin, label="Erreur relative d'interpolation linéaire")
                
            plt.legend()
            plt.show()
if souhait==9:
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation par Polynome de Lagrange (1)")
    print("Interpolation linéaire (2)")
    choix=input()
    choix=int(choix)
    if choix==1:
            a=1
            b=10
            k=10
            order=18
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            
            
             
                
            P=interpolation.lagrange(green_functions.green2,a,b,order,k)
            Y=P(x)
            errRelative=np.abs((y-Y)/y)
            
            plt.plot(x,errRelative, label="Erreur relative d'interpolation")
            plt.xlabel("Ordre du polynome " + str(order))
            
            plt.legend()
            plt.show()
    if choix==2:
            a=1
            b=100
            k=10
            sample=100
            x=np.linspace(a,b,N)
            y=green_functions.green2(k,x)
            
            Y=np.zeros(N)
            
               
             
                
            if a<rmin:
                    x=np.linspace(rmin,b,N)
                    x1=np.linspace(rmin,b,sample)
                    x2=np.linspace(a,rmin,ceil(sample/10))
                    exact=green_functions.green2(k,x2)
                    y1=green_functions.green2(k,x1)
                
                    f=interpolation.interpolLin(x1,y1.real)
                    fim=interpolation.interpolLin(x1,y1.imag)
                
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=(y0[j]+y0im[j])
                
            else:
                    x0=np.linspace(a,b,sample)
                    y1=green_functions.green2(k,x0)
                    
                    f=interpolation.interpolLin(x0,y1.real)
                    fim=interpolation.interpolLin(x0,y1.imag)
                    
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    for j in range(N):
                        
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                        Y[j]=(y0[j]+y0im[j])
                    
                        
                
                
            errRelative=(np.abs(y-Y)/np.abs(y))
                
                
            plt.plot(x,errRelative, label="Erreur relative d'interpolation")
            
            plt.xlabel("Nombre de points samplés " + str(sample))
            plt.legend()
            plt.show()
if souhait==10:
            a=1
            b=10
            k=10
            order=30
            x=np.linspace(a,b,N)
            t1=time.time()
            y=green_functions.green2(k,x)
            t2=time.time()
            temps1=ac.temps(t1,t2)
            liste=[]
            accelLgList=[]
            accelLinList=[]
            for i in range(2,order+1):
                if a<rmin:
                    
                    x1=np.linspace(rmin,b,N)
                    x2=np.linspace(a,rmin,ceil(N/10))
                    exact=green_functions.green2(k,x2) #partie exacte
                    P=interpolation.lagrange(green_functions.green2,rmin,b,i,k) #partie interpolée
                    t1=time.time()
                    Y=P(x)
                    t2=time.time()

                    
                    x1=np.linspace(rmin,b,i)
                    x2=np.linspace(a,rmin,ceil(i/10))
                
                    exact=green_functions.green2(k,x2)
                    y=green_functions.green2(k,x1)
                
                    f=interpolation.interpolLin(x1,y.real)
                    fim=interpolation.interpolLin(x1,y.imag)
                
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                    t3=time.time()
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                    t4=time.time()
                    
                else:
                 
                    P=interpolation.lagrange(green_functions.green2,a,b,i,k)                
                    t1=time.time()
                    Y=P(x)
                    t2=time.time()

                    x0=np.linspace(a,b,i)
                    y0=np.zeros(N)
                    y0im=np.zeros(N)
                
                    y=green_functions.green2(k,x0)
                    f=interpolation.interpolLin(x0,y.real)
                    fim=interpolation.interpolLin(x0,y.imag)
                    t3=time.time()
                    for j in range(N):
                        y0[j]=f(x[j])
                        y0im[j]=fim(x[j])
                    t4=time.time()
                 
                temps2=ac.temps(t1,t2)
                temps3=ac.temps(t3,t4)
            
                accelLg=ac.accel(temps1,temps2)
                accelLin=ac.accel(temps1,temps3)
                accelLgList.append(accelLg)
                accelLinList.append(accelLin)
                print(accelLin,accelLg)
                liste.append(i)
            plt.plot(liste,accelLgList,label="Acceleration interpolation Lagrange")
            plt.plot(liste,accelLinList,label="Acceleration interpolation Lineaire")
            plt.legend()
            plt.show()