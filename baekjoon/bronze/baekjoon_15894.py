# 수학은 체육과목 입니다

# 피라미드의 둘레

n = int(input())

floor = n - 1

# (n*2) = 양 옆 높이 실선의 둘레 , (1+n) = 맨 윗 부분과 아랫 부분의 둘레 , floor = 각 층 별 둘레
total = (n * 2) + (1 + n) + (floor)

print(total)