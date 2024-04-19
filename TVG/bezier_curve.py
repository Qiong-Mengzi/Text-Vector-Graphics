import math
import xml.etree.ElementTree as ET
from .vArray import vColorArray
from .point import point
from copy import deepcopy

class BezierCurve(object):
    def __init__(self,start:tuple[float,float],end:tuple[float,float],ctrl_point:list[tuple[float,float]],*,color:int,lr:float,total_step = 10):
        self.value = (start,end,ctrl_point,color,lr,total_step)
        self.et = ET.Element('bezier',{'start':str(start[0])+' '+str(start[1]),'end':str(end[0])+' '+str(end[1]),'color':'0x{:08X}'.format(color),'lr':str(lr)})
        for ctrl in ctrl_point:
            self.et.append(ET.Element('ctrl',{'point':str(ctrl[0])+' '+str(ctrl[1])}))
        self.poccess = 0.0
    def __str__(self) -> str:
        return ET.tostring(self.et).decode()
    def __call__(self,Cloth:vColorArray):
        self.poccess = 0.0
        f = lambda t,d1,d2:(d1[0] + t * (d2[0] - d1[0]),d1[1] + t * (d2[1] - d1[1]))
        points:list[list[tuple[float,float]]] = [[]]
        points[0].append(self.value[0])
        points[0] += deepcopy(self.value[2])
        points[0].append(self.value[1])
        for i in range(len(points[0]),1,-1):
            tmp_points_list:list[tuple[float,float]] = []
            for j in range(0,i - 1,1):
                tmp_points_list.append(f(0,points[len(points[0])-i][j],points[len(points[0])-i][j+1]))
            points.append(tmp_points_list)
        self.poccess += 1 / (self.value[-1] + 1)
        for t in range(1, self.value[-1] + 1):
            for i in range(len(points[0]),1,-1):
                for j in range(0,i - 1,1):
                    points[len(points[0])-i + 1][j] = f(t/self.value[-1],points[len(points[0])-i][j],points[len(points[0])-i][j+1])
            point(points[-1][-1][0],points[-1][-1][1],color=self.value[3],lr=self.value[4])(Cloth)
            self.poccess += 1 / (self.value[-1] + 1)
        self.poccess = 1.0
