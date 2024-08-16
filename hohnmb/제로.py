k = int(input())

num_list = []
for i in range(1,k+1):
    num = int(input())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()
result = sum(num_list)
print(result)    