# 숫자의 합

n = int(input())



number = str(input())
num_list = list(number)

for i in range(n):
    num_list[i] = int(num_list[i])

print(sum(num_list))




print()
    
    # print(number)
    # print(type(number))