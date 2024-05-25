def find_best_cut(R, rectangles):
    best_k = None
    min_area_diff = float('inf')
    for k in range(R + 1):
        left_small_area = 0
        right_small_area = 0
        for L, T, W, H in rectangles:
            if k >= L + W:
                left_small_area += W * H
            elif k <= L:
                right_small_area += W * H
            else:
                left_small_area += (k - L) * H
                right_small_area += (L + W - k) * H

        if left_small_area >= right_small_area:
            difference = left_small_area - right_small_area
            if difference <= min_area_diff:
                min_area_diff = difference
                best_k = k
    return best_k

# 读取输入
R = int(input())
N = int(input())
rectangles = []
for _ in range(N):
    L, T, W, H = map(int, input().split())
    rectangles.append((L, T, W, H))
output = find_best_cut(R, rectangles)
print(output)