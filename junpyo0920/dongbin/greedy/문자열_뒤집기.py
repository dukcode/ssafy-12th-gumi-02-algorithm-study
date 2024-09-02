data = input()

zero_cnt = 0
one_cnt = 0

cur_num = -1
for num in data:
    if cur_num == num:
        continue
    cur_num = num
    if num == "0":
        zero_cnt += 1
    else:
        one_cnt += 1

result = min(zero_cnt, one_cnt)
print(result)

'''
입력 예시 1
0001100
'''