# 두 용액

n = int(input())

lst = list(map(int,input().split()))

# 절댓값이 같은 용액이 있으면 바로 끝내버림
abs_lst = [abs(i) for i in lst]

s = set()

for i in abs_lst :
    if i in s :
        print(-i, i)
        quit()
    else :
        s.add(i)

lst.sort()

i = 0
j = n - 1
chr = 2000000001
l = []

while i < j :
    if abs(lst[i] + lst[j]) < chr :
        chr = abs(lst[i] + lst[j])
        l = [lst[i],lst[j]]

        # 어느 쪽이 더 0에 가까운지 비교 후에 값에 따라 포인터 옮기기
        if abs(lst[i+1] + lst[j]) < abs(lst[i] + lst[j-1]) :
            i += 1
        else :
            j -= 1
    elif abs(lst[i] + lst[j]) >= chr :
        if abs(lst[i+1] + lst[j]) < abs(lst[i] + lst[j-1]) :
            i += 1
        else :
            j -= 1

print(*l)