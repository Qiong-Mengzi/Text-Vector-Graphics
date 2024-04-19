import xml.etree.ElementTree as ET
from typing import Any
import time

from .transform import ToColor
from .vArray import vColorArray

TVG_VERSION = '0.0.1'

# 0.0.1
from .point import point
from .line import line
from .circle import circle
from .bezier_curve import BezierCurve

TVG_UnitLike = Any

TVG_Unit:dict[str,dict[str,TVG_UnitLike]] = {
    '0.0.1':{
        'point':point,
        'line':line,
        'circle':circle,
        'bezier':BezierCurve
    }
}

class TVG():
    def __init__(self):
        self.version = ''
        # Author, Date, Width, Height
        self.meta:tuple[str,str,int,int] = ('','',1,1)
        self.cloth:list[TVG_UnitLike] = []
    
    @property
    def Width(self):
        return self.meta[2]
    
    @property
    def Height(self):
        return self.meta[3]
    
    def append(self,unit:TVG_UnitLike):
        self.cloth.append(unit)
    
    def remove(self,index:int):
        self.cloth.pop(index)

    def setSize(self,newSize:tuple[int,int]):
        self.meta = self.meta[:2] + newSize
    
def TVG_OpenA(*,version:str = '0.0.1',author:str = 'unknown',date:str = 'unknown',cloth_size:tuple[int,int]=(1,1)):
    tvg = TVG()
    tvg.version = version
    tvg.meta = (author,date,*cloth_size)
    return tvg

def TVG_OpenB(buffer:str):
    tvg = TVG()
    root = ET.fromstring(buffer)
    if root.tag != 'scroll':
        raise Exception('Not available scroll type : <scroll> is not root tag')
    if not 'type' in root.attrib:
        raise Exception('Cannot parse scroll type : Missing "type" attribute')
    if root.attrib['type'] != 'tvg':
        raise Exception('Not TVG type')
    if not 'version' in root.attrib:
        raise Exception('Not available TVG version : Missing "version" attribute')
    if not root.attrib['version'] in TVG_Unit:
        raise Exception('Not available TVG version : This version '+root.attrib['version']+' is not supported')
    else:
        tvg.version = root.attrib['version']
    if len(root) != 2:
        raise Exception('Invaild TVG type')
    
    meta = root[0]
    draw = root[1]

    if not 'Width' in meta.attrib or not 'Height' in meta.attrib:
        raise Exception('Unknown cloth size: Missing "Width" or "Height')
    else:
        w = int(meta.attrib['Width'])
        h = int(meta.attrib['Height'])
    author = meta.attrib.get('author','unknown')
    date = meta.attrib.get('date','unknown')
    
    tvg.meta = (author,date,w,h)
    tvg_version_supports = sorted(TVG_Unit)
    tvg_supports_index = 0
    for i in range(len(tvg_version_supports)):
        if tvg_version_supports[i] == tvg.version:
            tvg_supports_index = i
            break
    
    tvg_unit_dict = {}
    for k in tvg_version_supports[:tvg_supports_index + 1]:
        tvg_unit_dict.update(TVG_Unit[k])
    for unit in draw:
        if unit.tag == 'point':
            tvg.append(point(float(unit.attrib['x']),float(unit.attrib['y']),color=ToColor(unit.attrib['color']),lr=float(unit.attrib['lr'])))
        elif unit.tag == 'line':
            tvg.append(line(float(unit.attrib['x1']),float(unit.attrib['y1']),float(unit.attrib['x2']),float(unit.attrib['y2']),color=ToColor(unit.attrib['color']),lr=float(unit.attrib['lr'])))
        elif unit.tag == 'circle':
            tvg.append(circle(float(unit.attrib['x']),float(unit.attrib['y']),float(unit.attrib['r']),color=ToColor(unit.attrib['color']),lr=float(unit.attrib['lr'])))
        elif unit.tag == 'bezier':
            tmp_table = []
            tmp_text = unit.attrib['start'].split()
            start = (float(tmp_text[0]),float(tmp_text[1]))
            tmp_text = unit.attrib['end'].split()
            end = (float(tmp_text[0]),float(tmp_text[1]))
            color = ToColor(unit.attrib['color'])
            lr = float(unit.attrib['lr'])
            for ctrl in unit:
                tmp_text = ctrl.attrib['point'].split()
                points = (float(tmp_text[0]),float(tmp_text[1]))
                tmp_table.append(points)
            ts = int(unit.attrib.get('total','64'))
            tvg.cloth.append(BezierCurve(start,end,tmp_table,color=color,lr=lr,total_step=ts))
        else:
            pass
    return tvg

def TVG_Show(tvg:TVG,cloth:vColorArray):
    for unit in tvg.cloth:
        #print(unit)
        unit(cloth)

def TVG_Save(tvg:TVG):
    cloth_elem = ET.Element('draw')
    meta_elem = ET.Element('meta')
    root_elem = ET.Element('scroll')

    root_elem.attrib['version'] = tvg.version
    root_elem.attrib['type'] = 'tvg'
    
    meta_elem.attrib.update({
        'author':tvg.meta[0],
        'date':time.asctime(),
        'Width':str(tvg.Width),
        'Height':str(tvg.Height)
    })

    for unit in tvg.cloth:
        cloth_elem.append(unit.et)
    
    root_elem.append(meta_elem)
    root_elem.append(cloth_elem)

    ET.indent(root_elem)

    return ET.tostring(root_elem).decode()


def curse():
    print('Not support yet')
    pass
