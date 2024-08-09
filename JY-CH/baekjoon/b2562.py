# 최 댓 값

all_num = []

for i in range(9):
    a = (int(input()))
    all_num.append(a)
# print(all_num)


# max_value = all_num[0]
# for i in range(len(all_num)):
#     if max_value < all_num[i]:
#         max_value = all_num[i]

# print(max_value)
# print(all_num.index(max_value) + 1)

print(max(all_num))
print(all_num.index(max(all_num)) + 1)

# 런타임 에러는 왜 나는가.
# 이거 때문에 10분 날린거 ㄹㅈㄷ