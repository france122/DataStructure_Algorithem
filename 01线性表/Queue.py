#!/user/bin/env python3
# -*- coding: utf-8 -*-
def Quecheck(l):
    Q=[]
    for s in l:
        if s[0]=="+":
            Q.append(s[1])
        else:
            if Q==[]:
                return "no"
            else:
                if Q[0]!=s[1]:
                    return "no"
                del Q[0]
    return "yes"

if __name__=="__main__":
    T=int(input())
    for i in range(T):
        n=int(input())
        l=input().split(" ")
        re=Quecheck(l)
        print("Case",str(i+1)+":",re)

