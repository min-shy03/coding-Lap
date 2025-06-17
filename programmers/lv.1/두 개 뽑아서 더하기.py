# 두 개 뽑아서 더하기

# 모듈 사용법 제대로 숙지하기 순열, 조합 등등에서 유용하게 사용할 수 있다.
import itertools 

def solution(numbers):
    return sorted(list(set(sum(i) for i in itertools.combinations(numbers,2))))

print(solution([2,1,3,4,1]))
