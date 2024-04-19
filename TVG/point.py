from . import transform
from .vArray import vColorArray
import xml.etree.ElementTree as ET

class point():
    def __init__(self,x:float,y:float,*,color:int,lr:float):
        self.value = (x,y,color,lr)
        self.et = ET.Element('point',{'x':str(self.value[0]),'y':str(self.value[1]),'color':'0x{:08X}'.format(color),'lr':str(self.value[3])})
    def __str__(self):
        return ET.tostring(self.et).decode()
    def __call__(self,Cloth:vColorArray):
        if transform.isInCloth(*self.value[:2]):
            length = max(*Cloth.size)
            c = self.value[2]
            for j in range(length):
                for i in range(length):
                    if transform.isInCloth(i / length,j / length):
                        if transform.isInCircle(i / length,j / length,self.value[0],self.value[1],self.value[3]):
                            Cloth.setval(i,j,list(transform.ColorCut('RGBA',c)))

