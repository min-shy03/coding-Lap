# 시간 복잡도 기초 2번

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }

# 이 코드의 실행 횟수는 코드1이 정확히 n번 실행된다.
# 따라서, 전체 수행 횟수는 n번이며
# 시간 복잡도는 O(n), 차수는 1이다.

n = int(input())

print(n)    # 수행 횟수
print(1)    # 수행 횟수의 차수 (O(n)에서 n의 차수)