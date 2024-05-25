# # 归并排序，求正序对数
# def merge(a, left, right, middle, ans):
#     ta = a[left:right + 1].copy()  # 复制数组的一部分到临时数组
#     i = left
#     index1 = left
#     index2 = middle + 1
#     local_ans = ans
#
#     while index1 <= middle and index2 <= right:
#         if ta[index1 - left] >= ta[index2 - left]:
#             a[i] = ta[index1 - left]
#             i += 1
#             index1 += 1
#         else:
#             a[i] = ta[index2 - left]
#             local_ans += middle - index1 + 1  # 这个右子列元素超过了左子列中剩余的元素
#             i += 1
#             index2 += 1
#
#     while index1 <= middle:
#         a[i] = ta[index1 - left]
#         i += 1
#         index1 += 1
#
#     while index2 <= right:
#         a[i] = ta[index2 - left]
#         i += 1
#         index2 += 1
#
#     return a, local_ans
#
#
# def mergesort(a, left, right, ans):
#     if left < right:
#         middle = (left + right) // 2
#         a, ans = mergesort(a, left, middle, ans)  # 递归调用左半部分，并更新ans
#         a, ans = mergesort(a, middle + 1, right, ans)  # 递归调用右半部分，并更新ans
#         a, ans = merge(a, left, right, middle, ans)  # 合并左右半部分，并更新ans
#     return a, ans
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = list(map(int, input().split()))  # 从输入读取数组a
#     ans = 0  # 初始化逆序对计数器
#     a, ans = mergesort(a, 0, n - 1, ans)  # 调用归并排序并计算逆序对
#     print(ans)  # 输出逆序对数量

def merge_count(left, right):
    merged, count = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged, count

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_count_left = merge_sort_count(arr[:mid])
    right, inv_count_right = merge_sort_count(arr[mid:])
    merged, inv_count_merge = merge_count(left, right)
    return merged, inv_count_left + inv_count_right + inv_count_merge

if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))[::-1]
        print(merge_sort_count(arr)[1])