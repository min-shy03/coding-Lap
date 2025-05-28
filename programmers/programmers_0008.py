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

print(solution([1,2,-3,4,-5]))