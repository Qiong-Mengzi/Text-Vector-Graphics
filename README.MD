# TVG (Text Vector Graphics)

~~*「この世界は美しいが、それは私のものではない...」*~~ [Chinese](/Sad/ZH/README-ZH.MD) | [Japanese](/Sad/JA/README-JA.MD)

A Vector Graphics format. (Useless)

~~[TVG API]()(Unwritten)~~

~~[TVG Format]()(Unwritten)~~

## Install by pip

```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

**TVG requires python>=3.9**

~~(Or the following error will appear.)
```
ERROR: Package 'python-text-vector-graphics' requires a different Python: 3.8.10 not in '>=3.9'
```

> However, removing the type annotation seems to be compatible with python 3.8 and below. (to be verified) (see `NOTE #1` at the bottom of the page)

+ Open all py files under `TVG/`.

+ Remove all type annotations. (a boooooooring job )

+ Remove the 8th line of `pytvg-setup/pylatest/setup.py`.

+ Repackage.
```bash
python pytvg-setup/pylatest/setup.py sdist
```

+ **Copy the `pytvg-setup/pylatest/setup.py` file to `dist/python-text-vector-graphics-0.0.1.tar.gz`**
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```

+ Finally, install TVG.
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

## Repackage

>For some reason, there may be a `fast` version (the current version is `pylatest`)
>
>Therefore, `setup.py` is placed in different folders

If you need to repackage the source code, use the following commands:
```bash
# Package
python pytvg-setup/pylatest/setup.py sdist
# Add setup.py
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```

## Samples

### Make a TVG file [(sample2.py)](/sample2.py)
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

If `numpy` and `cv2` are installed, the TVG file can be convert to PNG image.

*The default output color format of TVG is `RGBA` and the data type is `list[list[list[int]]]`.*

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

> NOTE: The image is drawn in `cloth.arr`.

### Read a TVG file [(sample1.py)](/sample1.py)

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

If `numpy` and `cv2` are installed (or other plotting libraries like `matplotlib`. `cv2` is used as an example in here), the picture can be viewed.

```python
# You need cv2 and Numpy to show the TVG image.
import cv2
import numpy as np

cv2.imshow('',cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA))
cv2.waitKey()
cv2.destroyAllWindows()
```

The the following picture will be shown.
![Sample](/Sad/correct.backup.png)

(The default background of TVG format is transparent.)

## License

The TVG format follows the MIT open source license.

## Release

## TVG 0.0.1

Supports [point](/TVG/point.py)，[segment](/TVG/line.py)，[circle](/TVG/circle.py)and[Bézier curves](/TVG/bezier_curve.py)

## NOTE

### #1

When I showed my teacher a small project ~~[Saiko2]()~~ at school, I found that the computer in the school computer room was pre-installed with python 3.8.

To solve this problem, it took me about 20 minutes to remove all the type annotations in it.

(This repository called `Saiko2` is inaccessible for some terrible reason...)

(Some Videos about `Saiko2`: [#1](https://www.bilibili.com/video/BV1Hw411x7Gr/) [#2](https://www.bilibili.com/video/BV1Y94y1V7tJ/))

### #2

My English is not very good, and I don't even know Japanese.

So... If there are translation errors, please point them out and I'll try to fix them. 
