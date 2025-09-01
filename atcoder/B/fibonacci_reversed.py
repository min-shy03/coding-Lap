# 임의의 X, Y를 입력받아
# A1 = X, A2 = Y일때
# Ai = A(i-1) + A(i-2)의 숫자를 거꾸로 읽은 숫자다. ex) X = 5, Y = 8 이라면 A3 = 13을 거꾸로 읽은 31
# 이 때 A10을 구하라.

x, y = map(int, input().split())

a = [0] * 11

a[1] = x
a[2] = y

for i in range(3, 11) :
    a[i] = int(''.join(reversed(str(a[i-1] + a[i-2]))))

print(a[10])