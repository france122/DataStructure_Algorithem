#!/user/bin/env python3
# -*- coding: utf-8 -*-
def killed(n,k):
    roster=[i for i in range(1,n+1)]

    num=1
    kill=[]
    while len(roster)>1:
        while num<k:
            roster.append(roster.pop(0))
            num+=1

        kill.append(roster.pop(0))
        num=1
    return kill
if __name__=="__main__":
    n,k=map(int,input().split())
    Re=killed(n,k)
    for r in Re:
        if r!=Re[-1]:
            print(r,end=" ")
        else:
            print(r)