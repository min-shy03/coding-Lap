# 연속합

n = int(input())

lst = list(map(int, input().split()))

i = 0
j = 0
# 가장 처음 수가 베스트라고 가정
best = 0
total = lst[0]
dp = [0] * n

# dp[i] = i 까지의 연속합 중 가장 크게 나올 수 있는 연속합 값
dp[0] = lst[0]

while j < n :
    if total > best :
        dp[j] = total
        best = total
        j += 1
        if j < n :
            total += lst[j]
    else :
        dp[j] = max(dp[j-1], total) if j != 0 else lst[j]
        j += 1
        
        if j < n :
            # lst[j] > total + lst[j] 일 경우 즉 연속합의 의미가 없을 경우 위치 변경
            if lst[j] > (total + lst[j]) :
                i = j
                total = lst[i]
            # 아니면 계속 추가
            else :
                total += lst[j]

print(max(dp))