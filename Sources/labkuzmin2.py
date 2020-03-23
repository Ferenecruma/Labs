import numpy as np
import random
import math 
import copy


def FitnessFunc(arr): #Функція Розстрігіна для н-вимірного випадку
    result=0
    for i in range(len(arr)-1):
        result+=(1-arr[i])**2+100*(arr[i+1]-arr[i]**2)**2
    return result

N, M, eps = 10, 2, 0.1 #N - Кількість членів популяції,M - Розмірність простору 
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
    return Gdec 


def Mutation(G,L): #L - Лист індексів впорядкованих за зменшенням значення фітнес функції
    for count, index in enumerate(L):
        for param in G[index]:
            print("param: {}".format(param))
            for i in range(len(param)):
                randomNum = random.uniform(0,1)
                if(param[i] == '1' and randomNum < 2*(1 - 1/(count+1))):
                    param[i] = '0'
                elif(randomNum < 2*(1 - 1/(count+1))):
                    param[i] = '1'
            print("param1: {}\n".format(param))
            


def Crossover(G,BestIndex,SecondBestIndex): #Mlist и Flist - списки чисел из которых будут формироватся пары 
    Best, SecondBest= G[BestIndex], G[SecondBestIndex]
    for BitsB,BitS in zip(Best,SecondBest):
        randomPoint = random.randint(0,len(BitsB))
        for i in range(randomPoint):
            BitS[i], BitsB[i] = BitsB[i], BitS[i]
    return Best, SecondBest
# ACodDecimal(ACodBinary(Gdec=GenerationDec()))

#тепер треба реалізувати вибір найкращого члена популяції та передачі його генів іншим членам

Gdec = GenerationDec() #Початкова популяція
i = 0
while(i<10):
    fitnessValues = {}
    sortedIndexes = []

    for count, row in enumerate(Gdec):
        fitnessValues[count] = FitnessFunc(row)
    for w in sorted(fitnessValues,key = fitnessValues.get,reverse=False): #Шукаємо значення фітнес функції для популяції і упорядковуємо
        sortedIndexes.append(w)

    Bdec = ACodBinary(Gdec) #Переводимо числа в бінарний код
    Best,SecondBest = Crossover(Bdec,sortedIndexes[0],sortedIndexes[1]) #найкращі дві особини кросовирятся - створюють дві нові
    Bdec[sortedIndexes[-1]], Bdec[sortedIndexes[-2]] = SecondBest, Best #Добавляємо нащадків в популяцію,замість найгірших
    Mutation(Bdec,sortedIndexes) #Найкращі мутують менше
    Gdec = ACodDecimal(Bdec)
    # print("Gdec: {}".format(Gdec))
    i+=1

