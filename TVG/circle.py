from . import transform
from .vArray import vColorArray
import xml.etree.ElementTree as ET

class circle():
    def __init__(self,x:float,y:float,r:float,*,color:int,lr:float):
        self.value = (x,y,r,color,lr)
        self.et = ET.Element('circle',{'x':str(self.value[0]),'y':str(self.value[1]),'r':str(self.value[2]),'color':'0x{:08X}'.format(color),'lr':str(self.value[4])})
    def __str__(self):
        return ET.tostring(self.et).decode()
    def __call__(self,Cloth:vColorArray):
        length = max(*Cloth.size)
        c = self.value[3]
        for j in range(length):
            for i in range(length):
                if transform.isInCloth(i / length,j / length):
                    if transform.isOnCircle(i / length,j / length,self.value[0],self.value[1],self.value[2],cost=self.value[4]):
                        Cloth.setval(i,j,list(transform.ColorCut('RGBA',c)))