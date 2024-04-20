import math

t_val_for_testing = [] # For Test

def Linear(x:float):
    if x > 1.0:
        return 1.0
    elif x < 0.0:
        return 0.0
    return x

def Sigmoid4(x:float):
    return 1 / (1 + math.exp(4 * (0.5 - x)))

def ToColor(color:str):
    if not len(color) in (2+2,6+2,8+2):
        raise ValueError(color)
    if color[:2] != '0x':
        raise ValueError(color)
    val = color[2:]
    if len(val) == 2:
        val = val*3
    if len(val) == 6:
        val += 'ff'
    return int('0x'+val,base=16)

def ColorCut(Format:str,color:int):
    m:list[int] = []
    for c in Format:
        if c in 'Rr':
            m.append((color&0xFFFFFFFF)>>24)
        elif c in 'Gg':
            m.append((color&0xFFFFFF)>>16)
        elif c in 'Bb':
            m.append((color&0xFFFF)>>8)
        elif c in 'Aa':
            m.append((color&0xFF)>>0)
    return tuple(m)

def isInCloth(x:float,y:float):
    return 0 <= x and x <= 1 and 0 <= y and y <= 1

def isInCircle(x:float,y:float,cx:float,cy:float,r:float):
    ret = (x-cx)**2 + (y-cy)**2 - r**2
    return ret <= 0

def isOnCircle(x:float,y:float,cx:float,cy:float,r:float,*,cost:float = 0.005):
    ret = abs((x-cx)**2 + (y-cy)**2 - r**2)
    return ret < cost

def isOnLine(x:float,y:float,A:float,B:float,C:float,*,cost:float = 0.005):
    ret = abs(A*x + B*y + C)
    #print(x,y,ret)
    return ret < cost