import matplotlib.pyplot as plt
import numpy as np

alpha, beta = 60, 39
t0, t1 = 0 , 1.4
x0, y0 = alpha, 0
h = 0.2

def functy(t,y):
    return 1 + y**2

prevPoint = [y0]

while (t0 < t1):
    t0 += h
    ynext = prevPoint[-1] + h/2*(functy(t0, prevPoint[-1]) + functy(t0 + h, prevPoint[-1] + h * functy(t0, prevPoint[-1])))
    prevPoint.append(ynext)
    

print(prevPoint)