# Four Squares

from collections import deque

n = int(input())

dp = [0] * (n + 1)

dp[1] = 1
if n >= 2 :
    dp[2] = 2
if n >= 3 :
    dp[3] = 3

# 제곱 수 리스트
squares = deque([1])

for i in range(4, n + 1) :
    least = 4
    
    # i가 제곱수면 1
    if (i ** 0.5).is_integer() :
        dp[i] = 1
        squares.appendleft(i)
    # i가 제곱수가 아니면
    else :
        # 각 제곱 수를 i 에서 빼보면서 가장 작은 경우의 수를 찾기
        for k in squares :
            if dp[i - k] + 1 < least :
                least = dp[i - k] + 1
        
        dp[i] = least

print(dp[n])