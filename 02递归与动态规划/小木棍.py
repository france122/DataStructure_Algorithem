while 1:
    n = int(input())
    if n==0:
        break
    a = list(map(int, input().split()))  # 每根木棍的长度
    a.sort(reverse=True)  # 将木棍从大到小排序
    maxx = sum(a)  # 所有小木棍的长度总和
    pd = False
    vis = [0] * 65
    for len in range(a[0], maxx + 1):
        if maxx % len != 0:
            continue
        pd = False
        vis[1] = 1
        m = maxx // len
        def dfs(k, last, rest):
            #  k 表示当前已选取的木棍数量，last 表示上一个选取的木棍的索引，rest 表示还需要拼凑的木棍长度。
            global pd
            if k == m:
                pd = True
                return
            if rest == 0:
                for i in range(1,n):
                    if vis[i+1] == 0:
                        break
                vis[i+1] = 1
                dfs(k + 1, i, len - a[i])
                vis[i+1] = 0
                return
            for i in range(last + 1, n):
                if vis[i+1] == 0 and a[i] <= rest:
                    vis[i+1] = 1
                    dfs(k, i, rest - a[i])
                    vis[i+1] = 0
                    if pd:
                        return
                    while i < n-1 and a[i] == a[i + 1]:
                        i += 1
        dfs(1, 0, len - a[0])
        if pd:
            print(len)
            break
