# 정수의 제곱근 판별
def solution(n):
    root = n ** 0.5
    # is_integer()는 float 타입 수에만 사용 가능 정수형에다 쓰면 안됨
    return int(root + 1) ** 2 if root.is_integer() else -1

print(solution(121))