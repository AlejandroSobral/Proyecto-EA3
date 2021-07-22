# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import signal
from sympy import *
import matplotlib.pyplot as plt
import math as m
import numpy as np
from splane import pzmap, grpDelay, bodePlot

S,Kt,J,B,La,Ra,Kb=symbols('S Kt J B La Ra Kb')
tf=(S*Kt) /(S*((S*J + B)*(S*La + Ra)+(Kt*Kb)))
pprint(tf)
pprint(cancel(tf))
print("transferencia angulo L/ Ea")
Tf=(1)/(S*((S+20)*(S+0.5)+1))
Tf_util=expand(Tf)
pprint(Tf_util)
#num1=[1]
#den1=[1,20.5,11,0]
#sys1=signal.TransferFunction(num1, den1)
#bodePlot(sys1)
#pzmap(sys1)

print("ThetaL/Thetar")
#Suponemos Kp1 y Kp2=5
Num2=[5]
Den2=[1,20.5,11,5]
sys2=signal.TransferFunction(Num2,Den2)
bodePlot(sys2)
pzmap(sys2)
Num3=[23]
Den3=[1,20.5,11,23]
sys3=signal.TransferFunction(Num3,Den3)
bodePlot(sys3)
pzmap(sys2)
Num4=[40]
Den4=[1,20.5,11,40]
sys4=signal.TransferFunction(Num4,Den4)
bodePlot(sys2)
pzmap(sys2)
Num5=[205]
Den5=[1,20.5,11,205]
sys5=signal.TransferFunction(Num5,Den5)
bodePlot(sys5)
pzmap(sys5)
Num6=[380]
Den6=[1,20.5,11,380]
sys6=signal.TransferFunction(Num6,Den6)
bodePlot(sys6)
pzmap(sys6)

algo=(380)/(S**3+S**2*20.5+S*11+380)
pprint(apart(algo))
