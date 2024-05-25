def amt(index,height,h):
    if index==0:
        if height<=h[index]:
            return 1
        else:
            return 0
    if height<=h[index]:
        return max(amt(index-1,h[index],h)+1, amt(index-1,height,h))
    else:
        return amt(index-1,height,h)

if __name__=="__main__":
    n = int(input())
    h = [int(x) for x in input().split()]
    print(amt(n-1,0,h))

# 改进方法：把计算过的结果存起来
# 但是在本题目中由于N<16，所以发挥不出大表的优势，反而会使得时间变长
def amt(index,height,h,alist):
    if index==0:
        if height<=h[index]:
            return 1
        else:
            return 0
    if height<=h[index]:
        if alist[index-1][h[index]]>0 and alist[index-1][height]>0:
            return max(alist[index-1][h[index]],alist[index-1][height])
        elif alist[index-1][height]>0:
            return max(amt(index-1,h[index],h,alist)+1,alist[index-1][height])
        elif alist[index-1][h[index]]>0:
            return max(alist[index-1][h[index]],amt(index-1,height,h,alist))
        else:
            return max(amt(index-1,h[index],h,alist)+1, amt(index-1,height,h,alist))
    else:
        if alist[index-1][height]>0:
            return alist[index-1][height]
        else:
            return amt(index-1,height,h,alist)

if __name__=="__main__":
    n = int(input())
    h = [int(x) for x in input().split()]
    alist=[[0]*30001 for _ in range(n)]
    print(amt(n-1,0,h,alist))
