# 나이순 정렬

import sys

input = sys.stdin.readline

N = int(input())

member = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    member.append((age, name, i))

member.sort(key=lambda x:(x[0], x[2]))
for mem in member:
    print(mem[0], mem[1])