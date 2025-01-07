# 비밀번호 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
for _ in range(n):
    site, password = input().split()
    dict[site] = password



for i in range(m):
    site = str(input().strip())
    if site in dict:
        print(dict[site])