# 学习笔记

## 小技巧
python的数组下标访问比hash快多了

l1, l2 = l2, l1
这个语法不但简单，而且思路其实适用于任何语言。
两个变量没有顺序要求，我们可以通过预处理的方式，强制变成有先后关系，这就避免了维护一个中间标量的尴尬

python的异或实现 bool(n1) != bool(n2) js也可以参考


DP 子问题有最优解 -> 全局最优解 找到最优子结构即可向上递推
递归 可以遍历所有解，这个是DP做不到的
