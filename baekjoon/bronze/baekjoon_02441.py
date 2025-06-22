# 별 찍기 4번 문제

n = int(input())

count = 0

for i in range(n) :
    print(" " * i, end="")
    print("*" * (n - count))
    count += 1