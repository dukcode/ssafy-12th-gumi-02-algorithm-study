# 사칙연산

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 4):
    N = int(input())
    left = [0] * (N+1)
    value = [0] * (N+1)
    right = [0] * (N+1)
    
    for _ in range(N):
        lst = list(map(str, input().split()))
        for i in range(len(lst)):


        
        print(lst)