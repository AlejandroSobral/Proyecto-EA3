# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:46 2020

@author: Alejandro
"""
from scipy import signal
from sympy import *
import matplotlib.pyplot as plt
import math as m
from splane import pzmap, grpDelay, bodePlot
import numpy as np



S, gm, capa=symbols('S gm capa')
#Si ya use la letra C soy un bolas
Y_FET= Matrix(([0,0],
            [gm,0]))
print("Y_FET=")
pprint(Y_FET)

Y_C= Matrix(([S*capa,-S*capa],
            [-S*capa,S*capa]))
print("Y_C=")
pprint(Y_C)

Y_Equi= Y_FET + Y_C
print("Y_Equi=")
pprint(Y_Equi)
pprint(det(Y_Equi))

#print("\nY_Equi[1] es:",Y_Equi[1])

T_Equi= Matrix(([-Y_Equi[3]/Y_Equi[2],-1/Y_Equi[2]],
            [-det(Y_Equi)/Y_Equi[2],-Y_Equi[0]/Y_Equi[2]]))
print("T_Equi=")
pprint(T_Equi)

T_C=Matrix(([-Y_C[3]/Y_C[2],-1/Y_C[2]],
            [-det(Y_C)/Y_C[2],-Y_C[0]/Y_C[2]]))
print("T_C=")
pprint(T_C)

T_total=T_C*T_Equi
print("T_total=")
pprint(T_total)