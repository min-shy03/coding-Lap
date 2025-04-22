# 시간 복잡도 기초 3번

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 이 코드의 실행 횟수는 코드1이 정확히 n^2번 실행된다.
# 따라서, 전체 수행 횟수는 n^2번이며
# 시간 복잡도는 O(n^2), 차수는 2이다.

n = int(input())

print(n**2)    # 수행 횟수
print(2)    # 수행 횟수의 차수 (O(n)에서 n의 차수)