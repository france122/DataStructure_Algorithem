#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(l, target):
    low, high = 0, len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == target:
            return True
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def checksum(m, l):
    # 假设l已经排序
    if m <= l[0]:
        print("No")
        return
    else:
        for index in range(len(l) // 2 + 1):
            complement = m - l[index]
            if complement >= l[index] and binary_search(l, complement):
                print(l[index], complement)
                return
    print("No")
# 列表里的内置in操作时间复杂度是O(n)，采用顺序查找

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()  # 对列表进行一次排序
    m = int(input())
    checksum(m, l)