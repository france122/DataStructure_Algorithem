#!/user/bin/env python3
# -*- coding: utf-8 -*-
def fib(k):
    if k>2:
        a,b=1,1
        for i in range(2,k):
            a,b=b,a+b
        return b
    else:
        return 1

re=fib(int(input()))
print(re)