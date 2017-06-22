# 数据的导入导出

> * 本节内容，以数据格式为子章节，分别介绍其导入和导出时应该注意的事项。
> * 注意事项：在 Mathematica 的字符串中，反斜杠“\”是转义字符。所以文件路径中的反斜杠“\”要双写为“\\”。但是更建议您使用斜杠“/”替代反斜杠，这样在 Mac 或 Linux 上也是通用的。

## 保存 Mathematica 符号：函数，变量
### 介绍
* **优点**： 容易导入与导出，不用考虑编码问题
* **缺点**： 作为 Mathematica 的专有数据格式，不便于其它软件导入
* **扩展名**： 不限，建议使用“.wl”，或不使用扩展名
* **导入函数**： `Get` (`<<`)
* **导出函数**： `DumpSave` | `Save` | `Put` (`>>`) | `PutAppend` (`>>>`)

### 导出 Mathematica 符号
#### 使用 **`DumpSave`** 保存符号【推荐】
* [帮助](http://reference.wolfram.com/language/ref/DumpSave.html)
* `DumpSave` 以二进制格式写出定义，该格式是 Wolfram 语言输入的**最优化格式**
* `DumpSave` 仅保存指定符号，**不保存依赖函数**
* `DumpSave` 保存到已存在的文件时，以追加方式保存。建议先删除之前已经保存过的文件，以避免数据冗余
* 由 `DumpSave` 生成的文件能使用 `Get` 读出
* 由 `DumpSave` 生成的文件只有在与生成它的计算机系统类型相同的系统上才能被读出
* 由 `DumpSave` 生成的文件的文件名通常以 .mx 结尾
* `DumpSave` 不会保存开放的流和连接对象
* `DumpSave` 适用于本地对象
* ...


<!--sec data-title="示例：使用 DumpSave 保存函数与变量" data-id="section1" data-show=true data-collapse=true ces-->
```mma{% raw %}
(* 定义测试函数 *)
g[x_] := Sin[x];
fPower2[x_] := g[x]^2;
(* 为测试函数设置列表属性 *)
SetAttributes[fPower2, Listable];
(* 生成一个10阶随机矩阵 data *)
data = RandomReal[1, {10, 10}];
(* 将生成的随机矩阵中每个元素平方 data2 *)
data2 = fPower2[data];
(* 保存1个函数和2个变量到 "D:/test.wl" *)
DumpSave["D:/test.wl", {fPower2, data, data2}];(* 注：函数 g 将不被保存 *)
{% endraw %}
```
<!--endsec-->


#### 使用 **`Save`** 保存符号
* [帮助](http://reference.wolfram.com/language/ref/Save.html)
* `Save` 使用 `FullDefinition` 来包含辅助定义：**保存依赖函数**
* `Save` 保存到已存在的文件时，以追加方式保存。建议先删除之前已经保存过的文件，以避免数据冗余
* `Save` 在 `InputForm` 中输出定义
* `Save` 用 `Names` 来查找名称与给定字符串模式匹配的符号
* `Save` 可作用于本地对象和云对象.

<!--sec data-title="示例：使用 Save 保存函数与变量" data-id="section2" data-show=true data-collapse=true ces-->
```mma{% raw %}
(* 定义测试函数 *)
g[x_] := Sin[x];
fPower2[x_] := g[x]^2;
(* 为测试函数设置列表属性 *)
SetAttributes[fPower2, Listable];
(* 生成一个10阶随机矩阵 data *)
data = RandomReal[1, {10, 10}];
(* 将生成的随机矩阵中每个元素平方 data2 *)
data2 = fPower2[data];
(* 保存1个函数和2个变量到 "D:/test.wl" *)
Save["D:/test.wl", {fPower2, data, data2}];(* 注：函数 g 将被保存 *)
{% endraw %}
```
<!--endsec-->

#### 使用 **`Put` (>>) | `PutAppend` (>>>)** 保存表达式【不推荐】
* [帮助：`Put`](http://reference.wolfram.com/language/ref/Put.html)
* [帮助：`PutAppend`](http://reference.wolfram.com/language/ref/PutAppend.html)
* 两个函数都是用于保存表达式返回值的，区别于符号，它们并不保存函数定义，与不保存变量名
* `Put` (`>>`) 以覆盖方式写入
* `PutAppend` (`>>>`) 以追加方式写入

### 导入 Mathematica 符号
```mma{% raw %}
Clear["Global`*"](* 消除刚刚定义的符号 *)
<< "D:/test.wl"(* 导入刚刚保存的符号 *)
{% endraw %}
```

## Excel 文件的导入导出
* **优点**： 不需要考虑编码问题（包含非英文字符时）
* **缺点**： 导入与导出都需要较长的时间，有大小限制，不支持 Excel 样式
* **扩展名**：.xlsx | .xls
* **注意事项**：默认情况下，导入与导出数据都是3维列表
* **导入函数**： `Import`
* **导出函数**： `Export`

### Excel 文件介绍
* Excel 的数据结构：表（Sheet），行（Row），列（Column），单元格（Cell）。每个单元格由“表+行+列”确定。
* Excel 数据导入到 Mathematica 之后，默认是 3 维列表。
* .xls  后缀对应于 95, 97, 2000, 2003 版本的 Excel 文件（最大 65536 行， 256 列），不建议使用。
* .xlsx 后缀对应于 2007 以上版本的 Excel 文件（最大 1048576 行， 16384 列）。


### 导出 Excel 文件
<!--sec data-title="示例：导出数据到 Excel 文件" data-id="section3" data-show=true data-collapse=true ces-->
```mma{% raw %}
table1={{1},{2,3},{4,5,6}};(* 对应于 Excel 中的 Sheet1 ，每行的列数可以不同 *)
table2={{7,,8},{},{9}};(* 对应于 Excel 中的 Sheet2 ，空单元格和空行要留出来 *)
excelData={table1,table2};(* 将上面两张2维列表组合成一个3维列表 *)
Export["D:/test.xlsx", excelData](* 将3维列表数据导出到 Excel 文件中 *)
Export["D:/test.xlsx", {table1}](* 将2维列表数据导出到 Excel 文件中时，要在2维列表外加一层花括，以保证其3维列表结构。虽然不加也可以导出，但导出的 Excel 文件会存在一些小问题。 *)
{% endraw %}
```
<!--endsec-->


### 导入 Excel 文件
* 总是处理整个文件
* 支持的元素："Data", "FormattedData", "Formulas", "Images", "Sheets"

<!--sec data-title="示例：从 Excel 文件导入数据或其它被支持的元素" data-id="section4" data-show=true data-collapse=true ces-->
```mma{% raw %}
(* 最简单的导入 *)
Import["D:/test.xlsx"];(* 导入整个 Excel 文件，总是返回3维列表，第1层为 Sheet 层，每个 Sheet 都是一个2维列表 *)
Import["D:/test.xlsx"][[1]];(* 导入整个 Excel 文件，导入后只取第1个 Sheet *)

(* 指定要导入的元素： "Data", "FormattedData", "Formulas", "Images", "Sheets" *)
(* 指定数据元素： "Data" | "Sheets" *)
Import["D:/test.xlsx", {"Data", 1}];(* 导入第1个 Sheet ，可用 "Sheets" 替换 "Data" *)
Import["D:/test.xlsx", {"Data", 1, 2}];(* 导入第1个 Sheet 中的第2行，可用 "Sheets" 替换 "Data" *)
Import["D:/test.xlsx", {"Data", 1, 2, 3}];(* 导入第1个 Sheet 中的第2行第3列，可用 "Sheets" 替换 "Data" *)
Import["D:/test.xlsx", {"Data", "Sheet2", 3}](* 导入名为“Sheet2”的表中的第3行，可用 "Sheets" 替换 "Data" *)


(* 指定公式元素： "Formulas" *)
Import["D:/test.xlsx", {"Formulas", 1}](* 第1个 Sheet 中的公式，非公式部分为空 *)

(* 指定图像元素： "Images" *)
Import["D:/test.xlsx", {"Images", 1}](* 第1个 Sheet 中的图像，不包括图表 *)
{% endraw %}
```
<!--endsec-->

<!--sec data-title="当 Excel 文件过大时，可以做以下设置" data-id="section5" data-show=true data-collapse=true ces-->
```mma{% raw %}
Needs["JLink`"];
ReinstallJava[JVMArguments -> "-Xmx512m"];(* 其中的数字越大，所支持的数据量越大 *)
{% endraw %}
```
<!--endsec-->


## 纯文本文件的导入导出
* **优点**：
* **缺点**：
* **扩展名**：.txt | .csv
* **注意事项**：
* **导入函数**： `Import`
* **导出函数**： `Export` | `Write` | `WriteLine`

## JSON 文件的导入导出
* **优点**：
* **缺点**：
* **扩展名**：.json
* **注意事项**：
* **导入函数**： `Import` | `ImportString` | ```JSONTools`FromJSON```
* **导出函数**： `Export` | `ExportString` | ```JSONTools`ToJSON```
