# 진법 변환 2

lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n , b = map(int,input().split())


total = ""
while True :
    # 더이상 몫으로 나눌 수 없을 때
    if n < b :
        # 마지막 남은 몫 가장 앞에 입력
        total = lst[n] + total
        # 종료
        break
    else :
        # 몫과 나머지 변수에 저장
        n, r = divmod(n, b)
        # 나머지 값 뒤집어서 출력
        total = lst[r] + total

print(total)