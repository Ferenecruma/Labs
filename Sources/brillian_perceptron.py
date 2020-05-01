import numpy as np
w = np.array([0,0])
x1,x2,x3 = np.array([-1,1]), np.array([0,-1]), np.array([10,1])
y1,y2,y3 =  1,-1,1
b = 0
cond = True

while (cond):
    
    if np.dot(x1,w)*y1 + b > 0:
        cond1 = False
    else:
        print(w,b)
        w += x1*y1
        b += y1
        cond1 = True
    
    if np.dot(x2,w)*y2 + b > 0:
        cond2 = False
    else:
        print(w,b)
        w += x2*y2
        b += y2
        cond2 = True
    if np.dot(x3,w)*y3 + b > 0:
        cond3 = False
    else:
        print(w,b)
        w += x3*y3  
        b += y3
        cond3 = True
    cond = cond1 or cond2 or cond3
print(w,b)