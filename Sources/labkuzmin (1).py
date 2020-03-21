import random
import numpy as np
import copy

#Параметри
a,b=-2,2#Кінці області на якій ми шукаємо екстремум
c1,c2,c3=0.5,1.3,1.2
quantity=400#Кількість точок рою
n=3#Вимір простору функції 
def func(arr,n=n):
    result=0
    for i in range(n-1):
        result+=(1-arr[i])**2+100*(arr[i+1]-arr[i]**2)**2
    return result
def funcRostr(arr,n=n):
    result=10*n
    for i in range(n):
        result+=arr[i]**2-10*np.cos(2*np.pi*arr[i])
    return result
#-----------------------------------------------------#
roy=np.empty((quantity,3*n))
GlobalBest=[]
for i in range(n):
    GlobalBest.append(random.uniform(a,b))

def reflect(arr,level=0):#Функція відбитя точки від границі області допустимих значень
    arr=arr%(b-a)
    while((arr>b).any() or (arr<a).any()):
        for i in range(n):
            if(arr[i]<a):
                arr[i]=a+(a-arr[i])
            if(arr[i]>b):
                arr[i]=b-(arr[i]-b)
    return arr

#ініціалізація рою
for i in range(quantity):
    for k in range(n):
        roy[i,k]=random.uniform(a,b)#позиція
        roy[i,k+n]=random.uniform(-1*(b-a),b-a)#швидкість
        roy[i,k+2*n]=random.uniform(a,b)#найкраща позиція
    if(func(roy[i][2*n:])<func(GlobalBest)):
        for j in range(n):
            GlobalBest[j]=roy[i][j+2*n]
        
for j in range(quantity):#Ітераційний процес
    for i in roy:
        for j in range(n):
            r1,r2=random.uniform(0,1),random.uniform(0,1)
            i[n+j]=c1*i[n+j]+c2*r1*(i[2*n+j]-i[j])+c3*r2*(GlobalBest[j]-i[j])#update velocity
            i[j]+=i[n+j]
        arr_pos=reflect(i[:n])#update position 
        l=func(arr_pos)#value of func at current position of point
        l1=func(i[2*n:])#best value of function of this point
        l2=func(GlobalBest)#global best value
        if(l<l1):
            for j in range(n):
                i[2*n+j]=arr_pos[j]
        if(l<l2):
            for j in range(n):
                GlobalBest[j]=copy.deepcopy(arr_pos[j])
                print(l)      
print(GlobalBest)








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

    