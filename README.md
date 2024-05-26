# DataStructure_Algorithem_xzm
    
## 目录结构
列出了前四章上机作业的主要代码，供自己上机考试复习和准备最近的算法岗位面试，分别是：
- 00算法复杂度
- 01线性表
- 02递归与动态规划
- 03排序与查找
- 04树及二叉树算法

## 代表题目
- 机制的股民老张<br>
- 反反复复
- 位查询
- 热土豆问题
- 链表的反转
- 最长公共子序列（动归）
- 美元找零（贪心）
- 月度开销（二分查找）
- 两座孤岛的最短距离（图）
- 求逆序对数（归并排序）
- 重建二叉树（二叉树的遍历）

## 思路解释
- 股民问题交易一次：min_price(最低价格，从prices【0】开始，在遍历的过程中遇到更小的，更新min_price=price),max_profit(在所有的price-min_price中留下最大的，可以用if判断代替max(output列表))
<br>leetcode链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
- 股民问题交易多次：将所有上升段累加
- 股民问题交易2次：动态规划
- 股民问题交易k次
