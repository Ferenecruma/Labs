import numpy as np
import random
import math 


N, M, eps = 1, 1, 0.1
Xmin, Xmax = [], []
for i in range(M):
    temp1, temp2 = random.uniform(-10, 10), random.uniform(-10, 10)
    if(temp1 > temp2):
        Xmax.append(temp1)
        Xmin.append(temp2)
    else:
        Xmax.append(temp2+0.00001)
        Xmin.append(temp1)


def GenerationDec(N=N, M=M, Xmin=Xmin, Xmax=Xmax):
    matr = np.zeros((N, M+1))
    for i in range(N):
        for j in range(M):
            matr[i, j] = random.uniform(Xmin[j], Xmax[j])
    return matr


def BinDecParam(eps):#Функція викликаєтся один раз для знаходження параметрів переводу чисел в різні системи
    nn, dd, NN = [], [], []
    NN.append(0)
    for i in range(M):
        nn.append(math.floor(math.log2((Xmax[i]-Xmin[i])/eps))+1)
        dd.append((Xmax[i]-Xmin[i])/2**nn[-1])
        NN.append(NN[-1]+nn[-1])
    return nn, dd, NN

nn, dd, NN= BinDecParam(eps)

def CodBinary(xdec, xmin, I, d):
    xx = math.floor((xdec-xmin)/d)
    binarr = list(np.binary_repr(xx, I))
    binarr.reverse()
    return binarr


def CodDecimal(xbin, xmin, d):
    xbin.reverse()
    xdec1 = int(''.join(xbin), 2)
    xdec = xmin + d*xdec1
    return xdec


def ACodBinary(N, M, Gdec, Xmin):
    Gbin = Gdec.copy()
    for i in range(N):
        for j in range(M):
            Gbin[i,j] = CodBinary(Gbin[i][j],Xmin[i],nn[i],dd[i])
    return Gbin


def ACodDecimal(N, M, Gbin, Xmin):
    Gdec = Gbin.copy()
    for i in range(N):
        for j in range(M):
            Gdec[i,j] = CodDecimal(Gdec[i][j],Xmin[i],dd[i])
    return Gdec 


def Mutation(G,p):
    Gmut = G.copy()
    for i in range(len(G)):
        for j in range(len(G[0])):
            prob = random.random()
            if(prob > p):
                if(Gmut[i,j] == '1'):
                    Gmut[i,j] = '0'
                else:
                    Gmut[i,j] = '1'
    return Gmut


def Crossover(N,G,Mlist,Flist):#Mlist и Flist - списки чисел из которых будут формироватся пары 
    for i in range(len(Mlist)):
        cros = random.randint(1,len(G[0]))
        for j in range(cros):
            G[Mlist[i],j], G[Flist[i],j] = G[Flist[i],j], G[Mlist[i],j]

