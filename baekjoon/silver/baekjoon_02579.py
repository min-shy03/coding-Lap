# 계단 오르기

stair = int(input())

score = [0]

for _ in range(stair) :
    score.append(int(input()))

dp = [0] * (stair + 1)

if stair >= 1 :
    # 계단이 1개일 때는 당연히 첫 계단만 밟는다.
    dp[1] = score[1]
if stair >= 2 :
    # 계단이 2개면 연속 밟아도 2칸까진 괜찮음
    dp[2] = dp[1] + score[2]

# ▶️ 경우 1: i-2 → i
# dp[i-2]까지 온 뒤, 2칸 점프해서 i를 밟음.

# 이때는 i-1 계단은 건너뛰기 때문에 3계단 연속 밟는 문제가 안 생김.

# 점수 합: dp[i-2] + score[i]

# ▶️ 경우 2: i-3 → i-1 → i
# dp[i-3]까지 와서 → i-1, i를 두 계단 연속 밟음.

# 총 밟은 건 i-3, i-1, i → 중간에 한 계단 쉬었으므로 3연속 아님

# 점수 합: dp[i-3] + score[i-1] + score[i]

for i in range(3, stair + 1) :
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[stair])