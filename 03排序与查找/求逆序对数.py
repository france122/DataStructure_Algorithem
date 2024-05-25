# 归并排序函数，用于合并两个已排序的数组并计算逆序对数量
def merge_count(left, right):
    merged, count = [], 0  # 初始化合并后的数组和逆序对计数器
    i = j = 0  # 初始化左右数组的索引
    # 合并较小的元素并计算逆序对
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # 计算逆序对数量
            count += len(left) - i
            # 合并剩余的元素
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    #     extend降低了时间复杂度，多开了内存
    return merged, count  # 返回合并后的数组和逆序对数量

# 归并排序的递归函数，用于分割数组并计算逆序对数量
def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0  # 如果数组长度为1或0，直接返回并返回逆序对数量为0

    mid = len(arr) // 2  # 找到数组的中间位置
    left, inv_count_left = merge_sort_count(arr[:mid])  # 对左半部分进行归并排序并计算逆序对
    right, inv_count_right = merge_sort_count(arr[mid:])  # 对右半部分进行归并排序并计算逆序对
    merged, inv_count_merge = merge_count(left, right)  # 合并两个已排序的数组并计算逆序对

    # 返回合并后的数组和总逆序对数量
    return merged, inv_count_left + inv_count_right + inv_count_merge


if __name__ == "__main__":
    while True:
        n = int(input())  # 输入数组长度
        if n == 0:
            break  # 如果长度为0，则退出循环
        else:
            arr = list(map(int, input().split()))[::-1]  # 输入数组元素
            print(merge_sort_count(arr)[1])