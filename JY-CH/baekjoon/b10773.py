# 제로

N = int(input())
num_lst = []
for _ in range(N):

    num = int(input())
    num_lst.append(num)


stack = []
for i in range(len(num_lst)):
    if num_lst[i] != 0:
        stack.append(num_lst[i])
    else:
        stack.pop()

print(sum(stack))


