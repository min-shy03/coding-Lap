n , b = input().split()

b = int(b)

# 0~35 까지 숫자 리스트 생성
lst1 = [str(i) for i in range(0,10)] 
lst2 = [chr(i) for i in range(65,91)]

lst = lst1 + lst2

# 값을 담을 변수
total = 0

# 제곱할 위치
square = len(n)-1

# 수식 돌기
for z in range(len(n)) :
    # 수식별로 돌면서 진수 계산
    result = (b**square) * lst.index(n[z])
    square -= 1 
    total += result

print(total)