n = int(input())
data = list(map(int, input().split()))
data.sort()

groups = 0
members = 0
for fear in data:
    members += 1
    if members >= fear:
        groups += 1
        members = 0

print(groups)

'''
입력 예시 1
5
2 3 1 2 2
'''