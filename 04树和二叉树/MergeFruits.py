# 哈夫曼编码，贪心算法，每次取最小的两个数相加
def main():
    n = int(input())  # 读取数组长度
    a = list(map(int, input().split()))[:n]  # 读取数组元素
     # 对数组进行排序
    ans = 0
    for i in range(1, n):
        a.sort()
        ans += a[i - 1] + a[i]  # 累加相邻元素之和
        a[i] = a[i - 1] + a[i]  # 更新当前元素为其与前一个元素的和
    print(ans)
if __name__ == "__main__":
    main()