# 최댓값 만들기

# 주어진 리스트에서 두 수의 곱으로 가장 큰 수를 만들어라.

# 알고리즘 작성
# 1. 절댓값이 가장 큰 수 두 개를 찾는다.
# 2. 두 수가 둘다 양수 or 음수면 그대로 정답
# 3. 두 수가 부호가 다르면 그 다음으로 절댓값이 큰 수의 부호에 따라 정해주기

def solution(numbers):
    answer = 0

    if len(numbers) == 2 :
        answer = numbers[0] * numbers[1]
    else :
        abs_lst = [abs(i) for i in numbers]
        
        max_1 = numbers.pop(abs_lst.index(max(abs_lst)))
        del abs_lst[abs_lst.index(max(abs_lst))]
        max_2 = numbers.pop(abs_lst.index(max(abs_lst)))
        del abs_lst[abs_lst.index(max(abs_lst))]
        
        if max_1 == 0 or max_2 == 0 :
            answer = 0
        elif (max_1 > 0 and max_2 > 0) or (max_1 < 0 and max_2 < 0) :
            answer = max_1 * max_2
        else : 
            lst_1 = []
            lst_2 = []
            for i in numbers :
                lst_1.append(i * max_1)
                lst_2.append(i * max_2)
            
            if max(lst_1) > max(lst_2) :
                answer = max(lst_1)
            else : 
                answer = max(lst_2)
                
    return answer

# 더 쉽고 빠르게 푸는 방법
# sort 함수를 이용해 맨 앞 두수와 맨 뒤 두수를 곱해 더 큰걸 출력하면 된다.
# 알고리즘 능력을 길러보자..
def solution2(numbers) :
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

print(solution2([10, 20, 30, 5, 5, 20, 5]))