# #!/user/bin/env python3
# # -*- coding: utf-8 -*-
dp=[[0]*51 for _ in range(51)]
for number in range(51):
    for madd in range(51):
        if number==0:
            dp[number][madd]=1
        else:
            if madd!=0:
                if number<madd:
                    dp[number][madd]=dp[number][madd]
                else:
                    dp[number][madd]=dp[number][madd-1]+dp[number - madd][madd]

if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            print(dp[n][n])
    except EOFError:
        pass  # 当输入结束时（例如文件末尾或Ctrl+D）退出循环,重点！！！runtime error了三遍才ac就是因为没写except模块

