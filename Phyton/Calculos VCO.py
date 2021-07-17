# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:10:37 2021

@author: Alejandro
"""

from scipy import signal
from sympy import *
import matplotlib.pyplot as plt
import math as m
from splane import pzmap, grpDelay, bodePlot
import numpy as np
import matplotlib as mpl

formatter = mpl.ticker.EngFormatter()

f = 900e6 # F = 900 Mhz
f_forma = formatter(f)
print("Frecuencia buscada: ", f_forma)

L1 = 5e-9 #Datasheet
Q = 140 #Datasheet

Rp = Q*2*m.pi*f*L1

Rp_forma = formatter(Rp)
print("Rp: ",Rp_forma)


Cstray = 2.7e-12
C17= 1.5e-12
C6 = 1.5e-12
C5 = 1.5e-12
C03 = 2.4e-12
C04 = 2.4e-12
C3 = 2.7e-12
C4 = 1e-12
CD1 = 3.55e-12 # Varactor capacitance

Cn = (C3+C03)*(C4*C04)/(C3+C03+C4+C04)
Cn_forma = formatter(Cn) 

print("Cn :", Cn)       
print("Cn :", Cn_forma)

fo = 1/(2*m.pi*sqrt(L1*(Cstray+(C17*CD1/(C17+CD1))+C6+(C5*Cn/(C5+Cn)))))
fo_forma = formatter(fo)
print("Frecuencia resultante :", fo_forma)



CD_sy = symbols('CD_sy')
CD_equation = Eq(-1 + f*(2*m.pi*sqrt(L1*(Cstray+(C17*CD_sy/(C17+CD_sy))+C6+(C5*Cn/(C5+Cn))))))
solu = solve(CD_equation)
CD_value = solu[0]
CD_value_forma = formatter(CD_value)
print("Valor exacto del varactor para 900Mhz: ", CD_value)

# solu_f = formatter(solu)
# print("Varactor resultante :", solu_f)





































