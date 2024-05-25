#!/user/bin/env python3
# -*- coding: utf-8 -*-
def min3(a, b, c):
    return min(min(a, b), c)

N = 1005
dp = [[0] * N for _ in range(N)]

str = input()
len_str = len(str)

for i in range(len_str - 1, -1, -1):
    for j in range(i + 1, len_str):
        if str[i] == str[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = min3(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1]) + 1
print(dp[0][len_str - 1])