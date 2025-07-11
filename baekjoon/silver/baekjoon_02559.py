# 수열

n, k = map(int, input().split())
lst = list(map(int, input().split()))

total_lst = [lst[0]]

for i in range(1, n) :
    total_lst.append(total_lst[i-1] + lst[i])

# 맨 처음 값 고정
a_lst = [total_lst[k-1]]
    
# 0, 1, 2, 3, 4
for i in range(n-k) :
    # 5,6,7,8,9
    a_lst.append(total_lst[k+i] - total_lst[i])

if n == k :
    print(sum(lst))
else :
    print(max(a_lst))