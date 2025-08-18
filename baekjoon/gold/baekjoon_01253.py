# 좋다

n = int(input())

lst = list(map(int, input().split()))

if n < 2 :
    print(0)
    quit()

lst.sort()

count = 0

for k in range(n) :
    find = lst[k]
    i = 0
    j = n - 1

    while i < j :
        if lst[i] + lst[j] == find :
            # 자기 자신을 포함하면 안됨 = 수식에 0이 있으면 안됨
            if i != k and j != k :
                count += 1
                break
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif lst[i] + lst[j] > find :
            j -= 1
        else :
            i += 1

print(count)