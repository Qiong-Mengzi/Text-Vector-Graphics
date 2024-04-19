from copy import deepcopy

class vColorArray(object):
    def __init__(self,arr:list[list[list[int]]] = [[[0,0,0,0]]]):
        self.arr = arr
        self.size = (len(arr),len(arr[0]))
    
    def getval(self,x:int,y:int):
        return self.arr[y][x]
    
    def setval(self,x:int,y:int,color:list[int]):
        self.arr[y][x] = color

def vEmptyCloth(size:tuple[int,int]):
    r = [0,0,0,0]
    t = []
    for i in range(size[0]):
        t.append(deepcopy(r))
    r = t
    t = []
    for i in range(size[1]):
        t.append(deepcopy(r))
    r = t
    return vColorArray(r)

