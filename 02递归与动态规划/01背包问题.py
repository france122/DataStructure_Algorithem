#!/user/bin/env python3
# -*- coding: utf-8 -*-
import time
def process(weight,value,cap,dp):
    for index in range(len(weight)):
        for capicity in range(cap+1):
            if capicity==0:
                pass
            else:
                if index==0:
                    if capicity<weight[0]:
                        dp[0][capicity]=0
                    else:
                        dp[0][capicity]=value[0]
                else:
                    if capicity<weight[index]:
                        dp[index][capicity]=dp[index-1][capicity]
                    else:
                        dp[index][capicity]=max(dp[index-1][capicity],dp[index-1][capicity-weight[index]]+value[index])
    return dp[len(weight)-1][cap]

if __name__=="__main__":
    weights=list(map(int,input().split()))
    values=list(map(int,input().split()))
    capicity = int(input())
    dp = [[0] * (capicity + 1) for _ in range(len(weights))]
    start_time = time.time()
    max_value=process(weights,values,capicity,dp)
    print(max_value)
    end_time = time.time()
    print(end_time - start_time)

