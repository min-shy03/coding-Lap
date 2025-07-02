# 비밀번호 찾기

import sys

n , m = map(int, sys.stdin.readline().strip().split())

d = {}

for _ in range(n) :
    site, pw = sys.stdin.readline().strip().split()
    d[site] = pw

for _ in range(m) :
    print(d[sys.stdin.readline().strip()])