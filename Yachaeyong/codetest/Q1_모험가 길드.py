# 모험가 길드

N = int(input())
people = list(map(int, input().split()))

groups = 0
members = 0
for fear in people:
    members += 1
    if members >= fear:
        groups += 1
        members = 0

print(groups)