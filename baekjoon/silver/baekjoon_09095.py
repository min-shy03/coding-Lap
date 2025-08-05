# 1,2,3 더하기

t = int(input())

dp = [0] * 13

# 숫자가 각 1, 2, 3일 때 경우의 수
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 4부터는 그 전 i - 3 일때 경우의 수에 + 3 한 경우, i - 2 일때 경우의 수에 + 2 한 수씩 다 더해주면 i 일때 경우의 수가 나옴
for i in range(4, 13) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for _ in range(t) :
    print(dp[int(input())])