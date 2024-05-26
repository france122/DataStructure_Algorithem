#!/user/bin/env python3
# -*- coding: utf-8 -*-
col=int(input())
str=input()
if 20>=col>=2 and len(str)<=200:
    row=int(len(str)/col)
    niddle=0
    array=[]
    l_num=0
    while l_num<=row-1 :
        l=list(str[niddle:niddle+col])
        if l_num%2==0:
            array.append(l)
        else:
            l.reverse()
            array.append(l)
        l_num+=1
        niddle = niddle + col

    output=""
    for c in range(col):
        for r in range(row):
            output+=array[r][c]
    print(output)
else:
    print("输入不合法")
