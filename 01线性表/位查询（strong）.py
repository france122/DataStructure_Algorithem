#!/user/bin/env python3
# -*- coding: utf-8 -*-
#!/user/bin/env python3
# -*- coding: utf-8 -*-

N,M=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(M):
    op=input().split()
    if op[0]=="C":
        p+=int(op[1])
    else:
        q=0
        for j in l:
            if (j+p) >> int(op[1]) & 1:
                q+=1
        print(q)


