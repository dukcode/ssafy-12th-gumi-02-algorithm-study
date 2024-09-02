data = list(map(int, input()))
left_num = 0
for num in data:
    if left_num == 0 or num == 0:
        left_num += num
    else:
        left_num *= num
print(left_num)

'''
입력 예시 1
02984
입력 예시 2
576
'''