from . import transform
from .vArray import vColorArray
import xml.etree.ElementTree as ET

class line():
    def __init__(self,x1:float,y1:float,x2:float,y2:float,*,color:int,lr:float):
        self.value = (x1,y1,x2,y2,color,lr)
        self.et = ET.Element('line',{'x1':str(x1),'y1':str(y1),'x2':str(x2),'y2':str(y2),'color':'0x{:08X}'.format(color),'lr':str(lr)})
    def __call__(self,Cloth:vColorArray):
        length = max(*Cloth.size)
        color = self.value[4]
        A = self.value[3] - self.value[1]
        B = self.value[0] - self.value[2]
        C = self.value[2]*self.value[1] - self.value[0]*self.value[3]
        x_1,y_1,x_2,y_2 = self.value[:4]
        x1 = length*min(x_1,x_2)
        x2 = length*max(x_1,x_2)
        y1 = length*min(y_1,y_2)
        y2 = length*max(y_1,y_2)
        for j in range(0,length):
            for i in range(0,length):
                if transform.isInCloth(i / length,j / length) and i >= x1 and i < x2 and j >= y1 and j <= y2:
                    if transform.isOnLine(i/length,j/length,A,B,C,cost=self.value[5]):
                        Cloth.setval(i,j,list(transform.ColorCut('RGBA',color)))
    def __str__(self) -> str:
        return ET.tostring(self.et).decode()