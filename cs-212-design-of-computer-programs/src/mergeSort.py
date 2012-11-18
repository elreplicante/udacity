'''
Created on 23/05/2012

@author: repli
'''
import random
import math
from numpy.oldnumeric.mlab import max
class Point:
    def __init__(self, x , y):
        self.x
        self.y
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str()
        

def dist(p0, p1):
    return math.sqrt((p1.x - p0.x)**2 + (p1.y - p0.y)**2)

def closesBF(points):
    i = 0;
    par = ()
    best = max
    while i < len(points) - 1:
        p0 = points[i]
        j =  i + 1
        while j < len(points):
            p1 = points[j]
            if par == () or dist(p0, p1) < best:
                best = dist(p0, p1)
                par = (p0, p1)
            j += 1
        i += 1
    return par

def closestPairDC(pointsX, pointsY):
    if len(pointsX) <= 3:
        pair = closesBF(pointsX)
        return pair
    leftX = pointsX[:len(pointsX)/2]
    rightX = pointsX[len(pointsX)/2:]
    med = pointsX[len(pointsX)/2]
    
    leftY = []
    rightY = []
    
    for p in pointsY:
        if p.x <= med.x:
            leftY.append(p)
        else:
            rightY.append(p)
    
    pairL = closestPairDC(leftX, leftY)
    pairR = closestPairDC(rightX, rightY)
    deltaL = dist(pairL[0], pairL[1]) 
    deltaR = dist(pairR[0], pairR[1])
    
    if deltaL < deltaR:
        delta = deltaL
        pair = pairL
    else:
        delta = deltaR
        delta = deltaR
        
    yS = []
    
    for p in pointsY:
        if abs(med.x - p.x) < delta:
            yS.append(p)
    deltaFinal = delta
    pairFinal = pair
    i = 0
    while i < len(yS) - 1:
        j = i + 1
        while j < len(yS) and abs(yS[j].y - yS[i].y) < delta:
            if dist(yS[j], yS[i]) < deltaFinal:
                deltaFinal = dist(yS[j], yS[i])
                pairFinal = (yS[j], yS[i])
            j += 1
        i += 1
    return pairFinal

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def ltX(p0, p1):
    return p0.x < p1.x

def ltY(p0, p1):
    return p0.y < p1.y
            
def mergeSort(lista, lt):
    if len(lista) < 2:
        return lista
    middle = len(lista) / 2
    left = mergeSort(lista[:middle], lt)
    right = mergeSort(lista[middle:], lt)
    return merge(left, right, lt)

numeros = []
for i in range(100):
    numeros.append(random.randint(0, 1000))
    
print numeros
print mergeSort(numeros)