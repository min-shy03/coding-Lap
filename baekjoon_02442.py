# 별 찍기 5번 문제

n = int(input())

count = n - 1
for i in range(1, n + 1) :
    print(" " * count, end="")
    print("*" * (2 * i - 1))
    count -= 1