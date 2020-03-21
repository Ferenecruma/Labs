import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

# matr=np.array([[0,9,12],[1/3,0,0],[0,0.5,0]])#Матриця Леслі
# startpopulation=np.array([0,1,1])#Популяція у початковий момент
# t=15
# #Для t=4 кількість більше 70
# # population=np.dot(lg.matrix_power(matr,t),startpopulation)
# # eigenval,eigenvec=lg.eig(np.transpose(matr))
# # print(population)
# # print(eigenval)
# # print(eigenvec[:,0])
# #немає стійкої вікової структури відміної від тривіальної

# #-----------------------------
# def model(P,t):
#     dPdt = 0.6*(P**2-170*P)
#     return dPdt
# # initial condition
# m=GEKKO()
# y=m.Var(120.0)
# k1,k2=0.006,170
# m.Equation(y.dt==y)
# m.time=np.linspace(0,1)

# m.options.IMODE = 4
# m.solve()

# plt.plot(m.time,y)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()

m = GEKKO()    # create GEKKO model
k = 0.006       # constant
y = m.Var(220.0) # create GEKKO variable
m.Equation(y.dt()==k*(y*y-170*y)) # create GEEKO equation
m.time = np.linspace(0,0.9,10) # time points



# solve ODE
m.options.IMODE = 4
m.solve()
plt.plot(m.time,y)
y = m.Var(120.0)
m.Equation(y.dt()==k*(y*y-170*y))
m.solve()
plt.plot(m.time,y)
# plot results
plt.scatter(0,120)
plt.scatter(0,220)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()