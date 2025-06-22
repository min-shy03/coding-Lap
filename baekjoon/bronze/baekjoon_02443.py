# 별 찍기 6번 문제

n = int(input())


for i in range(n) :
    print(" " * i, end="")
    print("*" * (2 * n - 1))
    n -= 1