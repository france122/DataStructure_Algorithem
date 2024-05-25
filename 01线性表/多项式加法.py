#!/user/bin/env python3
# -*- coding: utf-8 -*-
def pol_parsing(l):
    m={}
    for z in range(1,len(l),2):
        if l[z]<0:
            break
        else:
            if l[z] not in m:
                m[l[z]]=l[z-1]
            else:
                m[l[z]]+=l[z-1]


    return m

def pol_plusing(d1,d2):
    d={}
    for i in d1.keys():
        if i in d2.keys():
            d[i]=d1[i]+d2[i]
        else:
            d[i]=d1[i]

    for j in d2.keys():
        if j not in d1.keys():
            d[j]=d2[j]

    d = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
    return d

def present(d):
    out=""
    for k in d.keys():
        if d[k]!=0:
            out=out+"[ "+str(d[k])+" "+str(k)+" ]"
            if k!=list(d.keys())[-1]:
                out+=" "
    return out



if __name__=="__main__":
    n=int(input())
    re=[]
    for number in range(n):
        l1=list(map(int,input().split(" ")))
        l2=list(map(int,input().split(" ")))
        M1=pol_parsing(l1)
        M2=pol_parsing(l2)

        output=pol_plusing(M1,M2)

        re.append(output)
    for output in re:
        print(present(output))
