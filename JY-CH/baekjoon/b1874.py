# 스택 수열

import sys
input = sys.stdin.readline

# n = int(input())
# stack = []
# result = []

# for _ in range(n):
#     x = int(input())
#     if len(stack) == 0:
#         for num in range(1, x + 1):
#             stack.append(num)
#             result.append('+')
#     while stack and stack[-1] >= x:
#         if stack[-1] == x:
#             stack.pop()
#             result.append('-')
#             break
#         else:
#             stack.pop()
#             result.append('-')


#     if not stack or (stack[-1] < x):
#         if stack:
#             for num in range(stack[-1] + 1, x + 1):
#                 stack.append(num)
#                 result.append('+')
#         else:
#             for num in range(1, x + 1):
#                 stack.append(num)
#                 result.append('+')
#         if stack and stack[-1] == x:
#             stack.pop()
#             result.append('-')

# if len(stack) > 0:
#     print("NO")
# else:
#     print('\n'.join(result))



n = int(input())
stack = []
result = []  # 연산 기록
current = 0  # 현재 push할 숫자

for _ in range(n):
    x = int(input())
    
    # 목표 숫자에 도달할 때까지 push
    while current < x:
        current += 1
        stack.append(current)
        result.append('+')
    
    # 스택의 최상단이 목표 숫자라면 pop
    if stack and stack[-1] == x:
        stack.pop()
        result.append('-')
    else:  # 목표 숫자를 만들 수 없는 경우
        print("NO")
        exit()

# 결과 출력
print('\n'.join(result))