# Wolfram 语言特色

> 客官别急，此部分尚未完成，作者正在玩命码字呢，先看看其它主题吧 ^_^

---

## 基本规则
* `f[a,b,...]` —— Wolfram 系统中一切对象的基本形式。
  * 比如：`3+3`实际上是`Plus[3,3]`
  * 函数式编程
  * 一切对象都是表达式。像单个的符号称之为原子表达式，也具有返回值，例如：`3`和`Pi`都是原子表达式
  * 一对方括号只有一种作用：参数列表。也可以写成：`f@a`或`f@Sequence[a,b,...]`
* 大小写敏感
* 内置函数使用大驼峰格式：每个单词的首字母大写（`ListLinePlot`）
* 几乎所有内置函数都使用英文全拼。即便它有这长：`MultivariateHypergeometricDistribution`
* 句号代表向量内积或矩阵乘法
* 星号和空格都代表普通乘法，但不建议使用星号。数字和变量之间可省略掉空格
* 分号不是必需的，它的作用是不输出前面语句的结果。但是，在语句块中分号往往是需要的，不然换行也会当作乘法运算符

## 运行

## 前端（笔记本）
* 未命名变量显示为蓝色（可以修改，但不建议）