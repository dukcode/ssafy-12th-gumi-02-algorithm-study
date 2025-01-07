# 나머지

num_list = []

for i in range(10):
    a = int(input())
    num_list.append(a)
# print(num_list)

change_list = []

for i in range(len(num_list)):
    if num_list[i] % 42 not in change_list:
        change_list.append(num_list[i] % 42)

print(len(change_list))

# 도현이한테 2대 쳐맞고 나면
# 굉장히 쉽게 느껴지는 문제