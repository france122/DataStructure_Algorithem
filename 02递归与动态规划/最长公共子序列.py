#!/user/bin/env python3
# -*- coding: utf-8 -*-
text1=input()
text2=input()
dp=[[0] * (len(text2)+1) for _ in range(len(text1)+1)]
for i in range(len(text1)+1):
    for j in range(len(text2)+1):
        if i==0 or j==0:
            dp[i][j]=0
        else:
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[len(text1)][len(text2)])
