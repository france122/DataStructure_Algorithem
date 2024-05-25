#!/user/bin/env python3
# -*- coding: utf-8 -*-
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
    capicity,m=map(int,input().split())
    dp = [[0] * (capicity + 1) for _ in range(m)]
    weights=[]
    values=[]
    for number in range(m):
        time,value=map(int,input().split())
        weights.append(time)
        values.append(value)
    max_value=process(weights,values,capicity,dp)
    print(max_value)



