# 12789 도키도키 간식드리미

N = int(input())
students = list(map(int, input().split()))

stack = []
now_num = 1

for student in students:
    stack.append(student)
    while stack and stack[-1] == now_num:
        stack.pop()
        now_num += 1

if stack:
    print('Sad')
else:
    print('Nice')