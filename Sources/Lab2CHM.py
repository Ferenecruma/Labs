import pathlib
import numpy as np
import matplotlib.pyplot as plt
from math import log

def points_from_function(f, a, h, n, Array = True):
    x = h*np.arange(n+1) + a
    y = x.copy()
    if(Array):
        y = f(x)
    else:
        for i in range(n+1):
            y[i] = f(x[i])
            
    return x, y

n = 30 #Кількість інтервалів  
a = 1. #Початок інтервалу
b = 2. #Кінець інтервалу
h = (b-a)/n #Довжина інтервалу
eps = 10**(-5)


def new_points_with_nuton(X,x,F):#a - скаляр
    n1 = x.shape[0]
    Result = np.zeros(X.shape) + F[n1-1]
    for i in range(n1-1):
        Result *= (X - x[n1-(i+2)])
        Result += F[n1-(i+2)]

    return Result


def predict_d_f_with_nuton(X,x,y, rev = False):
    if(rev):
        x = np.flip(x)
        y = np.flip(y)
    n1 = x.shape[0]
    Dx = x
    F = y.copy()
    Fy = y.copy()

    for i in range(n1 - 1):
        Dx = x[:-(i+1)] - x[(i+1):]
        F[i] = Fy[0]
        Fy = (Fy[:-1] - Fy[1:])/Dx
    F[n1-1] = Fy[0]

    X_plus = X + eps
    X_minus = X - eps
    
    return (new_points_with_nuton(X_plus,x,F)-new_points_with_nuton(X_minus,x,F))/(X_plus - X_minus) #Рекурсувно знаходимо точки


def pol_without_i(a,x,i):#a - скаляр
    x_a = x - a
    x_a[i] = 1
    return x_a.prod()


def new_point_with_lagrange(a,x,y):#a - скаляр
    n1 = x.shape[0]
    
    result = 0
    for i in range(n1):
        result += y[i]*( pol_without_i(a,x,i)/pol_without_i(x[i],x,i) )
        
    return result

def predict_d_f_with_lagrange(X,x,y, rev = False):
    Result = np.zeros(X.shape)
    for i in np.arange(X.shape[0]):
        Result[i] = (new_point_with_lagrange(X[i]+eps, x,y) - new_point_with_lagrange(X[i]-eps, x,y) )/(2*eps)
    return Result

def d_f_with_rizn2(x,y):#x должно иметь минимум 3 елемента
    Result = np.zeros(x.shape)
    Result[1:-1] = (y[:-2] - y[2:])/(x[:-2] - x[2:])
    Result[0] = Result[1]
    Result[-1] = Result[-2]
    return Result


def predict_d_f_with_rizn2(X,x,y):
    return d_f_with_rizn2(x,y)


def d_f_with_rizn4(x,y):#x должно иметь минимум 5 елемента
    Result = np.zeros(x.shape)
    Result[1:-1] = (y[:-2] - y[2:])/(x[:-2] - x[2:])
    Result[2:-2] *= 4./3
    Result[2:-2] -= (1./3)*( (y[:-4] - y[4:])/(x[:-4] - x[4:]) )
    Result[0] = Result[1]
    Result[-1] = Result[-2]
    return Result


def predict_d_f_with_rizn4(X,x,y): # Функція заглушка
    return d_f_with_rizn4(x,y)

    

def test_der(F,f,d_f,x0,h,predict_d_f, i = 0):#predict_d_f - функция предсказатель
    x, y = points_from_function(F, x0, h, n)
    predict_d = predict_d_f(x,x,y) # Наближення першої похідної
    plt.plot(x,f(x))
    plt.plot(x,predict_d)
    plt.title("1 похідна")
    plt.legend(["функція", "набилження"])
    plt.savefig(str(pathlib.Path().absolute()) + "\\" + str(i) + 'figdx.png',format = "png")
    plt.close()

    predict_dd = predict_d_f(x,x,predict_d) # Наближення другої похідної
    plt.plot(x,d_f(x))
    plt.plot(x,predict_dd)
    plt.title("2 похідна")
    plt.legend(["функція", "наближення"])
    plt.savefig(str(pathlib.Path().absolute()) + '\\' + str(i) + 'figdxx.png',format = "png")
    plt.close()




F = lambda x: 1/3*(np.log(x/(2*x + 3))) #Інтеграл функції
f = lambda x: 1./(x*(3+2*x)) #Функція
df = lambda x: (-4*x - 3)/(x**2*(3 + 2*x)**2) #Похідна


test_der(F,f,df,a,h,predict_d_f_with_nuton,0)
test_der(F,f,df,a,h,predict_d_f_with_lagrange,1)
test_der(F,f,df,a,h,predict_d_f_with_rizn2, 2)
test_der(F,f,df,a,h,predict_d_f_with_rizn4,3)


#Формули Ньютона-Котеса


x, y = points_from_function(f, a, h, n)

AnalyticalValue = F(b) - F(a)
SimpsonsRule = h/3*(y[0] + 2*sum(y[2:n-1:2]) + 4*sum(y[1:n:2]) + y[-1]) #Формула Сімпсона
SimpsonsRule38 = 3*h/8*(y[0] + 3*sum(y[1:n-1:3]) + 3*sum(y[2:n:3]) + 2*sum(y[3:n-2:3]) + y[-1]) #Формула Сімпсона 3/8

BoolesRule = 2*h/45*(7*y[0] + 7 * y[-1] + 32*sum(y[1:n:2]) + 12*sum(y[2:n-1:4]) + 14*sum(y[4:n-3:4])) #Формула Буля
print("Аналітичне значення : " + str(AnalyticalValue))

print("Simposns Rule : " + str(SimpsonsRule) + "   Difference : " + str(abs(AnalyticalValue - SimpsonsRule)))
print("Simpson38 Rule : " + str(SimpsonsRule38) + "   Difference : " + str(abs(AnalyticalValue - SimpsonsRule38)))
print("Booles Rule : " + str(BoolesRule) + "   Difference : " + str(abs(AnalyticalValue - BoolesRule)))


