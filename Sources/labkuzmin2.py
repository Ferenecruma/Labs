import numpy as np
import random
import math 


def FitnessFunc(arr): #Функція Розстрігіна для н-вимірного випадку
    result=0
    for i in range(len(arr)-1):
        result+=(1-arr[i])**2+100*(arr[i+1]-arr[i]**2)**2
    return result

N, M, eps = 10, 1, 0.00001 #N - Кількість членів популяції,M - Розмірність простору 
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
    print(matr)
    return matr


def BinDecParam(eps): #Функція викликаєтся один раз для знаходження параметрів переводу чисел в різні системи
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
    # print("xx: {}".format(xx))
    # print("d: {} xmin: {}".format(d,xmin))
    binarr = list(np.binary_repr(xx, I))
    return binarr


def CodDecimal(xbin, xmin, d):
    xdec1 = int(''.join(xbin), 2)
    # print("xdec: {} ".format(xdec1))
    # print("d: {} xmin: {}".format(d,xmin))
    xdec = xmin + d*xdec1
    return xdec


def ACodBinary(Gdec , N=N, M=M, Xmin=Xmin):
    Gbin = [[0]*M for i in range(N)] #Не можна заповнювати np.array ітераційними елементами?
    for i in range(N):
        for j in range(M):
            Gbin[i][j] = CodBinary(Gdec[i][j],Xmin[j],nn[j],dd[j])
    return Gbin


def ACodDecimal(Gbin ,N = N, M = M, Xmin = Xmin):
    Gdec = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            Gdec[i][j] = CodDecimal(Gbin[i][j],Xmin[j],dd[j])
    for row in Gdec:
        print(row)
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


def Crossover(G,Mlist,Flist): #Mlist и Flist - списки чисел из которых будут формироватся пары 
    for i in range(len(Mlist)):
        cros = random.randint(1,len(G[0]))
        for j in range(cros):
            G[Mlist[i],j], G[Flist[i],j] = G[Flist[i],j], G[Mlist[i],j]

# ACodDecimal(ACodBinary(Gdec=GenerationDec()))

#тепер треба реалізувати вибір найкращого члена популяції та передачі його генів іншим членам
fitnessValues = {}
sortedIndexes = []
Gdec = GenerationDec()
for count, row in enumerate(Gdec):
    fitnessValues[count] = FitnessFunc(row)
for w in sorted(fitnessValues,key = fitnessValues.get,reverse=True):
    sortedIndexes.append(w)
    print(w, fitnessValues[w])
print(sortedIndexes)
print(ACodBinary(Gdec))