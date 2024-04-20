# TVG API

~~*「生きる。」*~~

## 画布

*class* TVG.**vColorArray**(arr:list[list[list[int]]] = [[[0,0,0,0]]])*

画布类，可传入一个画布数据

`arr`(画布数据)应是一个3D矩阵，如果内部的`list`长度不一致会导致接下来的操作出错

如果需要创建一个画布副本，请使用`copy.deepcopy`

+ vColorArray.**arr** (Read-Only)

    画布数据

+ vColorArray.**size** (Read-Only)

    画布大小(unit:px)

+ vColorArray.**getval**(x:int,y:int) -> list[int]

    获取某一像素

+ vColorArray.**setval**(x:int,y:int,color:list[int]) -> None

    设置某一像素

<br>

TVG.**vEmptyCloth**(size:tuple[int,int]) -> vColorArray

创建画布

*Fix: TVG 0.0.0-3修复：修改某一像素导致整列像素被修改的错误*

> 应尽可能创建宽高比为1:1的画布，在绘制过程中将以最长的边作为参照长度

## 乱七八糟的数学操作

TVG.transform.**t_val_for_testing**:list[Any] = []

记录每一次操作的结果，调试用

*调试完成后不应在此变量上面做任何操作*

<br>

TVG.transform.**Linear**(x:float) -> float

坐标归一化(大于1或小于0直接截断)

<br>

TVG.transform.**Sigmoid4**(x:float) -> float

坐标归一化($\frac{1}{\textit{e}^{-4 \; x + 2} + 1}$)

其中当$x = \frac{1}{2}$时其导数为$1$

> 此函数对生成结果有一定变形

<br>

TVG.transform.**ToColor**(color:str) -> int

颜色转换

颜色字符串格式为`0x??`(灰度)，`0x??????`(RGB)和`0x????????`(RGBA)，其中`?`为0~F

如果不符合格式，抛出`ValueError`

如果没有提供Alpha通道(透明度)，则默认为0xFF(仅灰度和RGB有效)

返回RGBA格式数据

*Future: Alpha通道处理计划在TVG 0.0.3中可用*

<br>

TVG.transform.**ColorCut**(Format:str,color:int) -> tuple[int,...]

按照`Format`中字段顺序提取像素的颜色通道，不分大小写

字段支持：

+ R : 红色
+ G : 绿色
+ B : 蓝色
+ A : 透明度

不支持的字段不会处理，字段可重复

返回一个元组，包含该像素提取的颜色通道

<br>

TVG.transform.**isInCloth**(x:float,y:float) -> bool

判断给定坐标是否在画布 $[0.0,1.0]$ 内

<br>

TVG.transform.**isInCircle**(x:float,y:float,cx:float,cy:float,r:float) -> bool

判断给定坐标是否在给定的圆内

$(x-cx)^2+(y-cy)^2-r^2<=0$

<br>

TVG.transform.**isOnCircle**(x:float,y:float,cx:float,cy:float,r:float,*,cost:float = 0.005) -> bool

判定给定坐标是否在给定圆上

此函数通常用于描绘圆的轮廓

由于点的坐标映射到画布上是离散的，故提供了cost作为误差值

$|(x-cx)^2+(y-cy)^2-r^2|<cost$

<br>

TVG.transform.**isOnLine**(x:float,y:float,A:float,B:float,C:float,*,cost:float = 0.005) -> bool

判定给定坐标是否在**直线**上(这是**直线**，不是**线段**)

A,B,C为直线的一般式参数 ($Ax+By+C=0$)

由于点的坐标映射到画布上是离散的，故提供了cost作为误差值

$|Ax+By+C|<cost$

> 应当将cost设置得较小，否则绘制出来的线会相当粗

## 基本图形

TVG.pytvg.**TVG_UnitLike**

`typing.Any`的别名，即所有基本图形类型

TVG_UnitLike只包含3个方法：`__init__`,`__str__`和`__call__`

其中`__str__`输出该图形的xml字符串

`__call__`只接受一个cloth参数，作为画布(`vColorArray`)

TVG_UnitLike的构造函数必然存在`lr`参数，本意为line-radius(线半径)即线上面每一个点的半径，但是由于底层实现所使用的算法不同导致该值所产生的效果无法统一

*Warning: 当前版本不支持处理Alpha通道数据，故会直接覆盖像素*

*Future: 在以后的版本中可能会将其改为所有基本图形类型的基类*

