# 2798번 블랙잭
# 완전 탐색 공부 위해서 라이브러리 없이 다시 풀어보기 

import itertools
n,m = map(int, input().split())
lst = list(map(int, input().split()))
answer = list(itertools.combinations(lst, 3))
answer = max([sum(i) for i in answer if sum(i) <= m])
print(answer)