#!/user/bin/env python3
# -*- coding: utf-8 -*-
def Msquare(n):
    R=[[0 for x in range(2*n-1)] for y in range(2*n-1)]
    cur=[0,0]
    # cur[0]=row,cur[1]=col
    for r in range(1,(2*n-1)*(2*n-1)+1):
        if r==1:
            cur[0]=0
            cur[1]=n - 1
        else:
            if cur==[0,2*n-2]:
                cur[0]+=1
            else:
                if cur[0]==0:
                    cur[0]=2*n-2
                    cur[1]+=1
                elif cur[1]==2*n-2:
                    cur[0]-=1
                    cur[1]=0
                elif R[cur[0]-1][cur[1]+1]!=0:
                    cur[0] += 1
                else:
                    cur[0]-=1
                    cur[1]+=1
        R[cur[0]][cur[1]]=r

    return R


if __name__=="__main__":
    N=int(input())
    l=Msquare(N)
    for row in range(2*N-1):
        for col in range(2*N-1):
            print(l[row][col],end=" ")
        print()