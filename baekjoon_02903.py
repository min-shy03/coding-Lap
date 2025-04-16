n = 2

count = int(input())

# 2^count + 1 꼴로 바꿔서 표현도 가능하다 -> 이게 더 좋다. 반복 없어서 지금 코드는 쓸데없는 반복을 실행함.
for _ in range(count) :
    n = n + (n-1)
    
result = n**2
print(result)