#!/user/bin/env python3
# -*- coding: utf-8 -*-
import heapq
from typing import List, Tuple
# 根据题意我们可以得出所有的序列和为：1+2 1+2 1+3 2+2 2+2 2+3 3+2 3+2 3+3这九个数，则最小的n个为3 3 4。
# 如果我们将m(设m=2)个序列先从小到大排序，这样我们要求的系列和就变成了
# A0+B0 A1+B0 … An-1+B0
# A0+B1 A1+B1 … A n − 1 An-1An−1+B1
# …
# A0+Bn-1 A1+Bn-1 … An-1+Bn-1
# 由于我们的系列是有序的，则得到的序列和也是有序的，每组序列和的第一个一定是该组中最小的，所以我们就从这些小的中选一个最小的，选完之后去掉，则该组中最小的变成了Ai+1 + Bj；这样重复n次，我们就得到了需要的最小的n个序列和。
#
# 然后考虑m>2的情况，我们可以先合并前两个，得到一个长度为n的序列和，再依次和后面的每一个进行合并，这样对于每一次操作都相当于m=2的情况。

# 原文链接：https://blog.csdn.net/qq_42279796/article/details/98661313
def main():
    t1 = int(input())
    while t1 > 0:
        m, n = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        for _ in range(1, m):
            b = list(map(int, input().split()))
            b.sort()
            # 使用heapq来实现最小堆
            pq = [(a[0] + b[i], 0) for i in range(n)]
            heapq.heapify(pq)
            c = [0] * n
            for i in range(n):
                t = heapq.heappop(pq)
                c[i] = t[0]
                if t[1] + 1 < n:
                    heapq.heappush(pq, (t[0] + a[t[1] + 1] - a[t[1]], t[1] + 1))
            a = c[:]  # 复制列表
        print(" ".join(map(str, a)))
        t1 -= 1
if __name__ == "__main__":
    main()