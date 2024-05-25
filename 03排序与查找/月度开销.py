#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 检查f=mid值是否满足：遍历如果和小于mid合为一组，如果组数不大于m成立，否则不成立
def check(f,l,m):
    count=0
    x=l.copy()
    while x:
        if len(x)==1:
            x.pop()
            count+=1
        else:
            if x[-1]+x[len(x)-2]<=f:
                add=x[-1] + x[len(x) - 2]
                x.pop()
                x.pop()
                x.append(add)
            else:
                x.pop()
                count+=1
    if count>m:
        return False
    else:
        return True

if __name__=="__main__":
    n,m=map(int,input().split())
    l=[int(input()) for x in range(n)]
    # 最大为sum(l)，最小为max(l),进行二分查找
    L,R=max(l),sum(l)
    output=[R]
    while L<=R:
        mid=(L+R)//2
        if check(mid,l,m):
            output.append(mid)
            R=mid-1
        #如果满足条件，则记下该mid值，继续缩小范围
        else:
            L=mid+1
        #如果不满足条件，则放大m值继续判断
    print(output[-1])

