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

## DATOS
f = 900e6
w = f*2*m.pi
L = 4.7e-9
Q = 140
CD = 5.78e-12
C3 = 1e-12
C4 = 1e-12
R1 = 25e3
ICQ = 170.72e-6

formatter = mpl.ticker.EngFormatter()
w_f = formatter(w)
print("El valor de W es", w_f, "1/s")

Y21 = 40*ICQ
Y21_f = formatter(Y21)
print("Y21 equivalente a gm es: ",Y21_f, "S")

Rp = w*L/Q
Rp_f = formatter(Rp)
print("R pérdida serie: ", Rp_f, "Ω")

YL = (1/(L*w))

YL_f = formatter(YL)
print("El valor de Admitancia del inductor", YL_f, "S")

XL = 1/YL

YC = (w*CD)
XC = 1/YC
YC_f = formatter(YC)
print("El valor de Admitancia del capacitor", YC_f, "S")

Yt = YC - YL
X = -(1/Yt)



Yt_f = formatter(Yt)
print("El valor de Admitancia paralelo total es", Yt_f, "S")



XL_f = formatter(XL)
print("XL @900Mhz", XL_f, "Ω")

XC_f = formatter(XC)
print("XC @900Mhz", XC_f, "Ω")

X_f = formatter(X)
print("Xtotal @900Mhz", X_f, "Ω")



bc3 = w*C3
bc3_f = formatter(bc3)
print("Bc3 equivale a: ",bc3_f, "S")


bc4 = w*C4
bc4_f = formatter(bc4)
print("Bc4 equivale a: ",bc4_f, "S")

g1 = 1/R1
g1_f = formatter(g1)
print("g1 por R1 es ", g1_f, "S")
g11 = 182.7e-6
g11_f = formatter(g11)
print("g11 es",g11_f, "S")
g22 = 9.479e-6
g22_f = formatter(g22)
print("g22 es",g22_f, "S")
b11 = 5.259e-3
b11_f = formatter(b11)
print("b11 es",b11_f, "S")
b22 = 1.357e-3
b22_f = formatter(b22)
print("b22 es",b22_f, "S") 

G11 = g11 
G22 = g22 + g1
B11 = b11 + bc3
B22 = b22 + bc4

G11_f = formatter(G11)
print("G11 total es", G11_f, "S")
G22_f = formatter(G22)
print("G22 total es", G22_f, "S")
B11_f = formatter(B11)
print("B11 total es", B11_f, "S")
B22_f = formatter(B22)
print("B22 total es", B22_f, "S")


arranque = G11 + G22 + ((G11*G22-B11*B22)*Rp) - ((G11*B22-G22*B11)*X)
arranque_f = formatter(arranque)
print("Condición de arranque:", arranque_f, "S")



fosci = B11+B22+(G11*G22-B11*B22)*X - (G11*B22-G22*B11)*Rp
fosci_f = formatter(fosci)
print("La condición de oscilación arroja: ", fosci_f,"S")

#formatter = mpl.ticker.EngFormatter()


Lx = symbols('Lx')
L_equation = Eq(B11+B22+(G11*G22-B11*B22)*(1/(-(YC)+(1/(Lx*w)))) - (G11*B22-G22*B11)*Rp)

solu = solve(L_equation, force = True)
Lx_value = solu[0]
lx_f = formatter(Lx_value)
print("El inductor equivalente es: ",lx_f, "Hy")


wx = symbols('wx')
w_equation = Eq(B11+B22+(G11*G22-B11*B22)*(1/(-(YC)+(1/(Lx_value*wx)))) - (G11*B22-G22*B11)*Rp)

solu = solve(w_equation, force = True)
wx_value = solu[0]/(2*m.pi)
wx_f = formatter(wx_value)
print("La frecuencia recalculada equivale a ",wx_f, "Hz")



























