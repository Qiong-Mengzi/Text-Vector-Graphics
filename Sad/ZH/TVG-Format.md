# TVG Format

~~*「しかし、すべてが私にとって悪いことになりそうです。」*~~

***所有节点的tag必须小写***

## 根节点

&lt;scroll&gt;

包含`version`(TVG版本)和`type`(卷轴类型为TVG格式)

*我有可能会在其他项目的xml文档中使用&lt;scroll&gt;作为根节点，故需要标明类型*

### TVG 元数据

&lt;meta&gt;

根节点的第一个子节点，包含 `author`(opt.),`date`(opt.),`Width` 和 `Height` 四个属性

*date由time.asctime()函数提供*

### TVG 绘图步骤

&lt;draw&gt;

根节点的第二个子节点，其中的每一个子节点都是一个基本图形

如果出现了无法识别的基本图形(通常是在使用低版本TVG包解析高版本TVG文件时)，则会忽略它们

受支持的基本图形请参阅[pytvg.py](/TVG/pytvg.py)的`TVG_Unit`常量


