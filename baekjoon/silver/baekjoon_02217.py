import sys

n = int(input())

lst = []

for _ in range(n) :
    kg = int(sys.stdin.readline().strip())
    lst.append(kg)

lst = sorted(lst,reverse=True)

# 가장 중량 로프를 기준으로 전부다 연결한 경우
a = lst[-1] * n

# 중량을 잘 견디는 로프들로만 견디는 경우
b = []
for idx,val in enumerate(lst, start=1) :
    b.append(val * idx)

print(max(a, max(b)))