# 부분합

n, s = map(int, input().split())

lst = list(map(int, input().split()))

i = 0
j = 0
total = lst[0]
count_lst = []

while j < n :
    # 누적합을 계속 더하면서 s보다 커지는 부분이 있으면 하나씩 빼보면서 가장 작은 경우 찾기
    # 구간 합을 구하는 과정
    if total >= s :
        count_lst.append(j - i + 1)
        total -= lst[i]
        i += 1
    
    # s보다 값이 커질때까지 계속 누적합 더하기
    elif total < s :
        j += 1
        if j < n :
            total += lst[j]

print(min(count_lst) if count_lst else 0)