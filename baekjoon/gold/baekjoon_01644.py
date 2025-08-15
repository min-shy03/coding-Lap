# 소수의 연속합

# 에라토스테네스의 체를 이용한 소수 구하기
def prime(num) :
    num_lst = [True] * (num + 1)

    num_lst[0] = num_lst[1] = False

    for i in range(2, int(num ** 0.5) + 1) :
        if num_lst[i] :
            for j in range(i*i, num + 1, i) :
                num_lst[j] = False
    
    return [i for i,v in enumerate(num_lst) if v]

n = int(input())

if n == 1 :
    print(0)
    quit()

prime_lst = prime(n)

i = 0
j = 0
total = prime_lst[0]
count = 0

l = len(prime_lst)

# 여기서부턴 간단한 투포인터를 통한 연속 합 구하기
while j < l :
    if total == n :
        count += 1
        j += 1
        if j < l :
            total += prime_lst[j]
    elif total < n :
        j += 1
        if j < l :
            total += prime_lst[j]
    else :
        total -= prime_lst[i]
        i += 1

print(count)