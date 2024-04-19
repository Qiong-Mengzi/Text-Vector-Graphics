# TVG (Text Vector Graphics)

~~*「この世界は美しいが、それは私のものではない...」*~~ [English](/README.MD) | [Japanese](/Sad/JA/README-JA.MD)

一个矢量图格式，虽然但是没有什么用就对了（逃

~~[TVG API]()(Unwritten)~~

~~[TVG Format]()(Unwritten)~~

## pip安装：

```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

**TVG 需要python3.9及以上的版本**

~~(否则会出现如下报错)~~
```
ERROR: Package 'python-text-vector-graphics' requires a different Python: 3.8.10 not in '>=3.9'
```

> 虽然但是，将类型注解去掉似乎可以兼容 python 3.8 及以下的版本(待验证)(见页面底部的`NOTE #1`)

+ 打开`TVG/`下的所有py文件

+ 将所有的类型注解去掉(一个枯燥的工作ww)

+ 去掉`pytvg-setup/pylatest/setup.py`的第8行

+ 重新打包 `python pytvg-setup/pylatest/setup.py sdist`

+ **将`pytvg-setup/pylatest/setup.py`文件复制到`dist/python-text-vector-graphics-0.0.1.tar.gz`**
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```
+ 然后安装TVG
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

## 打包

> 由于一些原因，后续可能会出现`fast`版本(当前版本为`pylatest`)
> 
> 故`setup.py`放在了不同的文件夹内

如果需要对源码重新打包，请使用如下符文：
```bash
# Package
python pytvg-setup/pylatest/setup.py sdist
# Add setup.py
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```

## 示例

### 生成TVG [(sample2.py)](/sample2.py)
```python
import TVG
from TVG.pytvg import TVG_OpenA,TVG_Save,TVG_Show

# Create a new TVG, Width = 200, Height = 200
tvg = TVG_OpenA()
tvg.setSize((200,200))

# Blue Color
Blue = TVG.ToColor('0x0000ff')

# Add a circle
tvg.append(TVG.circle(x=0.5,y=0.5,r=0.4,color=Blue,lr=0.008))

# Add two lines
tvg.append(TVG.line(x1=0.3,y1=0.5,x2=0.5,y2=0.7,color=Blue,lr=0.002))
tvg.append(TVG.line(x1=0.5,y1=0.7,x2=0.7,y2=0.3,color=Blue,lr=0.004))

# Save TVG
with open('TVG-samples/correct.tvg','w') as f:
    f.write(TVG_Save(tvg))
```
如果安装有`numpy`和`cv2`，则可以输出为png图片

*TVG的默认输出颜色格式为`RGBA`,类型为`list[list[list[int]]]`*

```python
# You need cv2 and numpy to save TVG image
import cv2
import numpy as np

# Convert TVG to RGBA
# It may take lots of time...
cloth = TVG.vEmptyCloth((tvg.Width,tvg.Height))
TVG_Show(tvg,cloth)

# Save PNG Image
cv2.imwrite('TVG-samples/correct.png',
    cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA)
)
```

> NOTE: 图像绘制在`cloth.arr`中

### 读取TVG [(sample1.py)](/sample1.py)

```python
import TVG
from TVG.pytvg import TVG_OpenB,TVG_Show

# Open a TVG image
with open('TVG-samples/correct.tvg','r') as f:
    tvg = TVG_OpenB(f.read())

# Create a cloth witch size is your need
cloth = TVG.vEmptyCloth((200,200))

TVG_Show(tvg,cloth)
```

如果安装有`numpy`和`cv2`(或其他绘图库，如`matplotlib`。这里以`cv2`为例)，则可以查看图片

```python
# You need cv2 and Numpy to show the TVG image.
import cv2
import numpy as np

cv2.imshow('',cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA))
cv2.waitKey()
cv2.destroyAllWindows()
```

然后就可以看到

![Sample](/Sad/correct.backup.png)

(TVG默认背景是透明的)

## License

MIT协议

## Release

### TVG 0.0.1

支持[点](/TVG/point.py)，[线段](/TVG/line.py)，[圆](/TVG/circle.py)和[贝塞尔曲线](/TVG/bezier_curve.py)

## NOTE

### #1

在学校给我的老师展示一个小的项目
~~[Saiko2]()~~时发现学校机房的电脑预装的是python3.8

为了解决这个问题，我花了大约20分钟将里面所有的类型注解全部删除了

(This repository called `Saiko2` is inaccessible for some terrible reason...)

(Some Videos about `Saiko2`: [#1](https://www.bilibili.com/video/BV1Hw411x7Gr/) [#2](https://www.bilibili.com/video/BV1Y94y1V7tJ/))

### #2

我的英语并不好，并且我甚至不会日语

所以...如果有翻译错误请指出来，我会尝试修正它们的 QwQ
