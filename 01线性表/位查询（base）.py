#!/user/bin/env python3
# -*- coding: utf-8 -*-
def loc_check(i,l):
    number=0
        # 十进制转二进制
    for decnum in l:
        s = []
        output = ""
        while decnum > 0:
            rem = decnum % 2
            decnum = decnum // 2
            s.append(rem)
        while len(s) > 0:
            output += str(s[-1])
            s.pop()

        output=output[::-1]
        if len(output)>i:
            if output[i]!="0":
                number+=1
    return number

if __name__=="__main__":
    re=[]
    N,M=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(M):
        op=input().split()
        if op[0]=="C":
            for j in range(len(l)):
                l[j]=(l[j]+int(op[1]))%65536
        else:
            number=loc_check(int(op[1]),l)

            re.append(number)
    for r in re:
        print(r)
