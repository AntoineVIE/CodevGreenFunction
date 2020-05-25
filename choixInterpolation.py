
import mainLagrange as mlg
import mainLinear as ml

def choix():
    print("Quelle interpolation souhaitez vous ?")
    print("Interpolation de Lagrange (1)")
    print("Interpolation linéaire (2)")

    souhait=input()
    souhait=int(souhait)

    if souhait==1:
        mlg.mainLagrange()
    if souhait==2:
        ml.mainLinear()
