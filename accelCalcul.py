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

def accel(t1,t2):
    return(t2*100/t1)

def temps(t1,t2):
    return(t2-t1)
