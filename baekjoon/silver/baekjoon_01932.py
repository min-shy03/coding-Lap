# 정수 삼각형

n = int(input())

piramid = []

for _ in range(n) :
    lst = list(map(int, input().split()))
    
    piramid.append(lst)

dp = [[0]]

for i in range(1,n + 1) :
    dp.append([0] * i)

for i in range(1, n+1) :
    for j in range(i) :
        if j == 0 :
            dp[i][j] = piramid[i-1][j] + dp[i-1][j]
            continue
        elif j == (i - 1) :
            dp[i][j] = piramid[i-1][j] + dp[i-1][j-1]
        else :
            dp[i][j] = max(piramid[i-1][j] + dp[i-1][j-1], piramid[i-1][j] + dp[i-1][j])

print(max(dp[n]))