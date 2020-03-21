import random
import numpy as np
import matplotlib.pyplot as plt
import copy

a,b=-10,10#Кінці області на якій ми шукаємо екстремум
c1,c2,c3=1,1,1
quantity=10#Кількість точок рою
roy=np.empty((quantity,6))
globalBest=np.array([5,-5])
# x=np.empty(quantity)
# y=np.empty(quantity)

def reflect(x,y):#Функція відбитя точки від границі області допустимих значень
    if((a<x and x<b) and (a<y and y<b)):
        return x,y
    elif(x>b):
        return reflect(b-(x-b),y)
    elif(y>b):
        return reflect(x,b-(y-b))    
    elif(x<a):
        return reflect(a-(x-a),y)
    elif(y<a):
        return reflect(x,a-(y-a))

def func(x,y):
    return np.sin(x)+np.sin(y)
#initiallization of a roy
for i in range(quantity):
    roy[i,0]=random.uniform(a,b)#position x
    roy[i,1]=random.uniform(a,b)#position y
    roy[i,2]=random.uniform(-1*(b-a),b-a)#velocity x
    roy[i,3]=random.uniform(-1*(b-a),b-a)#velocity y
    roy[i,4]=random.uniform(a,b)#best state x
    roy[i,5]=random.uniform(a,b)#best state y
    if(func(roy[i][4],roy[i][5])<func(globalBest[0],globalBest[1])):
        globalBest[0],globalBest[1]=roy[i,4],roy[i,5]
# for i in range(quantity):
#     x[i]=roy[i][0]
#     y[i]=roy[i][1] 

# plt.scatter(x,y,s=3)
# plt.show()

for j in range(quantity):
    for i in roy:
        r1_x,r1_y,r2_x,r2_y=random.uniform(a,b),random.uniform(a,b),random.uniform(a,b),random.uniform(a,b)#random constants for new velocity computing
        i[2]=c1*i[2]+c2*r1_x*(i[4]-i[0])+c3*r2_x*(globalBest[0]-i[0])#update velocity x
        i[3]=c1*i[3]+c2*r1_x*(i[5]-i[1])+c3*r2_x*(globalBest[1]-i[1])#update velocity y
        i[0],i[1]=reflect(i[0]+i[2],i[1]+i[3])#update position 
        l=func(i[0],i[1])#value of func at current position of point
        l1=copy.deepcopy(func(i[4],i[5]))#best value of function of this point
        l2=copy.deepcopy(func(globalBest[0],globalBest[1]))#global best value
        # print(i[0],i[1])
        if(l<l1):
            i[4],i[5]=copy.deepcopy(i[0]),copy.deepcopy(i[1])
        if(l<l2):
            print(str(l) + " : " + str(l2) + "\n")
            globalBest[0]=copy.deepcopy(i[0])
            globalBest[1]=copy.deepcopy(i[1])
print(globalBest[0],globalBest[1])    
print(func(globalBest[0],globalBest[1]))     
        







# class particle:
#     globalBest=np.ones(2)

#     def __init__(self):      
#         self.position=np.array([random.uniform(a,b),random.uniform(a,b)])
#         self.bestState=np.array([self.position[0],self.position[1]])
#         if(func(self.bestState[0],self.bestState[1])>func(self.globalBest[0],self.globalBest[1])):
#             self.globalBest=self.bestState
#         self.velocity=np.array([random.uniform(-1*(b-a),b-a),random.uniform(-1*(b-a),b-a)])
        
#     def updVelocityAndPosition(self):#had some troubles with pointers in python,should remember that variable is a pointer to object
#         r1,r2=np.array([random.uniform(a,b),random.uniform(a,b)]),np.array([random.uniform(a,b),random.uniform(a,b)])
#         self.velocity=c1*self.velocity+c2*r1*(self.bestState-self.position)+c3*r2*(self.globalBest-self.position)
#         newpos=np.array(self.position+self.velocity)
#         self.position[0],self.position[1]=reflect(newpos[0],newpos[1])
        
#     def updBestState(self):
        
#         l=func(self.position[0],self.position[1])#value at current position
#         l1=func(self.bestState[0],self.bestState[1])#local min
#         l3=func(self.globalBest[0],self.globalBest[1])#global min
#         if(l<l1):
#             self.bestState=self.position
#         if(l<l3):
#             self.globalBest=self.position
#             print(func(self.globalBest[0],self.globalBest[1]))
            

# for i in range(100):
#     for counter,o in enumerate(roy):
#         o.updVelocityAndPosition()
#         o.updBestState()

    