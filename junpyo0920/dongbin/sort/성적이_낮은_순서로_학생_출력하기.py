# 2
# 홍길동 97
# 이순신 77

n = int(input())
counts = [[] for _ in range(101)]

for _ in range(n):
    student, score = map(lambda x: x if not x.isdigit() else int(x), input().split())
    counts[score].append(student)

for i in range(101):
    for student in counts[i]:
        print(student, end=" ")
