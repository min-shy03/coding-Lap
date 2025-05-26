# 시간 복잡도 4번

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# def MenOfPassion(A, n):
#     total = 0
#     for i in range(0, n-1):               # i는 0부터 n-2까지 (파이썬은 0-indexed)
#         for j in range(i+1, n):           # j는 i+1부터 n-1까지
#             total += A[i] * A[j]            # A[i] × A[j] 쌍의 곱을 누적
#     return total