*Future: 在以后的版本中将修改遍历算法，以减小计算量与支持并行计算*

<br>

*class* TVG.**circle**(x:float,y:float,r:float,*,color:int,lr:float)

绘制一个圆

+ x 圆心的`x`坐标

+ y 圆心的`y`坐标

+ r 圆的半径

+ color 圆轮廓颜色

+ lr 误差

*这个类用于描绘圆的轮廓，如果要画实心圆，请使用`point`*

<br>

*class* TVG.**line**(x1:float,y1:float,x2:float,y2:float,*,color:int,lr:float)

绘制一条线段

+ x1,y2 第一个点的坐标

+ x2,y2 第二个点的坐标

+ color 线的颜色

+ lr 误差

*由于底层算法原因，同样的值相较于其他图形会让线段显得比较粗，故请使用相对较小的值*

<br>

*class* TVG.**point**(x:float,y:float,*,color:int,lr:float)

绘制一个点

+ x,y 点的坐标

+ color 点的颜色

+ lr 误差

*此处的`lr`即绘制的实心圆的半径*

<br>

*class* TVG.**BezierCurve**(start:tuple[float,float],end:tuple[float,float],ctrl_point:list[tuple[float,float]],*,color:int,lr:float,total_step = 10)

绘制一条贝塞尔曲线

+ start 起点坐标

+ end 终点坐标

+ ctrl_point 所有控制点坐标的列表

+ color 曲线颜色

+ lr 误差

+ total_step 采样点数量，默认为10

*应设置采样点数量为一个合适的值，否则会出现绘制的图像不连续或运算时间过长的情况*

BezierCurve.**process**:float

贝塞尔曲线的绘制进度，取值在[0.0,1.0]之间

可以另起一个线程绘制贝塞尔曲线，通过`process`成员变量查看其进度
```python
import threading
import time
import numpy as np
import cv2
import TVG

cloth = TVG.vEmptyCloth((400,400))
bc = TVG.BezierCurve((0.0,0.8),(1.0,0.7),[(0.7,0.0),(0.3,1.0)],color=0xFFC0C0FF,lr=0.01,total_step=1000)
th = threading.Thread(target=bc.__call__,args=(cloth,))

th.start()
while bc.poccess < 1.0:
    time.sleep(0.25)
    print(f'Drawing Bezier Curve: {int(bc.poccess*100)}%',end='   \r')
print()

cv2.imshow('',cv2.cvtColor(np.array(cloth.arr,np.uint8),cv2.COLOR_RGBA2BGRA))
cv2.waitKey()
cv2.destroyAllWindows()
```
这份代码会在绘制的时候在终端显示百分比进度

## 糟糕的封装

TVG.**TVG_VERSION**:str

当前TVG包能处理的TVG格式版本，通常可以向下兼容

<br>

TVG.pytvg.**TVG_Unit**:dict[str,dict[str,TVG_UnitLike]]

每一个版本中新的操作id与新的基本图形之间的映射

<br>

*class* TVG.pytvg.**TVG**()

TVG类，包含TVG Version, TVG Meta 和绘画顺序

TVG.**Width**:int (property)
图像的宽

TVG.**Height**:int (property)
图像的高

*Future: 在0.0.2版本中这两个属性将作为画布的默认大小*

TVG.**append**(unit:TVG_UnitLike) -> None

添加绘画步骤

TVG.**remove**(index:int) -> None

删除index处的操作

TVG.**newSize**(newSize:tuple[int,int])

更改`Width`和`Height`

<br>

TVG.pytvg.**TVG_OpenA**(*,version:str = '0.0.1',author:str = 'unknown',date:str = 'unknown',cloth_size:tuple[int,int]=(1,1)) -> TVG.pytvg.TVG

创建一个空的TVG

其中author和date是可选的

虽然选项中提供了date参数，但是在写入时仍会写入当前日期而非提供的值

version 指定TVG版本
cloth_size 指定画布大小

<br>

TVG.pytvg.**TVG_OpenB**(buffer:str) -> TVG.pytvg.TVG

解析TVG文件

buffer为待解析的数据

<br>

TVG.pytvg.**TVG_Show**(tvg:TVG,cloth:vColorArray) -> None

将TVG绘制在画布上

<br>

TVG.pytvg.**TVG_Save**(tvg:TVG) -> str

保存TVG文件

<br>

TVG.pytvg.**curse**() -> None

命令行接口，目前暂未实现
