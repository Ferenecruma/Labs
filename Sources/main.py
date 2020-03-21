import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as lg

x=np.array([-1.6,-1.2,-0.8,-0.4,0.0,0.4,0.8,1.2,1.6,2.0])
y=np.array([4.32,3.28,2.88,3.12,4.0,5.52,7.68,10.48,13.92,18.0])
eps=np.array([-0.0081,0.0047,-0.0016,0.0022,-0.0064,0.0043,-0.0005,0.0096,-0.0042,0.0029])
y_zbur=y+eps
matr=np.zeros((3,3))
vec,vec1=np.zeros(3),np.zeros(3)

for i in range(len(x)):
    matr[0,0]+=pow(x[i],4)
    matr[0,1]+=pow(x[i],3)
    matr[1,1]+=pow(x[i],2)
    matr[2,1]+=x[i]
matr[2,2]=10
matr[1,0]=matr[0,1]
matr[0,2]=matr[2,0]=matr[1,1]
matr[1,0]=matr[0,1]
matr[1,2]=matr[2,1]
for i in range(len(vec)):
    for j in range(len(x)):
        vec[i]+=y[j]*pow(x[j],2-i)
for i in range(len(vec)):
    for j in range(len(x)):
        vec1[i]+=y_zbur[j]*pow(x[j],2-i)

sol=lg.solve(matr,vec)
sol1=lg.solve(matr,vec1)
print(np.dot(matr,sol)-vec)
# print(sol)
# print(sol1)

def func(x):
    return sol[0]*x**2+sol[1]*x+sol[2]
def func1(x):
    return sol1[0]*x**2+sol1[1]*x+sol1[2]
x1=np.linspace(-1.6,2.0,100)
y1=np.zeros(100)
y2=np.zeros(100)
for i,val in enumerate(x1):
    y1[i]=func(val)
for i,val in enumerate(x1):
    y2[i]=func1(val)   
plt.scatter(x,y,s=7.5,color="red")
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.show()

