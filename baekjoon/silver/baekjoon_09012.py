# 괄호

# 스택 개념을 통해 풀어보자
# 괄호는 가장 마지막에 열린것이 가장 먼저 닫히는 것과 매칭되어야 한다.

count = int(input())

for _ in range(count) :
    char = input()
    
    lst = []
    flag = True
    for i in char :
        # 열린것 저장
        if i == "(" :
            lst.append(i)
        else :
            # 닫힌 것이 나왔을때 리스트가 들어있으면 닫아주기
            if lst :
                lst.pop()
            # 리스트가 없는데 닫힌게 나오면 이상한것
            else :
                flag = False
                break
    
    if flag :
        if lst :
            print("NO")
        else :
            print("YES")
    else :
        print("NO")