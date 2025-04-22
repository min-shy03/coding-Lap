# a/n 이라고 가정하고

# 대각선을 층 수라고 가정하면 a,n 의 최댓값 = 층수의 값이다.

# 각 층수는 a,n 가 대칭형태로 수가 줄고 는다. 
# ex ) 층수가 3 일때 (3/1, 2/2, 1/3)

# 층수가 짝수일때, 홀수일때 리스트를 읽는 순서가 바뀐다.

# 층수 = 층수 내에 있는 분수의 개수 이다. 층수가 늘수록 분수도 증가!

x = int(input())

floor = 1
count = 1
lst = []

# 입력한 숫자가 일정 층수 계단 갯수만큼 오면 스톱.
while count < x :
    # 층수가 오를수록 층수의 단계만큼 계단의 갯수도 오른다!
    count += (floor + 1)
    floor += 1

n = floor

# 리스트에 해당 층수의 분수들을 저장
# 사실 리스트에 저장을 하지 않고도 바로 밑에 구한 location 값으로 분수를 출력할 수 있다.
# 근데 이건 GPT가 알려준 것임으로 스스로 이해한게 아님. 
if floor % 2 == 0 :
    # 층수가 짝수 일 경우 
    for i in range(1,floor+1) :
        lst.append(f"{i}/{n}")
        n -= 1
else :
    # 층수가 홀수 일 경우
    for i in range(1,floor+1) :
        lst.append(f"{n}/{i}")
        n -= 1

location = x - (count - floor)

print(lst[location-1])