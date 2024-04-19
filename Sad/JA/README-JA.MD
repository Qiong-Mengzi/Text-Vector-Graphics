# TVG (Text Vector Graphics)

~~*「この世界は美しいが、それは私のものではない...」*~~ [English](/README.MD) | [Chinese](/Sad/ZH/README-ZH.MD)

ベクターグラフィックス形式。何の役にも立たない気がします(笑)

~~[TVG API]()(Unwritten)~~

~~[TVG Format]()(Unwritten)~~

## pipでインストールする

```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

**TVG には python>=3.9 が必要です**

~~ (そうしないと、次のエラーが表示されます)~~
```
ERROR: Package 'python-text-vector-graphics' requires a different Python: 3.8.10 not in '>=3.9'
```

> ただし、型アノテーションを削除すると、PYTHON 3.8以下(検証予定)と互換性があるようです(ページ下部の「注#1」を参照)

+ `TVG/`の下にあるすべてのpyファイルを開きます。

+ すべての型注釈を削除します。 (退屈な仕事 T^T)

+ `pytvg-setup/pylatest/setup.py` の 8 行目を削除します。

+ `python pytvg-setup/pylatest/setup.py sdist`を再梱包します。

+ **`pytvg-setup/pylatest/setup.py` ファイルを `dist/python-text-vector-graphics-0.0.1.tar.gz` 圧縮ファイルにコピーします。**
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```

+ 最後にTVGをインストールします。
```bash
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
pip install ./python-text-vector-graphics-0.0.1
```

## ソースコードを再梱包する

~~(ソースコードを再パッケージ化する? I don't know which is th correct translation)~~

> なんらかの理由で、`fast`バージョンが続く場合があります。 (現在のバージョンは`pylatest`です)
>
> そのため、`setup.py` は別のフォルダに置かれます。

ソースコードを再パッケージ化する必要がある場合は、次のコマンドを使用します。
```bash
# Package
python pytvg-setup/pylatest/setup.py sdist
# Add setup.py
tar -zxvf python-text-vector-graphics-0.0.1.tar.gz
cp -v pytvg-setup/pylatest/setup.py python-text-vector-graphics-0.0.1
tar -zcvf python-text-vector-graphics-0.0.1.tar.gz python-text-vector-graphics-0.0.1
```

## 使用例

### TVG ファイルの生成 [(sample2.py)](/sample2.py)
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

「numpy」と「cv2」がインストールされている場合は、TVGファイルをpng画像として出力できます。

*TVGのデフォルトのカラー形式は「RGBA」で、データ型は `list[list[list[int]]]`です*

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

> 注:画像は「cloth.arr」に描画されます。

### TVG ファイルの読み取り [(sample1.py)](/sample1.py)

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

`numpy` と `cv2` がインストールされている場合(または `matplotlib` のような他のプロットライブラリ。 `cv2` を例にとります)、画像を表示できます。

```python
# You need cv2 and Numpy to show the TVG image.
import cv2
import numpy as np

cv2.imshow('',cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA))
cv2.waitKey()
cv2.destroyAllWindows()
```

すると、下の画像が表示されます。

![Sample](/Sad/correct.backup.png)

(TVG形式のデフォルトの背景は透明です)

## License

The TVG format follows the MIT open source license.

## Release

### TVG 0.0.1

[Point](/TVG/point.py)、[Segment](/TVG/line.py)、[Circle](/TVG/circle.py)、[Bézier curves](/TVG/bezier_curve.py) がサポートされています。

## NOTE

### 注#1

学校で先生にちょっとしたプロジェクトを見せてあげる
~~[Saiko2]()~~、学校のコンピュータ室のコンピュータにはpython3.8がプリインストールされていることがわかりました。

この問題を解決するために、その中のすべての型注釈を削除するのに約20分かかりました。

(This repository called `Saiko2` is inaccessible for some terrible reason...)

(Some Videos about `Saiko2`: [#1](https://www.bilibili.com/video/BV1Hw411x7Gr/) [#2](https://www.bilibili.com/video/BV1Y94y1V7tJ/))

### 注#2

私の英語はあまり上手ではなく、日本語もわかりません。

だから。。。 翻訳エラーがある場合は、それらを指摘してください、そして私はそれらを修正しようとします、ありがとうニャー。
